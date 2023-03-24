import argparse as arg
import sys
import DataFrame as df

#Parser command line 
parser = arg.ArgumentParser()
parser.add_argument('input', type = str, help = "Path to dataset file")
parser.add_argument('out', action = 'store_true', help = "Path to result file")
parser.add_argument('standard', action = 'store_true', help = "Maximun percentage of NaN value", default = 0.5)
args = parser.parse_args()

data = df.DataFrame()
data = data.read_csv(args.input_path)

for i in data.columns:
    if data.count_nan(i) > len(data[i]) * args.standard:
        data.drop(i)

data.to_csv()