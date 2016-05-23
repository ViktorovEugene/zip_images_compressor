import os
import sys
import logging

pkg_dir_name = os.path.dirname(os.path.abspath(__file__))
pkg_name = os.path.basename(pkg_dir_name)
if pkg_name not in sys.modules.keys():
    sys.path.insert(0, os.path.dirname(pkg_dir_name))


from zipic.console_line_interface import parse
from zipic.logger import set_logger
from zipic.processor import process_zip


def main():
    args = parse()
    set_logger(args.verbosity)

    logging.info("Running the Zipic...")

    process_zip(args.file_)

    logging.info("Done!")


if __name__ == "__main__":
    main()
