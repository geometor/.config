"""
run the main app
"""
from .config import Config


def run() -> None:
    reply = Config().run()
    print(reply)
