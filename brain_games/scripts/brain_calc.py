#!/usr/bin/env python3
from brain_games.engine import process_game
from brain_games.games import calculator


def main():
    process_game(calculator)


if __name__ == "__main__":
    main()
