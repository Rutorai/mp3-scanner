import sys
import taglib

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
                mp3 = taglib.File(path + '/' + filename)

                for k in list(mp3.tags):
                    if not (k == 'ARTIST') and not (k == 'TITLE'):
                        del mp3.tags[k]

                # Updated fileds
                mp3.tags['ARTIST'] = artist
                mp3.tags['TITLE'] = song

                mp3.save()

                print(mp3.tags)
            else:
                count += 1
                print(path + '/' + filename + ": Not processed!")

        print(str(count) + ' not processed')

if __name__ == '__main__':
    mp3tagger = Mp3Tagger()
    mp3tagger.execute(sys.argv[1])
