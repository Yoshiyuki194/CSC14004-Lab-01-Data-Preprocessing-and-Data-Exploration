import argparse as arg
import sys
import DataFrame as df

parser = arg.ArgumentParser()
parser.add_argument('input_path', type = str, help = "Path to the input file")
parser.add_argument('--opt', type = str, help = "Operator to perform")
parser.add_argument('--column1', type = str, help = "Name of the column as the first operand")
parser.add_argument('--column2', type = str, help = "Name of the column as the second operand")
parser.add_argument('--res', type = str, help = "Name of the result column")
args = parser.parse_args()

data = df.DataFrame.read_csv(args.input_path)
# Verify both columns have numeric data type
if data.type(args.column1) != 'Numeric' or data.type(args.column2) != 'Numeric':
   arg.ArgumentTypeError('Invalid pair of columns. Both must have numeric data')
# Parsing
tmp = zip(data[args.column1], data[args.column2])
if args.opt == '+':
    data[args.res] = [float(i) + float(j) if i != '' and j != '' else '' for i, j in tmp]
elif args.opt == '-':
    data[args.res] = [float(i) - float(j) if i != '' and j != '' else '' for i, j in tmp]
elif args.opt == '*':
    data[args.res] = [float(i) * float(j) if i != '' and j != '' else '' for i, j in tmp]
elif args.opt == '/':
    data[args.res] = [float(i) / float(j) if i != '' and j != '' else '' for i, j in tmp]
else:
    arg.ArgumentTypeError('Invalid operators')
data.columns.append(args.res)
data.to_csv(args.input_path)