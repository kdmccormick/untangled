"""
Test Untangled.
"""

from . import run


def test_placeholder():
    """
    Test placeholder run function.
    """
    assert run() == 42
