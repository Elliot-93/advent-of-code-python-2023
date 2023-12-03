import time

from pathlib import Path

from regex import regex

from aoc_utils.api import load_input

SCRIPT_DIR = Path(__file__).parent.parent
INPUT_FILE = Path(SCRIPT_DIR, "inputs/02.txt")
SAMPLE_INPUT = Path(SCRIPT_DIR, "inputs/02_sample.txt")


class ColourReveal:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


class Game:
    def __init__(self, game_num, colour_reveals):
        self.game_num = game_num
        self.colour_reveals = colour_reveals

    def get_maxes(self):
        return max(self.colour_reveals, key=lambda x: x.red).red, \
            max(self.colour_reveals, key=lambda x: x.green).green, \
            max(self.colour_reveals, key=lambda x: x.blue).blue


def part_one():
    games = parse_games()

    possible_games = []

    bag_total_red = 12
    bag_total_green = 13
    bag_total_blue = 14

    for game in games:
        red_max, green_max, blue_max = game.get_maxes()

        if red_max <= bag_total_red and blue_max <= bag_total_blue and green_max <= bag_total_green:
            possible_games.append(game)

    print(f"Part 1: {sum(game.game_num for game in possible_games)}")


def part_two():
    games = parse_games()

    game_powers = []

    for game in games:
        red_max, green_max, blue_max = game.get_maxes()
        game_powers.append(red_max * green_max * blue_max)

    print(f"Part 2: {sum(game_powers)}")


def parse_games():
    with open(INPUT_FILE, mode="rt") as f:
        game_strings = f.read().split("\n")
    games = []
    for game_string in game_strings:
        game_num = regex.findall(r"Game (\d+):", game_string)[0]

        reveal_strings = game_string.split(";")

        reveals = []

        for reveal_string in reveal_strings:
            red = 0
            red_finds = regex.findall(r"(\d+) red", reveal_string)
            if len(red_finds) > 0:
                red = red_finds[0]

            green = 0
            green_finds = regex.findall(r"(\d+) green", reveal_string)
            if len(green_finds) > 0:
                green = green_finds[0]

            blue = 0
            blue_finds = regex.findall(r"(\d+) blue", reveal_string)
            if len(blue_finds) > 0:
                blue = blue_finds[0]

            reveals.append(ColourReveal(int(red), int(green), int(blue)))

        games.append(Game(int(game_num), reveals))
    return games


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
