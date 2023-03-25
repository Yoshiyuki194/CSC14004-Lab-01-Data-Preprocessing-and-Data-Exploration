import argparse as arg
import sys
import DataFrame as df

#Parser command line 
parser = arg.ArgumentParser()
parser.add_argument('input', type = str, help = "Path to dataset file")
parser.add_argument('out', type = str, help = "Path to result file")
parser.add_argument('standard', type = float, help = "Maximun percentage of NaN value", default = 0.5)
args = parser.parse_args()

data = df.DataFrame.read_csv(args.input)

count = 0
for j in range(len(data[data.columns[0]])):
    if data.count_nan_in_row(j) > (args.standard * len(data[data.columns[0]])):
        data.drop_row(j)
        count += 1

data.to_csv(args.out)
print('Delete ', count, ' row with number of missing value more than', args.standard*100, '%')