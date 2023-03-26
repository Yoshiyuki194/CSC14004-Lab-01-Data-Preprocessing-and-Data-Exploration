import argparse as arg
import sys
import DataFrame as df

parser = arg.ArgumentParser()
parser.add_argument('input_path', type = str, help = "Path to the input file")
parser.add_argument('--opt', type = chr, help = "Operator to perform")
parser.add_argument('--column1', type = str, help = "Name of the column as the first operand")
parser.add_argument('--column2', type = str, help = "Name of the column as the second operand")
parser.add_argument('--res', type = str, help = "Name of the result column")
args = parser.parse_args()

data = df.DataFrame.read_csv(args.input_path)
# Verify both columns have numeric data type
if ()
# Parsing
col1 = data[arg.column1]
col2 = data[arg.column2]
tmp = zip(col1, col2)
if args.opt == '+':
    data[arg.res] = [i + j for i, j in tmp]
elif args.out == '-':
    data[arg.res] = [i - j for i, j in tmp]
elif args.out == '*':
    data[arg.res] = [i * j for i, j in tmp]
elif args.out == '/':
    data[arg.res] = [i / j for i, j in tmp]
else:
    arg.ArgumentTypeError('Invalid operators')
