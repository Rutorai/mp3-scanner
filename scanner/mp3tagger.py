import sys

from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH

from scanner.folderscanner import FolderScanner
from scanner.filenameparser import FileNameParser

class Mp3Tagger:
    def __init__(self):
        self.folderscanner = FolderScanner()
        self.filenameparser = FileNameParser()

    def execute(self, rootfolder):
        count = 0
        files = self.folderscanner.list(rootfolder)

        for (path, filename) in files:
            res = self.filenameparser.parse(filename)
            if res:
                (artist, song) = res

                # Create MP3File instance.
                mp3 = MP3File(path + '/' + filename)

                mp3.set_version(VERSION_1)

                # Updated fileds
                mp3.artist = artist
                mp3.song = song

                # Cleared fields
                mp3.album = ''
                mp3.year = ''
                mp3.comment = ''
                mp3.track = 0
                mp3.genre = 255

                mp3.save()

                mp3.set_version(VERSION_2)

                # Updated fileds
                mp3.artist = artist
                mp3.song = song

                # Cleared fields
                mp3.album = ''
                mp3.band = None
                mp3.composer = None
                mp3.copyright = None
                mp3.year = ''
                mp3.comment = ''
                mp3.track = '0'
                mp3.genre = '255'
                mp3.year = None
                mp3.publisher = None
                mp3.url = None

                mp3.save()

                mp3.set_version(VERSION_BOTH)
                print(mp3.get_tags())
            else:
                count += 1
                print(path + '/' + filename + ": Not processed!")

        print(str(count) + ' not processed')

if __name__ == '__main__':
    mp3tagger = Mp3Tagger()
    mp3tagger.execute(sys.argv[1])
