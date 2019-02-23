import unittest

from scanner.filenameparser import FileNameParser


class TestFileNameParser(unittest.TestCase):
    def setUp(self):
        self.fileNameParser = FileNameParser()

    def test_parse_empty_filename(self):
        properties = self.fileNameParser.parse('')
        self.assertEqual(None, properties)

    def test_parse_invalid_filename(self):
        properties = self.fileNameParser.parse('L artist Le titre.mp3')
        self.assertEqual(None, properties)

    def test_parse_invalid_filename_no_artist(self):
        properties = self.fileNameParser.parse(' - Le titre.mp3')
        self.assertEqual(None, properties)

    def test_parse_invalid_filename_no_title(self):
        properties = self.fileNameParser.parse('L artist - .mp3')
        self.assertEqual(None, properties)

    def test_parse_correct_filename(self):
        properties = self.fileNameParser.parse('L artist - Le titre.mp3')
        self.assertEqual(('L artist', 'Le titre'), properties)


if __name__ == '__main__':
    unittest.main()
