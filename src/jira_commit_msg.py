import re

TICKET_NUMBER_REGEX = re.compile(r"^[A-Z]{2,}-\d+")
FAIL = 1
PASS = 0
