import sys
import random
from lib.fs import download_file
from db.SQLite import init_db, EvidenceFile, Session, seed_db, Scenario
from modules.files import File
from settings import *


def init():
    init_db()


def get_index(length, affected):
    rand_index = random.randint(0, files_length -1)
    while rand_index in affected:
        rand_index = random.randint(0, files_length)
    return rand_index


if __name__ == "__main__":
    init()
    scenario_id = 1
    if len(sys.argv) > 1:
        if sys.argv[1] == "seed":
            seed_db()
    session = Session()

    # Getting Scenario from db by name
    murder_scenario = session.query(Scenario).filter_by(name="murder").first()

    # Get all files related to scenario
    files = [File(file.file_path, file.contents) for file in session.query(EvidenceFile).filter_by(scenario=scenario_id).all()]

    # Find out how many files there are, used for generating a random index
    files_length = len(files)
    affected = []

    #Download a file to a specified location
    download_file("https://veldt.me/share/books/Dissertation_Proposal.pdf", HOME_DIR+"calum.pdf")

    for i in range(HIDE_NUM):
        index = get_index(files_length, affected)
        files[index].hidden = True
        affected.append(index)
    for i in range(DELETE_NUM):
        index = get_index(files_length, affected)
        files[index].delete = True
        affected.append(index)
    for i in range(ENCRYPT_NUM):
        index = get_index(files_length, affected)
        files[index].encrypt = True
        affected.append(index)

    for file in files:
        file.run()
