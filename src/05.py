import collections
import re
import sys
import time

from pathlib import Path

from aoc_utils.api import load_input

SCRIPT_DIR = Path(__file__).parent.parent
INPUT_FILE = Path(SCRIPT_DIR, "inputs/05.txt")
SAMPLE_INPUT = Path(SCRIPT_DIR, "inputs/05_sample.txt")


class ResourceMap:
    def __init__(self, destination_range_start: int, source_range_start: int, range_length: int):
        self.destination_range_start = destination_range_start
        self.source_range_start = source_range_start
        self.range_length = range_length

    def in_range(self, value):
        if self.source_range_start <= value < (self.source_range_start + self.range_length):
            return True
        return False

    def map_value(self, value):
        source_delta = value - self.source_range_start
        return self.destination_range_start + source_delta

class ResourceMapReversed:
    def __init__(self, destination_range_start: int, source_range_start: int, range_length: int):
        self.destination_range_start = destination_range_start
        self.source_range_start = source_range_start
        self.range_length = range_length

    def in_range(self, value):
        if self.destination_range_start <= value < (self.destination_range_start + self.range_length):
            return True
        return False

    def map_value(self, value):
        delta = value - self.destination_range_start
        return self.source_range_start + delta


def map_resource(resource_maps: list[any], value: int):
    for m in resource_maps:
        if m.in_range(value):
            return m.map_value(value)

    return value


def map_source_to_destination(resource_maps_list: list[list[any]], value: int):
    mapped_value = value
    for resource_map in resource_maps_list:
        mapped_value = map_resource(resource_map, mapped_value)

    return mapped_value


def part_one():
    with open(INPUT_FILE, mode="rt") as f:
        groups = f.read().split("\n\n")

    seeds: list[int] = list()
    seed_to_soil: list[ResourceMap] = list()
    soil_to_fertilizer: list[ResourceMap] = list()
    fertilizer_to_water: list[ResourceMap] = list()
    water_to_light: list[ResourceMap] = list()
    light_to_temperature: list[ResourceMap] = list()
    temperature_to_humidity: list[ResourceMap] = list()
    humidity_to_location: list[ResourceMap] = list()

    resource_maps: list[list[ResourceMap]] = [
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location]

    first_group = True
    i = 0
    for group in groups:
        if first_group:
            seeds = [int(x) for x in re.findall(r"(\d+)", group)]
            first_group = False
            continue
        maps = group.split("\n")
        for r_map in maps[1:]:
            list_to_populate = resource_maps[i]
            elements = r_map.split(" ")
            m = ResourceMap(int(elements[0]), int(elements[1]), int(elements[2]))
            list_to_populate.append(m)

        i += 1

    destinations: list[int] = list()

    for seed in seeds:
        destinations.append(map_source_to_destination(resource_maps, seed))

    print(f"Part 1: {min(destinations)}")


def part_two():
    with open(INPUT_FILE, mode="rt") as f:
        groups = f.read().split("\n\n")

    seed_tuples: list[(int, int)] = list()
    seed_to_soil: list[ResourceMapReversed] = list()
    soil_to_fertilizer: list[ResourceMapReversed] = list()
    fertilizer_to_water: list[ResourceMapReversed] = list()
    water_to_light: list[ResourceMapReversed] = list()
    light_to_temperature: list[ResourceMapReversed] = list()
    temperature_to_humidity: list[ResourceMapReversed] = list()
    humidity_to_location: list[ResourceMapReversed] = list()

    resource_maps: list[list[ResourceMapReversed]] = [
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location]

    first_group = True
    group_i = 0
    for group in groups:
        if first_group:

            si = [int(x) for x in re.findall(r"(\d+)", group)]
            for i in range(0, len(si), 2):
                seed_tuples.append((si[i], si[i] + si[i+1]))

            first_group = False
            continue
        maps = group.split("\n")
        for r_map in maps[1:]:
            list_to_populate = resource_maps[group_i]
            elements = r_map.split(" ")
            m = ResourceMapReversed(int(elements[0]), int(elements[1]), int(elements[2]))
            list_to_populate.append(m)

        group_i += 1

    resource_maps.reverse()

    for i in range(0, sys.maxsize):
        result = map_source_to_destination(resource_maps, i)

        for st in seed_tuples:
            if st[0] <= result < st[1]:
                print(f"Part 2: {i}")
                return


if __name__ == "__main__":
    load_input(5)

    t1 = time.perf_counter()
    part_one()
    t2 = time.perf_counter()
    print(f"Part 1 execution time: {t2 - t1:0.4f} seconds")

    t1 = time.perf_counter()
    part_two()
    t2 = time.perf_counter()
    print(f"Part 2 execution time: {t2 - t1:0.4f} seconds")
