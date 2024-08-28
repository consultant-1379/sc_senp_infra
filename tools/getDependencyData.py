#!/usr/bin/python3

__author__ = "ekoteva"

import argparse
import logging
import os
import sys
import yaml

log = logging.getLogger(__name__)
logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s",
                    level=logging.INFO)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',
                        '--name',
                        help="""Name of dependency""",
                        required=True)
    parser.add_argument('-p',
                        '--path',
                        default="csar/requirements.yaml",
                        help="""The path of the requirements.yaml exists""",
                        required=False)
    parser.add_argument('-k',
                        '--key',
                        help="""Set key that value is to be extracted""",
                        default="version",
                        required=False)
    return parser.parse_args()

def exit_and_fail(msg):
    if msg:
        log.error(msg)
    sys.exit(msg)

def read_yaml(yaml_file):
    if not os.path.exists(yaml_file):
        exit_and_fail("Couldn't find file: " + yaml_file)
    with open(yaml_file, 'r') as stream:
        try:
            doc = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            exit_and_fail("Not a yaml file: " + exc)
    return doc

def check_files(file):
    if os.path.isfile(file):
        log.debug(file + " file exists.")
    else:
        exit_and_fail(file + " file does not exist.")

def get_version(args):
    """ Read requirements.yaml file and
        print version of input dependency name"""
    data = None
    check_files(args.path)
    requirements = read_yaml(args.path)
    for dependency in requirements["dependencies"]:
        if dependency['name'] == args.name:
             data = dependency[args.key]
    return data

def main():
    """ This is the main function that does everything """

    # Parse all input arguments
    args = parse_arguments()

    # Print version
    data = get_version(args)
    if data is None:
        exit_and_fail("Failed to identify key " + args.key + " of dependency " + args.name)
    else:
        print(data)

if __name__ == "__main__":
    main()