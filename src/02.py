import time

from pathlib import Path
from aoc_utils.api import load_input

SCRIPT_DIR = Path(__file__).parent.parent
INPUT_FILE = Path(SCRIPT_DIR, "inputs/02.txt")
PART1_SAMPLE = Path(SCRIPT_DIR, "inputs/02_part1_sample.txt")
PART2_SAMPLE = Path(SCRIPT_DIR, "inputs/02_part2_sample.txt")


def part_one():
    with open(INPUT_FILE, mode="rt") as f:
        strings = f.read().split("\n")

    print(f"Part 1: ")


def part_two():
    with open(INPUT_FILE, mode="rt") as f:
        strings = f.read().split("\n")

    print(f"Part 2: ")


if __name__ == "__main__":
    load_input(2)

    t1 = time.perf_counter()
    part_one()
    t2 = time.perf_counter()
    print(f"Part 1 execution time: {t2 - t1:0.4f} seconds")

    t1 = time.perf_counter()
    part_two()
    t2 = time.perf_counter()
    print(f"Part 2 execution time: {t2 - t1:0.4f} seconds")
