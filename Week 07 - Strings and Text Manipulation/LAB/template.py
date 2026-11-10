"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here


def parse_line(raw_line):
    """Clean a messy IT record and convert it to a dictionary."""
    record = {}

    for part in raw_line.strip().split(","):
        part = part.strip()

        if "=" not in part:
            record["hostname"] = part.lower()
            continue

        key, value = part.split("=", 1)
        key = key.strip().lower()
        value = value.strip()

        if key in ("used", "total"):
            record[key] = float(value)
        else:
            record[key] = value.lower()

    return record


def status_of(record):
    """Return server status based on percentage used."""
    used = record["used"]
    total = record["total"]

    if total <= 0:
        return "FLAGGED"

    percent = (used / total) * 100

    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.


raw_records = []

with open("messy_records.txt", "r") as file:
    for line in file:
        if line.strip():
            raw_records.append(line)


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

total_records = 0
flagged_records = 0

for raw_record in raw_records:
    total_records += 1

    try:
        record = parse_line(raw_record)
        status = status_of(record)

        print("Record:", record)
        print("Status:", status)

        if status != "OK":
            flagged_records += 1

    except (ValueError, KeyError, ZeroDivisionError) as error:
        print("Invalid record:", raw_record.strip())
        print("Error:", error)
        flagged_records += 1

    print("-" * 40)

print(f"Summary: {total_records} records, {flagged_records} flagged")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
