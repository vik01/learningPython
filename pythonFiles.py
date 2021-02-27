class pythonFiles:

    def __init__(self):
        self.reading_file = 'testingFile.txt'

    def read_whole_file(self):
        with open(self.reading_file) as test_file:
            # Grabs the whole document
            lines = test_file.read()
        
        return lines
    
    def read_line_by_line(self):
        line_array = []
        str1 = ""
        with open(self.reading_file) as test_file:
            for each_line in test_file:
                line_array.append(each_line)
        
        return str1.join(line_array)
    
many = pythonFiles()
print(many.read_whole_file())
