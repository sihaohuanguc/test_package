#!/usr/bin/python

import argparse

parser=argparse.ArgumentParser(description="your script description")
parser.add_argument('--input','-i',type=str)
parser.add_argument('--output','-o',type=str)

args=parser.parse_args()

if args.input:
    in_file=args.input
else:
    in_file="./happy_Friday.txt"

print(in_file)
