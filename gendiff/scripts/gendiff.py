#!/usr/bin/env python3

import argparse
import json

parser = argparse.ArgumentParser(description='Generate diff')

parser.add_argument('-f', '--format')
parser.add_argument('first_file', type=str, help='first_file')
parser.add_argument('second_file', type=str, help='second_file')

args = parser.parse_args()
args_dict = vars(args)
first_file = args_dict['first_file']
second_file = args_dict['second_file']


def generate_diff(first_file, second_file):
    file_1 = json.load(open(first_file))
    file_2 = json.load(open(second_file))

    merged_dict = {**file_1, **file_2}
    list_keys = list(merged_dict.keys())
    list_keys.sort()
    
    for i in list_keys:
        if i in file_1 and i in file_2:
            if file_1[i] == file_2[i]:
                print('  ' + str(i) + ': ' + file_1.get(i))
            else:
                print('- ' + str(i) + ': ' + str(file_1.get(i)))
                print("+ " + str(i) + ': ' + str(file_2.get(i)))
        else:
            if i in file_1:
                print('- ' + str(i) + ': ' + str(file_1.get(i)))
            if i in file_2:
                print('+ ' + str(i) + ': ' + str(file_2.get(i)))


def main():
    generate_diff(first_file, second_file)


if __name__ == '__main__':
    main()
