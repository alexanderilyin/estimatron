#!/usr/bin/env python3
import os
import logging
import click # TODO /usr/local/bin/python3 -m pip install click==8.0.1
import coloredlogs # TODO /usr/local/bin/python3 -m pip install coloredlogs==15.0.1
from prettytable import PrettyTable # TODO /usr/local/bin/python3 -m pip install prettytable==2.2.0

logging_level = os.environ.get('LOGGING_LEVEL', logging.INFO)

coloredlogs.install(fmt='%(asctime)s %(levelname)s %(message)s', datefmt="%m/%d/%Y %I:%M:%S %p %Z")
coloredlogs.set_level(logging_level)
logging.basicConfig(level=coloredlogs.get_level())
logging.getLogger().setLevel(logging_level)

complexity_level = 0
table = PrettyTable()
title = "Software projects sorted by increasing difficulty:"
goals = [
    "criticizing existing thing",
    "maintaining own thing",
    "rewriting own thing",
    "writing a new thing",
    "rewriting somebody else’s thing",
    "maintaining somebody else’s thing",
    "moving from old thing to new thing",
    "turning off old thing",
]
table.field_names = ["Goal", "Complexity"]
table.align["Goal"] = "l"
score = 0

for goal in goals:
    complexity_level += 1
    logging.debug("Setting complexity level '%s' for '%s'.", complexity_level, goal.capitalize())
    table.add_row([goal.capitalize(), complexity_level])
    yes = click.confirm(f'Are you going to {goal}?', goal)
    if yes:
        score += pow(2, complexity_level)

for row in table.get_string().splitlines():
    logging.debug(row)

logging.info("Your score: %s", score)