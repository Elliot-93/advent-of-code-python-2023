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
    day_path = f"inputs/{day:02d}"
    input_path = day_path+".txt"

    if not exists(input_path):
        url = get_url(YEAR, day)
        response = requests.get(url, cookies=COOKIES)
        if not response.ok:
            raise RuntimeError(
                f"Request failed\n\tstatus code: {response.status_code}\n\tmessage: {response.content}"
            )
        with open(input_path, "w") as f:
            f.write(response.text[:-1])

        with open(day_path + "_sample.txt", "w") as f:
            f.write("sample here")
