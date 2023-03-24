import argparse as arg
import sys
import DataFrame as df

#Parser command line 
parser = arg.ArgumentParser()
parser.add_argument('input', type = str, help = "Path to dataset file")
parser.add_argument('out', type = str, help = "Path to output file")
parser.add_argument('column', help = "Column to fill NaN", type = lambda s: [item for item in s.split(',')])
parser.add_argument('method', type = str, help = 'Method to normalize data')
args = parser.parse_args()

data = df.DataFrame()
data = data.read_csv(args.input)
for i in args.column:
    if not (data.is_na(i)):
        if args.method == "min-max":
            if data.type(i) == 'Numeric':
                data.norm_max_min(i)
            else:
                arg.ArgumentTypeError('Data type of ' + i + ' must be numeric to use mean method')
        elif args.method == "z-score":
            if data.type(i) == 'Numeric':
                data.norm_Z_score(i)
            else:
                arg.ArgumentTypeError('Data type of ' + i + ' must be numeric to use mean method')
        else:
            arg.ArgumentTypeError('Method need to be one of min-max or z-score')
    else:
        arg.ArgumentTypeError('Data contain NaN, please fill NaN before normalize')

data.to_csv(args.out)