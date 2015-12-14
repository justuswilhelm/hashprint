HashPrint
=========
Perform a drunken bishop random walk on a public key fingerprint.

Installation
------------
::

  pip install hashprint

Example
-------
::
  >>> from hashprint import pformat
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
