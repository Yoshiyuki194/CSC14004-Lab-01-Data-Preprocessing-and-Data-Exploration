from csv import DictReader
from os import path

class DataFrame():
    def __init__(self, columns = [], values = {}) -> None:
        self.columns = columns
        self.values = values

    @staticmethod
    def read_csv(filename):
        with open(filename, "r") as file:
            reader = DictReader(file)
            columns = reader.fieldnames
            values = {attr: [] for attr in columns}

            for row in reader:
                for column in columns:
                    values[column].append(row[column])

        return DataFrame(columns, values)
    
    @staticmethod
    def write_csv(list_columns):
        print(1)

    def __getitem__(self, attr: str):
        return self.values[attr]
    
    def __setitem__(self, attr: str, value):
        self.values[attr] = value
    
    def is_nan(self, column):
        for i in self[column]:
            if i != i or i == "":
                return True
        return False
    
    def fill_nan(self, column, value):
        for i in self[column]:
            if i != i or i == "":
                i = value
    
    def mean(self, column):
        sum, count = 0, 0
        for i in self[column]:
            sum += int(i)
            count +=1
        return sum/count
    
    def median(self, column):
        temp = self[column]
        temp.sort()
        mid = len(temp) // 2
        return (temp[mid] + temp[~mid]) / 2
    
    def mode(self, column):
        temp = self[column]
        temp.sort()
        mid = len(temp) // 2
        return (temp[mid] + temp[~mid]) / 2
    
script_path = path.realpath(__file__)
dir_path = path.dirname(script_path)
input_dir = path.join(dir_path, 'House_Prices')
input_path = path.join(input_dir, 'test.csv')
df = DataFrame.read_csv(input_path)
print(df.mean('LotArea'))