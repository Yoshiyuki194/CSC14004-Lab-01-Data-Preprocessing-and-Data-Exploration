import argparse as arg
import sys
import DataFrame as df

#Parser command line 
parser = arg.ArgumentParser()
parser.add_argument('input', type = str, help = "Path to the dataset file")
args = parser.parse_args()

data = df.DataFrame.read_csv(args.input)

print('Number of lines with missing data:', data.count_row_nan())