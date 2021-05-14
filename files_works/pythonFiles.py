from os import write
import csv
import json

class pythonFiles:

    def __init__(self):
        """ Construct a PythonFile object which holds a test file.
            Test file is inside the files directory.

        Args:
            None
        """

        self.reading_file = 'files\\testingFile.txt'
        self.csv_file = 'files\\logger.csv'
        self.json_file = 'files\\test.json'

    def read_whole_file(self):
        """ Read the entire contents of the field file

        Args:
            None
        Return:
            lines: All lines from the file
        """

        with open(self.reading_file) as test_file:
            # Grabs the whole document
            lines = test_file.read()
            return lines
    
    def read_line_by_line(self):
        """ Read the contents of the field file line by line

        Args:
            None
        Return:
            str1.join(line_array): joins all lines which are read and returns the entire file's contents
        """

        line_array = []
        str1 = "\n"
        with open(self.reading_file) as test_file:
            for each_line in test_file:
                line_array.append(each_line)
        
            return str1.join(line_array)
    
    def write_to_file(self, content: str):
        """ Write given string to the file

        Args:
            content: contents that is going to be written to the file
        Return:
            None
        """

        with open(self.reading_file,'w') as write_to_file:
            write_to_file.write(content)
        
    def append_file(self, content: str):
        """ appends the given string to the string

        Args:
            content: contents that is going to be written to the
        Return:
            None
        """

        with open(self.reading_file, 'a') as append_file:
            append_file.write(content)
        
    def read_csv_file(self):
        with open(self.csv_file) as file:
            print(file.read())
    
    def csv_to_dict(self, delimit: str):
        """ Uses a DictReader method from the import object csv to create a dictionary of the columns 
            in the csv file. 
        
        NOTE: DictReader creates a list that holds multiple dictionaries that have data
        Args:
            delimit: the delimiter by which to separate the file contents could be any value (; : / , .)
        """

        with open(self.csv_file, newline='') as file:
            file_dict = csv.DictReader(file, delimiter=delimit)
            csv_list = []
            for row in file_dict:
                csv_list.append((row['Name'], row[' Age']))
                print(row['Name'])

    def write_to_csv(self, columns: list, values_to_add: list):
        """Uses a DictWriter.writerow method from the import object csv to write data to a csv file.

        Args:
            columns: column names for the csv file
            values_to_add: row values to add to the csv file under the columns

        Return:
            None
        """
        
        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writerheader(columns)
            for line in values_to_add:
                writer.writerow(line)

    def read_json_file(self):
        """Read a json file into a dictionary and print out contents of the dictionary.

        Args:
            None
        
        Return:
            None
        """

        with open(self.json_file) as file:
            contents = json.load(file)
            print(contents)
    
    def write_to_json(self, source_dict: dict):
        """Write to a json file the contents of the passed dictionary.

        Args:
            source_dict: the dictionary that will be saved on the json file

        Return:
            None
        """

        with open(self.json_file, "w") as file:
            json.dump(source_dict, file)


many = pythonFiles()
many.csv_to_dict(',')


