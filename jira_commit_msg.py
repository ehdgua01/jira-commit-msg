import argparse
import pathlib
import re
import sys

TICKET_NUMBER_REGEX = re.compile(r"^[A-Z]{2,}-\d+")
FAIL = 1
PASS = 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    commit_msg = pathlib.Path(args.filename).read_text()
    if not TICKET_NUMBER_REGEX.match(commit_msg):
        sys.stdout.write("[Aborted] The commit message should start with the jira ticket number.")
        return FAIL
    return PASS
