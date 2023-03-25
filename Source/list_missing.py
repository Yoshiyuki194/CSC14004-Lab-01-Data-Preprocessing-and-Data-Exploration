import argparse as arg
import sys
import DataFrame as df

#Parser command line 
parser = arg.ArgumentParser()
parser.add_argument('input_path', type = str, help = "Path to dataset file")
parser.add_argument('--print_data', action = 'store_true', help = "Print column with NaN")
parser.add_argument('--output_path', type = str, help = "Path to result file", default = "result_list_missing_column.csv", required='--print_data' in sys.argv)
args = parser.parse_args()

data = df.DataFrame.read_csv(args.input_path)

result = []
for i in data.columns:
    if data.is_na(i):
        result.append(i)

if args.print_data:
    data.write_csv(result)
else:
    print(result)