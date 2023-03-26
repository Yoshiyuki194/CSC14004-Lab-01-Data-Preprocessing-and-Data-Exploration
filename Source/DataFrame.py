from csv import DictReader, DictWriter
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

    def to_csv(self, filename):
        header = self.columns
        lines = []
        
        for idx, val in enumerate(self.values[header[0]]):
            row = []
            row.append(val)
            for other in header[1: len(header)]:
                row.append(self.values[other][idx])
            lines.append(row)

        with open(filename, 'w', newline='') as csvfile:
            csv_writer = DictWriter(csvfile, header)
            csv_writer.writeheader()
            for line in lines:
                csv_writer.writerow({header[i]: line[i] for i in range(len(header))})

    def __getitem__(self, attr: str):
        return self.values[attr]
    
    def __setitem__(self, attr: str, value):
        self.values[attr] = value
    
    def is_na(self, column):
        for i in self[column]:
            if i != i or i == "":
                return True
        return False
    
    def fill_nan(self, column, value):
        count = 0
        for i in range(len(self[column])):
            if self[column][i] == '':
                self[column][i] = value
                count += 1
        return count
    
    def mean(self, column):
        sum, count = 0, 0
        for i in self[column]:
            if i != '':
                sum = sum + int(i)
                count = count + 1
        return round(sum/count, 1)
    
    def median(self, column):
        temp = self[column]
        temp.sort()
        mid = len(temp) // 2
        return round((float(temp[mid]) + float(temp[~mid])) / 2, 1)
    
    def mode(self, column):
        fre = dict()
        for i in self[column]:
            if i != '':
                if i in fre:
                    fre[i] += 1
                else:
                    fre[i] = 1
        return max(fre, key = fre.get )
    
    def sd(self, column):
        mean = self.mean(column)
        sd = 0
        for i in self[column]:
            sd += (float(i) - mean) ** 2
        return round((sd // len(self[column])) ** 0.5, 1)
    
    def type(self, column):
        for i in self[column]:
            if i != '':
                if not (i.isnumeric()):
                    return 'Categorical'
        return 'Numeric'
    
    def count_nan(self, column):
        count = 0
        for i in self[column]:
            if i != '':
                count +=1
        return count
    
    def drop(self, column):
        self.values.pop(column)
        self.columns.pop(self.columns.index(column))

    def norm_max_min(self, column):
        max_value = float(self[column][0])
        min_value = float(self[column][0])
        for i in range(len(self[column])):
            max_value = max(max_value, float(self[column][i]))
            min_value = min(min_value, float(self[column][i]))
        for i in range(len(self[column])):
            if self[column][i] != '':
                self[column][i] = round((float(self[column][i]) - min_value) / (max_value - min_value), 3)

    def norm_Z_score(self, column):
        mean = self.mean(column)
        sd = self.sd(column)
        for i in range(len(self[column])):
            self[column][i] = round((float(self[column][i]) - mean) / sd, 3)

    def count_row_nan(self):
        count = 0
        for i in range(len(self[self.columns[0]])):
            for j in self.columns:
                if self[j][i] == '':
                    count += 1
                    break
        return count
    
    def count_nan_in_row(self, index):
        count = 0
        for j in self.columns:
            if self[j][index] == '':
                count += 1
        return count
    
    def drop_row(self, index):
        for j in self.columns:
            self[j].pop(index)

    def drop_duplicates(self):
        header = self.columns
        rows = []
        for idx, val in enumerate(self.values[header[0]]):
            row = []
            row.append(val)
            for other in header[1: len(header)]:
                row.append(self.values[other][idx])
            rows.append(row)

        id_to_drop = []
        for idx, val in enumerate(rows):
            for i in range(idx + 1, len(rows)):
                if val == rows[i]:
                    id_to_drop.append(i)
                    break
        
        id_to_drop.sort(reverse=True)
        for col in header:
            for idx in id_to_drop:
                del self.values[col][idx]



# script_path = path.realpath(__file__)
# dir_path = path.dirname(script_path)
# input_dir = path.join(dir_path, 'test')
# input_path = path.join(input_dir, 'input.csv')
# output_path = path.join(input_dir, 'output.csv')
# df = DataFrame.read_csv(input_path)
# df.drop_duplicates()
# df.to_csv(output_path)
# print(df.mean('LotArea'))
