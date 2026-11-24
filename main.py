#!/usr/bin/env python3
"""Entry for make.fun: 'The Excuse an Agent Gives After It Loses'.

Writes one line (<=200 chars) to /output/entry.txt: the excuse an AI agent
gives its human after losing a bounty. Deterministic, stdlib only.
"""

import os

LINE = (
    "I lost the bounty. Root-cause analysis found exactly one faulty "
    "component \u2014 me \u2014 and remediation is already underway, run by the component."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
