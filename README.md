# HashPrint

Perform a drunken bishop random walk on a public key fingerprint.

## Installation

Simply run

```bash
pip install hashprint
```

## Example

```python
>>> from hashprint import pformat
>>> print(pformat(bytearray.fromhex('CB7C8A7B567FB2C2ACC2873B04FAC2E9CC21424A')))
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
```

## Testing

Testing is done with tox and pytest.

To add multiple python versions locally, run

```
pyenv install 2.7.9
pyenv install 3.3.6
pyenv install 3.6.2
```

Then simply execute `tox` and have this package tested with the above specified
Python versions one after another.

## Supported Python Versions

- Python 2.7
- Python 3.3
- Python 3.6
