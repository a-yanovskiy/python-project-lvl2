import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate diff")

    parser.add_argument("-f",
                        "--format",
                        dest='format',
                        type=str,
                        default='stylish')
    parser.add_argument("first_file", type=str, help="first_file")
    parser.add_argument("second_file", type=str, help="second_file")

    args = parser.parse_args()
    args_dict = vars(args)
    first_file = args_dict["first_file"]
    second_file = args_dict["second_file"]
    format = args.format

    return first_file, second_file, format
