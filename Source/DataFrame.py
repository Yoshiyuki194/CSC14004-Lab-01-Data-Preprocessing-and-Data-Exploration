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

    def __getitem__(self, attr: str):
        return self.values[attr]
    
    def __setitem__(self, attr: str, value):
        self.values[attr] = value
    
# script_path = path.realpath(__file__)
# dir_path = path.dirname(script_path)
# input_dir = path.join(dir_path, 'House_Prices')
# input_path = path.join(input_dir, 'test.csv')
# df = DataFrame.read_csv(input_path)
# print(df['LotArea'][:5])