import os


class FolderScanner:
    FILE_EXTENSION = '.mp3'

    def __init__(self):
        self.files = []

    def list(self, root_folder):
        for root, dirs, files in os.walk(root_folder):
            for filename in files:
                if filename.endswith(FolderScanner.FILE_EXTENSION):
                    self.files.append((root, filename))

        self.files.sort()

        return self.files
