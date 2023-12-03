import regex
import time

from pathlib import Path
from aoc_utils.api import load_input

SCRIPT_DIR = Path(__file__).parent.parent
INPUT_FILE = Path(SCRIPT_DIR, "inputs/01.txt")
SAMPLE_INPUT = Path(SCRIPT_DIR, "inputs/01_sample.txt")


def part_one():
    with open(INPUT_FILE, mode="rt") as f:
        strings = f.read().split("\n")

    two_digit_nums = []
    for string in strings:
        digit_one = regex.search(r'[0-9]', string).group()
        digit_two = regex.search(r'[0-9]', string[::-1]).group()

        two_digit_nums.append(int(digit_one + digit_two))

    print(f"Part 1: {sum(two_digit_nums)}")


def part_two():
    with open(INPUT_FILE, mode="rt") as f:
        strings = f.read().split("\n")

    two_digit_nums = []
    for string in strings:
        all_found_values = regex.findall(r'[0-9]|one|two|three|four|five|six|seven|eight|nine', string.lower(),
                                         overlapped=True)
        digit_one = all_found_values[0]
        digit_two = all_found_values[-1]

        if not digit_one.isnumeric():
            digit_one = word_int_to_digit(digit_one)

        if not digit_two.isnumeric():
            digit_two = word_int_to_digit(digit_two)

        two_digit_nums.append(int(digit_one + digit_two))

    print(f"Part 2: {sum(two_digit_nums)}")


def word_int_to_digit(string):
    if string == "one":
        return "1"
    elif string == "two":
        return "2"
    elif string == "three":
        return "3"
    elif string == "four":
        return "4"
    elif string == "five":
        return "5"
    elif string == "six":
        return "6"
    elif string == "seven":
        return "7"
    elif string == "eight":
        return "8"
    elif string == "nine":
        return "9"

    return 0


if __name__ == "__main__":
    load_input(1)

    t1 = time.perf_counter()
    part_one()
    t2 = time.perf_counter()
    print(f"Part 1 execution time: {t2 - t1:0.4f} seconds")

    t1 = time.perf_counter()
    part_two()
    t2 = time.perf_counter()
    print(f"Part 2 execution time: {t2 - t1:0.4f} seconds")
