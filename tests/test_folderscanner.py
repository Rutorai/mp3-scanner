import unittest

from scanner.folderscanner import FolderScanner


class TestFolderScanner(unittest.TestCase):
    def setUp(self):
        self.folderScanner = FolderScanner()

    def test_init(self):
        files = self.folderScanner.files
        self.assertListEqual([], files)

    def test_list(self):
        files = self.folderScanner.list('./tests/resources')
        self.assertListEqual([
            ('./tests/resources/Artiste 1', 'Artiste 1 - Chanson 1.mp3'),
            ('./tests/resources/Artiste 1', 'Artiste 1 - Chanson 2.mp3'),
            ('./tests/resources/Artiste 1', 'Artiste 1 - Chanson 3.mp3'),
            ('./tests/resources/Artiste 1', 'Artiste 1 - Chanson 4.mp3'),
            ('./tests/resources/Artiste 2', 'Artiste 2 - Chanson 1.mp3'),
            ('./tests/resources/Artiste 2', 'Artiste 2 - Chanson 2.mp3')
        ], files)


if __name__ == '__main__':
    unittest.main()
