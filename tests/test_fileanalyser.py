import unittest

from scanner.fileanalysser import FileAnalyser


class TestFileNameParser(unittest.TestCase):
    def setUp(self):
        self.fileAnalyser = FileAnalyser()

    def test_analyse_1(self):
        self.fileAnalyser.analyse('./resources/Noir Désir - Un jour en France.mp3')
    #
    # def test_analyse_2(self):
    #     self.fileAnalyser.analyse('./resources/fic2.mp3')

if __name__ == '__main__':
    unittest.main()
