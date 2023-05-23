from sys import argv
import pandas as pd


if __name__ == '__main__':
    df = pd.read_parquet(argv[1])
    print(f"The number of columns in {argv[1]} is {df.shape[1]}")