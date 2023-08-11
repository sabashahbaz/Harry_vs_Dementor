
<p align="center">
    </a>
    </a>
    <br>
    <a href="https://docs.python.org/3/index.html"><img src="https://img.shields.io/badge/python-%2320232a?style=for-the-badge&logo=python&logoColor=ffdd54" /></a>
</p>

<h1 align="center"><b>Harry Potter vs Dementors</b></h1>
<h4 align="center"> A simple game using Pygame </h4>

<p align="center">
    <img src="https://www.texomashomepage.com/wp-content/uploads/sites/41/2022/01/harry-potter-light.jpg?strip=1" alt="Project Banner" width=60% height=60%/>
</p>

## Table of Contents

- [Description](#description)
- [Technical Requirements](#technical-requirements)
- [Project Structure](#project-structure)
- [Gameplay Features](#gameplay-features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Description

"Harry vs. Dementors" is an exciting game developed using the Python programming language and the Pygame library. In this game, players take on the role of Harry Potter, who must fend off waves of Dementors that are attacking from the top of the screen. As Harry, you'll have to dodge the Dementors' shots while using your magical abilities to shoot them down.

## Technical Requirements

To run the game locally, you need the following:

- Python 3.7 or later


## Project Directory Hierarchy

Upon successful setup (see **Getting Started**), you should see the following project directory hierarchy.

```
Harry_VS_DEMENTOR-dashboard/
├── __pycache__
├── .venv
├── Assets
├── Classes
│  └──  bullet.py
│  └──  enemy.py
│  └──  game.py
│  └──  main.py
│  └──  player.py
├── Pipfile
└── README.md
```

- `data/`: Directory containing the dataset `nfl_offensive_stats.csv`.
- `app.py`: Main application file containing the Dash app code and callbacks.
- `Pipfile` and `Pipfile.lock`: Files specifying project dependencies when using `pipenv`.
- `README.md`: Project documentation providing an overview, setup instructions, and other details.

## Gameplay Features

Gameplay Features:

Control Harry Potter's movement at the bottom of the screen using arrow keys.
Shoot spells at the Dementors using the left shift key to eliminate them.
Dodge the incoming shots from the Dementors to avoid losing health.
Dementors at the top of the screen shoot spells towards Harry, adding an element of challenge and strategy to the game.
Defeating Dementors earns you points, while getting hit by their spells reduces your health.
The game features dynamic visuals, including character animations and spell effects, thanks to the Pygame library.

## Objectives

Objective:
Survive as long as possible by avoiding the Dementors' spells and eliminating them to earn points. Challenge your reflexes and strategic thinking to achieve a high score and become the ultimate defender against the dark forces.

## How to Play:

How to Play:

Install Python and the Pygame library.
Run the game's main script to start playing.
Use arrow keys to move Harry Potter left and right.
Press the left shift key to shoot spells at the Dementors.
Dodge incoming spells from the Dementors to avoid losing health.
Eliminate Dementors to earn points and increase your score.

## Controls 

Controls:

Arrow Left: Move Harry left
Arrow Right: Move Harry right
Left Shift: Shoot spells
Installation:

Ensure you have Python (version X.X or later) installed.
Install the Pygame library using pip install pygame.
Clone this repository or download the source code.
Run the game by executing the main script.


## Installation: 

1. Clone this repository to your local machine:

```bash
git clone https://github.com/jonrosenblum/nfl-player-stats-dashboard.git
```

2. Navigate to the project directory:

```bash
cd Harry_vs_Dementor
```

3. Install the required dependencies using pipenv:

```bash
pipenv install
```

4. Run the Dash app:

```bash
pipenv run python app.py
```

## Usage

1. Choose a position (Quarterbacks, Running Backs, or Wide Receivers) from the tabs.
2. Select a player from the dropdown menu.
3. Use the radio items to choose the desired statistic.
4. Observe the corresponding bar graph showing the player's statistics.

## Dependencies

The game relies on the following libraries:

- Pygame: A web application framework for building interactive web applications with Python.

## Contributions

Contributions to the game are welcome! If you'd like to add features, fix bugs, or enhance the gameplay, feel free to fork this repository and create a pull request.

## Acknowledgments

This game was inspired by the magical world of Harry Potter and created using the Pygame library, a fantastic tool for game development in Python.

## License

This project is licensed under the MIT License. See the LICENSE file for details.


