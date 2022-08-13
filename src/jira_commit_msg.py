import argparse
import re
import typing as tp

TICKET_NUMBER_REGEX = re.compile(r"^[A-Z]{2,}-\d+")
FAIL = 1
PASS = 0


def main(argv: tp.Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args(argv)
    print(argv, args)
    return PASS


if __name__ == "__main__":
    raise SystemExit(main())
