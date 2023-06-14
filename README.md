# Brain Games

[![Maintainability](https://api.codeclimate.com/v1/badges/1882f65ff1ef2ea1ac3f/maintainability)](https://codeclimate.com/github/Mr-Freewan/python-project-49/maintainability)
[![Actions Status](https://github.com/Mr-Freewan/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/Mr-Freewan/python-project-49/actions)

### Description

CLI-based python script. 5 games for brain training:

| Game                | Description                                                              |
|---------------------|--------------------------------------------------------------------------|
| brain-even          | You need to decide if the number is even                                 |
| brain-calc          | You need to solve a simple mathematical expression                       |
| brain-gcd           | You need to find greatest common divisor of two numbers                  |
| brain-progression   | You need to specify the missing element of the arithmetic progression    |
| brain-prime         | You need to decide if the number is prime                                |

Each game consists of three rounds. If you answer correctly, you move on to the next round. If you answer incorrectly in any round, the game ends.

---

### Links

This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://python-poetry.org/)                                        | "Python dependency management and packaging made easy"  |
| [flake8](https://flake8.pycqa.org/)                                         | "Your tool for style guide enforcement"                 |

---

### Installation with pip

    pip install git+https://github.com/Mr-Freewan/brain-games.git
    
Test running after installation:

    brain-games

### Building from repo and test running
Steps (see video below):

    git clone https://github.com/Mr-Freewan/brain-games.git

    cd brain-games/

    poetry install

    poetry build

Test running with poetry:

    poetry run brain-games

Test running without poetry:

    make package-install

    brain-games

[![asciicast](https://asciinema.org/a/hYQNtkBxCGTnsVuZxs9v9ivAY.svg)](https://asciinema.org/a/hYQNtkBxCGTnsVuZxs9v9ivAY)

---

### Games demonstration:

---

### brain-even

Game launch:

    brain-even

or

    poetry run brain-even

[![asciicast](https://asciinema.org/a/fpz9loLHv1wHWKhZqPWVVOL66.svg)](https://asciinema.org/a/fpz9loLHv1wHWKhZqPWVVOL66)

### brain-calc

Game launch:

    brain-calc

or

    poetry run brain-calc

[![asciicast](https://asciinema.org/a/uRWmeOM16gsRtOKBUceeWZPA9.svg)](https://asciinema.org/a/uRWmeOM16gsRtOKBUceeWZPA9)

### brain-gcd

Game launch:

    brain-gcd

or

    poetry run brain-gcd

[![asciicast](https://asciinema.org/a/NuZpqI3mQKiT0o1swWiyox2E6.svg)](https://asciinema.org/a/NuZpqI3mQKiT0o1swWiyox2E6)

### brain-progression

Game launch:

    brain-progression

or

    poetry run brain-progression

[![asciicast](https://asciinema.org/a/FTwWYGbgJcKiw6a7hhiDt0gU2.svg)](https://asciinema.org/a/FTwWYGbgJcKiw6a7hhiDt0gU2)

### brain-prime

Game launch:

    brain-prime

or

    poetry run brain-prime

[![asciicast](https://asciinema.org/a/IJ1aoIilIDD6h8m3yzqrTA359.svg)](https://asciinema.org/a/IJ1aoIilIDD6h8m3yzqrTA359)
