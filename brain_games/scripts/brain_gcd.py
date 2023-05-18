#!/usr/bin/env python3
from brain_games.engine import process_game
from brain_games.games import gcd


def main():
    process_game(gcd)


if __name__ == "__main__":
    main()
