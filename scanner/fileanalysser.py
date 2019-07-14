import io


class FileAnalyser:
    ID3_TAG_PATTERN = 'TAG'
    READ_SIZE = 1024

    # def __init__(self):
    #     self.filename_pattern = re.compile(FileNameParser.FILE_NAME_PATTERN)

    def analyse(self, filename, length=READ_SIZE):
        end = False

        file = io.open(filename, 'rb')
        output = io.open(filename + '.txt', 'w')

        while not end:
            tmp = file.read(length)
            output.write(str(tmp) + '')

            if tmp.__len__() != length:
                end = True


        file.close()
        output.close()