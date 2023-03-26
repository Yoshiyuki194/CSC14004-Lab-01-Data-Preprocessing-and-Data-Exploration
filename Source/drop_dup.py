import argparse as arg
import sys
import DataFrame as df

parser = arg.ArgumentParser()
parser.add_argument('input_path', type = str, help = "Path to the input file")
parser.add_argument('--out', type = str, help = "Path to the output file")
args = parser.parse_args()

data = df.DataFrame.read_csv(args.input_path)
data.drop_duplicates()
data.to_csv(args.out)

