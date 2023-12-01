import requests
from os.path import exists


def get_session_id(filename):
    with open(filename) as f:
        return f.read().strip()


def get_url(year, day):
    return f"https://adventofcode.com/{year}/day/{day}/input"


YEAR = 2023
SESSION_ID_FILE = "session.cookie"
SESSION = get_session_id(SESSION_ID_FILE)
COOKIES = {"session": SESSION}


def load_input(day):
    path = f"inputs/{day:02d}.txt"

    if not exists(path):
        url = get_url(YEAR, day)
        response = requests.get(url, cookies=COOKIES)
        if not response.ok:
            raise RuntimeError(
                f"Request failed\n\tstatus code: {response.status_code}\n\tmessage: {response.content}"
            )
        with open(path, "w") as f:
            f.write(response.text[:-1])

        with open(path + "part1_sample.txt", "w") as f:
            f.write("part 1 sample here")

        with open(path + "part2_sample.txt", "w") as f:
            f.write("part 2 sample here")

    with open(path, "r") as f:
        return f.read()
