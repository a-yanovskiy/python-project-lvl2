#!/usr/bin/env python3
from gendiff.cli import parse_arguments
from gendiff.diff import generate_diff


def main():
    first_file, second_file, format = parse_arguments()
    print(generate_diff(first_file, second_file, format))


if __name__ == "__main__":
    main()
