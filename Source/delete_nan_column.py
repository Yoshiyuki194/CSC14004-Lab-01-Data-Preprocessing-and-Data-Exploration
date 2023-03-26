import argparse as arg
import sys
import DataFrame as df

#Parser command line 
parser = arg.ArgumentParser()
parser.add_argument('input', type = str, help = "Path to the dataset file")
parser.add_argument('out', type = str, help = "Path to the result file")
parser.add_argument('standard', type = float, help = "Maximun percentage of NaN value", default = 0.5)
args = parser.parse_args()

data = df.DataFrame.read_csv(args.input)

count = 0
for i in data.columns:
    if data.count_nan(i) > len(data[i]) * args.standard:
        data.drop(i)
        count += 1

data.to_csv(args.out)
print('Delete ', count, ' column with number of missing value more than', args.standard*100, '%')