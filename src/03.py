import collections
import time

from pathlib import Path

from aoc_utils.api import load_input

SCRIPT_DIR = Path(__file__).parent.parent
INPUT_FILE = Path(SCRIPT_DIR, "inputs/03.txt")
SAMPLE_INPUT = Path(SCRIPT_DIR, "inputs/03_sample.txt")


class Grid:
    g: dict[(int, int), chr] = {}

    def __init__(self, file):
        self.g = {(x, y): val for y, line in enumerate(file.split('\n'))
                  for x, val in enumerate(line)}

    def get(self, pos):
        return self.g.get(pos)

    def get_bounds(self):
        xl = min(x for x, y in self.g.keys())
        xh = max(x for x, y in self.g.keys())
        yl = min(y for x, y in self.g.keys())
        yh = max(y for x, y in self.g.keys())
        return xl, xh, yl, yh

    def print(self):
        xl, xh, yl, yh = self.get_bounds()
        for y in range(yl, yh + 1):
            for x in range(xl, xh + 1):
                print(self.g[(x, y)], end='')
            print("\n", end='')


class NumberInGrid:
    g: dict[(int, int), str] = {}
    neighbouring_gear_positions = []

    def __init__(self, num_positions):
        self.g = num_positions

    def has_adjacent_special_char(self, grid):
        neighbour_positions = self.neighbour_positions()

        neighbour_values = []
        for np in neighbour_positions:
            nv = grid.get(np)
            if nv is not None:
                neighbour_values.append(nv)

        if any((not str(n).isnumeric()) and (not n == ".") for n in neighbour_values):
            return True
        return False

    def neighbour_positions(self):
        xl = min(x for x, y in self.g.keys()) - 1
        xh = max(x for x, y in self.g.keys()) + 1
        yl = min(y for x, y in self.g.keys()) - 1
        yh = max(y for x, y in self.g.keys()) + 1

        positions = []

        for x in range(xl, xh + 1):
            for y in range(yl, yh + 1):
                v = self.g.get((x, y))
                if v is None:
                    positions.append((x, y))
        return positions

    def int_value(self):
        str_val = ""
        for v in self.g.values():
            str_val += v
        return int(str_val)


def part_one():
    with open(INPUT_FILE, mode="rt") as f:
        input_file = f.read()

    grid = Grid(input_file)

    numbers_in_grid = get_numbers_in_grid(grid)

    part_nums = []
    for num in numbers_in_grid:
        if num.has_adjacent_special_char(grid):
            part_nums.append(num)

    part_num_values=[]
    for num in part_nums:
        part_num_values.append(num.int_value())
        print(num.int_value())

    print(f"Part 1: {sum(part_num_values)}")


def part_two():
    with open(INPUT_FILE, mode="rt") as f:
        input_file = f.read()

    grid = Grid(input_file)

    numbers_in_grid = get_numbers_in_grid(grid)

    gear_positions_neighbouring_numbers = collections.defaultdict(list)

    for number in numbers_in_grid:
        for n in number.neighbour_positions():
            if grid.get(n) == "*":

                gear_positions_neighbouring_numbers[n].append(number)
                number.neighbouring_gear_positions.append(n)

    result = 0

    for x, y in gear_positions_neighbouring_numbers:
        nums = gear_positions_neighbouring_numbers.get((x, y))
        if len(nums) == 2:
            ratio = nums[0].int_value() * nums[1].int_value()
            result += ratio

    print(f"Part 2: {result}")


def get_numbers_in_grid(grid):
    numbers_in_grid = []
    xl, xh, yl, yh = grid.get_bounds()
    for y in range(yl, yh + 1):
        number_in_grid_positions = None
        for x in range(xl, xh + 1):
            grid_val = grid.get((x, y))
            if str(grid_val).isnumeric():
                if number_in_grid_positions is None:
                    number_in_grid_positions = {(x, y): grid_val}
                else:
                    number_in_grid_positions[(x, y)] = grid_val
            else:
                if number_in_grid_positions is not None:
                    numbers_in_grid.append(NumberInGrid(number_in_grid_positions))
                    number_in_grid_positions = None
        if number_in_grid_positions is not None:
            numbers_in_grid.append(NumberInGrid(number_in_grid_positions))
    return numbers_in_grid


if __name__ == "__main__":
    load_input(3)

    t1 = time.perf_counter()
    part_one()
    t2 = time.perf_counter()
    print(f"Part 1 execution time: {t2 - t1:0.4f} seconds")

    t1 = time.perf_counter()
    part_two()
    t2 = time.perf_counter()
    print(f"Part 2 execution time: {t2 - t1:0.4f} seconds")
