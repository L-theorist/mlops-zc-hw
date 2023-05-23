from sys import argv
import pandas as pd


if __name__ == '__main__':
    df = pd.read_parquet(argv[1])
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df.duration = df.duration.apply(lambda td: td.total_seconds() / 60)
    print(f"The average duration of trips in {argv[1]} is {df.duration.mean():.2f} minutes.")
    print(f"The standard deviation of the duration distribution of trips in {argv[1]} is {df.duration.std():.2f} minutes.")

    entries_total = df.shape[0]
    df = df[(df['duration'] >= 1) & (df['duration'] <= 60)]
    print(f"{df.shape[0]/entries_total:.0%} is the fraction of the records left after outliers were dropped.")

    # df['PUlocationID'].fillna(-1, inplace=True)
    # print(f"The proportion of trips with missing pickup location is {df[df.PUlocationID == -1].shape[0]/df.shape[0]}.")