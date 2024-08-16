import argparse
import sys


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo_url", help="Provide the GitHub Repo URL",
                        type=str, default='repo_url')
    args = parser.parse_args()
    return args


def write_to_file(filename, content):
    with open(filename, 'a+') as f:
        f.write(content)
