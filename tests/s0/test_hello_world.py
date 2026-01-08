"""
Stage 0 Tests: Hello World

This test suite verifies that the hello_world function correctly prints "Hello, World!"
"""
import pytest
import sys
from io import StringIO
from project.hello_world import hello_world


def test_hello_world_output(capsys):
    """
    Test that hello_world() prints "Hello, World!" to stdout.
    """
    hello_world()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!", \
        f'Expected "Hello, World!" but got "{captured.out.strip()}"'


def test_hello_world_is_function():
    """
    Test that hello_world is a callable function.
    """
    assert callable(hello_world), "hello_world should be a callable function"


def test_hello_world_exact_output(capsys):
    """
    Test that the output matches exactly (including punctuation).
    """
    hello_world()
    captured = capsys.readouterr()
    output = captured.out.strip()
    assert output == "Hello, World!", \
        f'Output must be exactly "Hello, World!" (got: "{output}")'
    assert "Hello" in output, "Output must contain 'Hello'"
    assert "World" in output, "Output must contain 'World'"
    assert "," in output, "Output must contain a comma"
    assert "!" in output, "Output must contain an exclamation mark"

