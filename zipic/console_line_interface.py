import os
import argparse


def file_name_type(argument):
    if not os.path.isfile(argument):
        raise argparse.ArgumentTypeError("Provided argument should be "
                                         "an existed file name")
    return argument


def parse():
    parser = argparse.ArgumentParser(
        prog='Zipic',
        description="This is the console app intended for compressing image "
                    "files nested in ZIP archive"
    )

    parser.add_argument('file_', type=file_name_type,
                               metavar='file', help="A path to the file.")
    parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
                        help="increase output verbosity")

    return parser.parse_args()
