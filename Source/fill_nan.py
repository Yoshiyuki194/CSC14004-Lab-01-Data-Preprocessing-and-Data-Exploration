import argparse as arg
import sys
import DataFrame as df

#Parser command line 
parser = arg.ArgumentParser()
parser.add_argument('input', type = str, help = "Path to dataset file")
parser.add_argument('out', type = str, help = "Path to output file")
parser.add_argument('column', help = "Column to fill NaN", type = lambda s: [item for item in s.split(',')])
parser.add_argument('method', type = str, help = 'Method to fill NaN')
args = parser.parse_args()

data = df.DataFrame()
data = data.read_csv(args.input)
for i in args.column:
    if args.method == "mean":
        if data.type(i) == 'Numeric':
            data.fill_nan(i, data.mean(i))
        else:
            arg.ArgumentTypeError('Data type of ' + i + ' must be numeric to use mean method')
    elif args.method == 'median':
        if data.type(i) == 'Numeric':
            data.fill_nan(i, data.median(i))
        else:
            arg.ArgumentTypeError('Data type of ' + i + ' must be numeric to use median method')
    elif args.method == 'mode':
        if data.type(i) == 'Categorical':
            data.fill_nan(i, data.mode(i))
        else:
            arg.ArgumentTypeError('Data type of ' + i + ' must be categorical to use mode method')
            
data.to_csv(args.out)
