"""
Simple module for simulating dice rolls.
"""

import argparse
import random


def _get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sides', default=6, type=int)
    parser.add_argument('number', nargs='?', type=int, default=1)
    args = parser.parse_args()
    return args


class Dice:
    """
    >>> d20 = Dice(20)
    >>> 1 <= d20.roll() <= 20
    True
    """

    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


def main():
    """
    Roll n-sided dice and return each result and the total.

    >>> monkeypatch = getfixture('monkeypatch')
    >>> monkeypatch.setattr('sys.argv', ['roll-dice'])
    >>> main()
    rolled ...
    >>> monkeypatch.setattr('sys.argv', ['roll-dice', '2'])
    >>> main()
    rolled ...
    rolled ...
    total ...
    """
    options = _get_options()
    dice = Dice(options.sides)
    rolls = [dice.roll() for n in range(options.number)]
    for roll in rolls:
        print('rolled', roll)
    if options.number > 1:
        print('total', sum(rolls))


__name__ == '__main__' and main()
