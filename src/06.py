import collections
import re
import sys
import time

from pathlib import Path

import numpy

from aoc_utils.api import load_input

SCRIPT_DIR = Path(__file__).parent.parent
INPUT_FILE = Path(SCRIPT_DIR, "inputs/06.txt")
SAMPLE_INPUT = Path(SCRIPT_DIR, "inputs/06_sample.txt")


def part_one():
    with open(INPUT_FILE, mode="rt") as f:
        time_distance_input = f.read().split("\n")

    time_records = []

    times = [int(x) for x in re.findall(r"(\d+)", time_distance_input[0])]
    distances = [int(x) for x in re.findall(r"(\d+)", time_distance_input[1])]

    for i in range(0, len(times)):
        time_records.append((times[i], distances[i]))

    ways_to_beat_all_races = []
    for tr in time_records:
        race_time = tr[0]
        record = tr[1]
        ways_to_beat_all_races.append(get_ways_to_beat_count(race_time, record))

    final_result = numpy.prod(ways_to_beat_all_races)

    print(f"Part 1: {final_result}")


def part_two():
    race_time = 63789468
    record = 411127420471035
    ways_to_beat = get_ways_to_beat_count(race_time, record)

    print(f"Part 2: {ways_to_beat}")


def get_ways_to_beat_count(race_time, record: int):
    ways_to_beat = 0
    for hold_time in range(0, race_time):
        result = get_distance(race_time, hold_time)
        if result > record:
            ways_to_beat += 1
    return ways_to_beat


def get_distance(race_time, hold_time: int):
    speed = hold_time
    travel_time = race_time-hold_time
    return speed*travel_time


if __name__ == "__main__":
    load_input(6)

    t1 = time.perf_counter()
    part_one()
    t2 = time.perf_counter()
    print(f"Part 1 execution time: {t2 - t1:0.4f} seconds")

    t1 = time.perf_counter()
    part_two()
    t2 = time.perf_counter()
    print(f"Part 2 execution time: {t2 - t1:0.4f} seconds")
