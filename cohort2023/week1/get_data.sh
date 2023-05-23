#!/bin/bash

mkdir -p ../data
curl -sS https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet > ../data/yellow_tripdata_2022-01.parquet
curl -sS https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-02.parquet > ../data/yellow_tripdata_2022-02.parquet