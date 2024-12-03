import requests
import os
from dotenv import load_dotenv

def get_input(day):
    load_dotenv(".env")
    r = requests.get(f"https://adventofcode.com/2024/day/{day}/input", headers={"Cookie": f"session={os.environ["session_cookie"]}"})
    return r.text()