from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from settings import DB_URL, HOME_DIR

engine = create_engine(DB_URL, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Scenario(Base):
    __tablename__ = "scenarios"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    credentials = relationship("Credential")
    web_history = relationship("EvidenceWebHistory")
    web_downloads = relationship("EvidenceWebDownload")
    files = relationship("EvidenceFile")


class Credential(Base):
    __tablename__ = "credentials"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    scenario = Column(Integer, ForeignKey('scenarios.id'))


class EvidenceWebHistory(Base):
    __tablename__ = "web_history"

    id = Column(Integer, primary_key=True)
    url = Column(String)
    incriminating = Column(Boolean)
    scenario = Column(Integer, ForeignKey('scenarios.id'))

class EvidenceWebDownload(Base):
    __tablename__ = "web_downloads"

    id = Column(Integer, primary_key=True)
    url = Column(String)
    file_path = Column(String)
    incriminating = Column(Boolean)
    scenario = Column(Integer, ForeignKey('scenarios.id'))


class EvidenceFile(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)
    file_path = Column(String)
    contents = Column(String)
    scenario = Column(Integer, ForeignKey('scenarios.id'))


def init_db():
    Base.metadata.create_all(engine)


def seed_db():
    session = Session()
    #Scenarios
    scenario_murder = Scenario(name="murder")
    scenario_blackmail = Scenario(name="blackmail")

    session.add_all([scenario_murder, scenario_blackmail])
    session.commit()

    scenario_murder = session.query(Scenario).filter_by(name="murder").first()
    scenario_blackmail = session.query(Scenario).filter_by(name="blackmail").first()

    #EvidenceFiles
    murder_plot = EvidenceFile(file_path=HOME_DIR+"Documents/Secret/plot.txt",
                               contents="Under the darkness of night I shall murder them",
                               scenario=scenario_murder.id)
    murder_confession = EvidenceFile(file_path=HOME_DIR+"confession.txt",
                                     contents="I confess to murdering them",
                                     scenario=scenario_murder.id)
    blackmail_draft = EvidenceFile(file_path=HOME_DIR+"Documents/blackmail_draft.txt",
                                   contents="I know what you've done, everyone's done something",
                                   scenario=scenario_blackmail.id)

    session.add_all([murder_plot, murder_confession, blackmail_draft])
    session.commit()

