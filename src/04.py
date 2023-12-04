import collections
import time

from pathlib import Path

from aoc_utils.api import load_input

SCRIPT_DIR = Path(__file__).parent.parent
INPUT_FILE = Path(SCRIPT_DIR, "inputs/04.txt")
SAMPLE_INPUT = Path(SCRIPT_DIR, "inputs/04_sample.txt")


class Card:
    copies: int = 0

    def __init__(self, winning_nums, my_nums):
        self.winning_nums = winning_nums
        self.my_nums = my_nums
        self.copies = 1

    def get_wins(self):
        return len(list(set(self.winning_nums).intersection(self.my_nums)))

    def add_copy(self):
        self.copies += 1

    def get_copy_count(self):
        return self.copies


def part_one():
    with open(INPUT_FILE, mode="rt") as f:
        cards = f.read().split("\n")

    total_points = 0

    for card in cards:
        nums = card.split(": ")[1]
        nums_split = nums.split(" | ")

        winning_nums = nums_split[0].split()
        my_nums = nums_split[1].split()

        my_winning_nums = list(set(winning_nums).intersection(my_nums))

        if len(my_winning_nums) == 0:
            continue

        card_points = 1
        for win in range(0, len(my_winning_nums)-1):
            card_points = card_points*2

        total_points += card_points

    print(f"Part 1: {total_points}")


def part_two():
    with open(INPUT_FILE, mode="rt") as f:
        cards_input = f.read().split("\n")

    cards = []

    for card_input in cards_input:
        nums = card_input.split(": ")[1]
        nums_split = nums.split(" | ")

        winning_nums = nums_split[0].split()
        my_nums = nums_split[1].split()

        cards.append(Card(winning_nums, my_nums))

    current_card_index = -1
    for card in cards:
        current_card_index+=1
        wins = card.get_wins()

        for copy in range(1, card.get_copy_count()+1):
            for subsequent_card_index in range(1, wins+1):
                increment_copy_index = current_card_index + subsequent_card_index
                if increment_copy_index >= len(cards):
                    break
                cards[increment_copy_index].add_copy()

    total_copies = 0
    for card in cards:
        total_copies += card.get_copy_count()

    print(f"Part 2: {total_copies}")


if __name__ == "__main__":
    load_input(4)

    t1 = time.perf_counter()
    part_one()
    t2 = time.perf_counter()
    print(f"Part 1 execution time: {t2 - t1:0.4f} seconds")

    t1 = time.perf_counter()
    part_two()
    t2 = time.perf_counter()
    print(f"Part 2 execution time: {t2 - t1:0.4f} seconds")
