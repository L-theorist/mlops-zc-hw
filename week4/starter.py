
import pickle, argparse
import pandas as pd


with open('model.bin', 'rb') as f_in:
    dv, lr = pickle.load(f_in)



categorical = ['PUlocationID', 'DOlocationID']

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.dropOff_datetime - df.pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df


parser = argparse.ArgumentParser()
parser.add_argument(
        "--year",
        default=2021,
        help="Reference year "
    )
parser.add_argument(
        "--month",
        default=2,
        help="Reference month "
    )

year = int(parser.parse_args().year)
month = int(parser.parse_args().month)



df = read_data(f'https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_{year:04d}-{month:02d}.parquet')



dicts = df[categorical].to_dict(orient='records')
X_val = dv.transform(dicts)
y_pred = lr.predict(X_val)



print(f"The mean prediction duration for {month:02d}-{year:04d} is {y_pred.mean()}")



df.head()



df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')



df_result = df[['ride_id']]


output_file = f'predictions_fhv_tripdata_{year:04d}-{month:02d}.parquet'



df_result.to_parquet(
    output_file,
    engine='pyarrow',
    compression=None,
    index=False
)

