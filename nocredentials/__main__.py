import sys
# Why does this file exist, and why __main__?
# For more info, read:
# - https://www.python.org/dev/peps/pep-0338/
# - https://docs.python.org/2/using/cmdline.html#cmdoption-m
# - https://docs.python.org/3/using/cmdline.html#cmdoption-m

import logging
import argparse
import fileinput

logger = logging.getLogger(__name__)


def parse_args(argv=()):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", help='file to scan',
                        nargs='+')
    return parser.parse_args(argv)


def main(argv=()):
    """
    Args:
        argv (list): List of arguments

    Returns:
        int: A return code

    Does stuff.
    """

    args = parse_args(argv)
    args
    # assume success if we reached here
    return 0

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    sys.exit(main(sys.argv[1:]))
