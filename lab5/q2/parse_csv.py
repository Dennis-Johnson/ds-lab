"""parse_csv.py
   Outputs contents of given .csv files for later map reduce stages
"""

import sys
import csv

if len(sys.argv) != 2:
    print("Incorrect usage: expects 1 arg --> dataset path")
    exit(1)

dataset_path = sys.argv[1]

with open(dataset_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        print(f'{" ".join(row)}', end = " ")
