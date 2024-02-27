#!/usr/bin/env python3
from gendiff.functions.arg_parser import get_args
from gendiff.functions.generate_diff import generate_diff


def main():
    args = get_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
