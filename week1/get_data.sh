#!/bin/bash

mkdir -p ../data
curl -sS https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_2021-01.parquet > ../data/fhv_tripdata_2021-01.parquet
curl -sS https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_2021-02.parquet > ../data/fhv_tripdata_2021-02.parquet