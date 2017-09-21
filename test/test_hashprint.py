"""Test hasprint module."""
import hashprint


def test_grouper():
    """Test grouper."""
    assert list(hashprint.grouper('ABCDEFG', 3)) == [
        ('A', 'B', 'C'), ('D', 'E', 'F'), ('G', None, None)
    ]
