import re


class FileNameParser:
    FILE_NAME_PATTERN = '(?P<artist>.+) - (?P<title>.+).mp3'

    def __init__(self):
        self.filename_pattern = re.compile(FileNameParser.FILE_NAME_PATTERN)

    def parse(self, filename):
        res = self.filename_pattern.match(filename)

        if res:
            return res.group('artist'), res.group('title')