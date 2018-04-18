from lib.fs import create_file, delete_file
from lib.crypt import encrypt

class File:
    def __init__(self, file_path, contents):
        self.file_path = file_path
        self.contents = contents
        self.hidden = False
        self.delete = False
        self.encrypt = False

    def run(self):
        mode = 'w'
        if self.hidden:
            path_parts = self.file_path.split("/")
            path_parts[-1:] = "." + "".join(path_parts[-1:])
            self.file_path = "/".join(path_parts)

        create_file(self.file_path, self.contents, mode=mode)
        if self.delete:
            delete_file(self.file_path)
        elif self.delete:
            pass
            # @TODO Run bash script to encrypt file, pass self.path as an argument using GPG
            # Delete unencrypted file
            delete_file(self.path)
