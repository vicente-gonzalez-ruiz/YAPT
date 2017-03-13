import argparse

parser = argparse.ArgumentParser(description='This program bla, bla, bla ...')
parser.add_argument('-i', '--input', help='Input file name', default='stdin')

args = parser.parse_known_args()[0]

if args.input:
    print("Using input file", args.input)

