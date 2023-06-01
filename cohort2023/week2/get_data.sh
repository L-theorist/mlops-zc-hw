#!/bin/bash

mkdir -p ../data
curl -sS https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-01.parquet > ../data/green_tripdata_2022-01.parquet
curl -sS https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-02.parquet > ../data/green_tripdata_2022-02.parquet
curl -sS https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-03.parquet > ../data/green_tripdata_2022-03.parquet

