#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Generate diff')

parser.add_argument('first_file', type=str, help='first_file')
parser.add_argument('second_file', type=str, help='second_file')

args = parser.parse_args()


def main():
    pass


if __name__ == '__main__':
    main()
