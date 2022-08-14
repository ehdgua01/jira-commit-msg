import re
import typing as tp

TICKET_NUMBER_REGEX = re.compile(r"^[A-Z]{2,}-\d+")
FAIL = 1
PASS = 0


def main(argv: tp.Sequence[str] | None = None) -> int:
    print("test")
    print(argv)
    return FAIL
