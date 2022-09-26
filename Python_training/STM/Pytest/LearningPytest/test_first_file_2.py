"""Testing file name should be test_*.py or *_test.py"""
import pytest


def test_print_function():
    print("testtttt")


@pytest.mark.example_group
def test_divide():
    assert 6/2 == 3


@pytest.mark.example_group
@pytest.mark.xfail
def test_subtract():
    assert 10-2 == 7


