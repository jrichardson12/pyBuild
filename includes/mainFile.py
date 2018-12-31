def driver_file():
    text = """import os
import sys
import datetime
import logging  # debug, info, warning, error, critical


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    logging.basicConfig(filename=dir_path + '/log/' +
                        str(datetime.date.today()) +
                        '.log', level=logging.DEBUG)
    logging.debug(sys.argv[0])


if __name__ == '__main__':
    main()
"""
    return text
