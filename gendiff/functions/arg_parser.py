import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Compares'
                                                 ' two configuration files'
                                                 ' and shows a difference.')
    parser.add_argument('-f', '--format',
                        type=str,
                        default='stylish',
                        help='set format of output (default: "stylish")')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    return parser.parse_args()
