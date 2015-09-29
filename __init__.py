#!/usr/bin/env python
"""
Perform a random walk seeded by a byte array.

Can be used to visualize SSH fingerprints.
Inspiration: http://aarontoponce.org/drunken_bishop.pdf
"""
from itertools import zip_longest


def grouper(iterable, n):
    """
    Collect data into fixed-length chunks or blocks.

    Source: from python 3.5 itertools doc
    >>> list(grouper('ABCDEFG', 3))
    [('A', 'B', 'C'), ('D', 'E', 'F'), ('G', None, None)]
    """
    args = [iter(iterable)] * n
    return zip_longest(*args)


def randomwalk(key, x=17, y=9):
    """
    Perform a drunken bishop random walk on a byte array.

    Values 0 and 1 are reserved for start and end position.
    >>> list(randomwalk(b'', 3, 3))  # Empty walk
    [(2, 2, 2), (2, 1, 2), (2, 2, 2)]
    >>> list(randomwalk(b'asde', 3, 3))
    [(3, 4, 1), (5, 0, 3), (4, 3, 3)]
    """
    size = x * y  # size of random walk field
    position = size // 2  # place bishop in the middle
    assert size % 2, "X * Y must be odd."
    field = [2] * (size)  # random walk field
    field[position] = 0  # set starting point

    def move(pos, dir):  # map 4 possible bitpairs to up/down/left/right
        return ({0: 1, 1: -1, 2: y, 3: -y}[dir] + pos) % size

    for byte in key:
        for bitpair in grouper(bin(byte)[2:].zfill(8), 2):
            field[position] += 1 if field[position] > 1 else 0
            position = move(position, int("".join(bitpair), 2))
    field[position] = 1  # set end point
    return grouper(field, x)


def pformat(key, byte_mapping="SE .o+=*BOX@%&#/^"):
    r"""
    Pretty format a random walk byte array.

    byte_mapping format: "XYZ..." where X and Y are reserved for the start and
    end position and Z signifies a field that hasn't been visited.

    >>> from binascii import unhexlify
    >>> print(pformat(unhexlify('CB7C8A7B567FB2C2ACC2873B04FAC2E9CC21424A')))
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
    field = list(randomwalk(key))
    border = "+" + "-" * len(field[0]) + "+"
    return "\n".join([border] + ["|{}|".format(
        "".join(byte_mapping[cell % len(byte_mapping)] for cell in line))
        for line in field] + [border])
