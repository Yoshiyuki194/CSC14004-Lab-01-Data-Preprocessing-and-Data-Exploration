import argparse as arg
import sys
import DataFrame as df

#Parser command line 
parser = arg.ArgumentParser()
parser.add_argument('input', type = str, help = "Path to dataset file")
parser.add_argument('out', type = str, help = "Path to output file")
parser.add_argument('column', type = str, help = "Column to fill NaN")
parser.add_argument('method', type = str, help = 'Method to fill NaN')
args = parser.parse_args()

data = df.DataFrame.read_csv(args.input)
if args.method == "mean":
    if data.type(args.column) == 'Numeric':
        data.fill_nan(args.column, data.mean(args.column))
    else:
        arg.ArgumentTypeError('Data type of column must be numeric to use mean method')
elif args.method == 'median':
    if data.type(args.column) == 'Numeric':
        data.fill_nan(args.column, data.median(args.column))
    else:
        arg.ArgumentTypeError('Data type of column must be numeric to use median method')
elif args.method == 'mode':
    if data.type(args.column) == 'Categorical':
        data.fill_nan(args.column, data.mode(args.column))
    else:
        arg.ArgumentTypeError('Data type of column must be categorical to use mode method')
else:
    arg.ArgumentTypeError('Method need to be one of mean, median and mode')

#print(data['LotArea'])