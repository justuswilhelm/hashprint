#!/usr/bin/env python
"""
Perform a random walk seeded by a byte array. Can be used to visualize SSH
fingerprints.
http://aarontoponce.org/drunken_bishop.pdf

Example
======

----------------------------------------
CB7C8A7B567FB2C2ACC2873B04FAC2E9CC21424A
----------------------------------------
+-----------------+
|                 |
|                 |
|            +o.o.|
|    *o+++o.oo=o=B|
|X+oo .o.S=+o.    |
|  .        E     |
|                 |
|                 |
|                 |
+-----------------+
"""
from itertools import zip_longest


def grouper(iterable, n, fillvalue=None):
    """
    Collect data into fixed-length chunks or blocks
    from python 3.5 itertools doc
    >>> ["".join(l) for l in grouper('ABCDEFG', 3, 'x')]
    ['ABC', 'DEF', 'Gxx']
    """
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def randomwalk(key, x=17, y=9):
    """
    Perform a drunken bishop random walk on a byte array. Values 0 and 1 are
    reserved for start and end position
    >>> list(randomwalk(b'asde', 3, 3))
    [(3, 4, 1), (5, 0, 3), (4, 3, 3)]
    """
    size = x * y  # size of random walk field
    position = size // 2  # place bishop in the middle
    assert size % 2, "X * Y must be odd."
    field = [2] * (size)  # random walk field
    field[position] = 0  # set starting point

    # map 4 possible bitpairs to up/down/left/right
    def move(pos, dir):
        return ({0: 1, 1: -1, 2: y, 3: -y}[dir] + pos) % size

    for byte in key:
        for bitpair in grouper(bin(byte)[2:].zfill(8), 2):
            if field[position] > 1:  # do not override start/end pos
                field[position] += 1
            position = move(position, int("".join(bitpair), 2))
    field[position] = 1
    return grouper(field, x)


def pformat(key, byte_mapping="SE .o+=*BOX@%&#/^"):
    r"""
    byte_mapping format: "XYZ..." where X and Y are reserved for the start and
    end position and Z signifies a field that hasn't been visited.

    >>> print(pformat(b'asdf'))
    +-----------------+
    |                 |
    |                 |
    |                 |
    |              .. |
    |     o+oS    ...o|
    |.    E           |
    |                 |
    |                 |
    |                 |
    +-----------------+
    >>> print(pformat(range(253), byte_mapping="SE 😁😂😃😄😅😆😇😈👿😉😊☺️😋😌😍"))
    +-----------------+
    |😇😂😅😈😊E😄😅😇😄😂😁😇😉😆😅😂|
    |😃😅😆😄😄👿😈😄😃😄😄😃😃 😇😅😄|
    |😁😂😇😆😅😁️😆😈😅😅😆😁😅😂😌😈|
    |😈😅😈😇😆😆😁S😊😉😊😇😂😄😅😁S|
    |😈😄😈😅 😂😅😁S😊😅😆😃😃😇😆😃|
    |😊☺😈😅😃😆😉👿😅😈😇😇😄😂😂😃👿|
    |😆😅😅😃😃😅👿👿👿👿😇😅😇😇😆👿😇|
    |😆😆😆😄😈😉😇☺️👿👿😉👿😆😉😊👿|
    |😉😇☺☺😉😉😊☺️😆😃😆😅😊😇👿️|
    +-----------------+
    """
    field = list(randomwalk(key))
    border = "+" + "-" * len(field[0]) + "+"
    lines = [border] + [
        "|" +
        "".join(byte_mapping[cell % len(byte_mapping)] for cell in line) +
        "|" for line in field] + [border]
    return "\n".join(lines)


if __name__ == "__main__":
    from binascii import unhexlify
    from sys import stdin

    for line in stdin.readlines():
        line = line.strip().replace(':', '')
        if not line:
            continue
        print('-' * len(line))
        print(line)
        print('-' * len(line))
        print(pformat(unhexlify(line)))
