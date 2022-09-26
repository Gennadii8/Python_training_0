"""
Testing file name should be test_*.py or *_test.py

pytest -v will show details about every test case
pytest --help shows all possible uses

Grouping tests - above needed test add @pytest.mark.GROUP_NAME amd them run test like: pytest -m GROUP_NAME
(It's possible to group test from different files, but probably they have to be in one Directory).
Also, there are built in markers - for example for skipping test: @pytest.mark.skip
Or skip a failing test: @pytest.mark.xfail and many other

For making some "patterns" for setting up and finishing test cases can be used @pytest.fixtures
For separate what will be used before function and after "yield" have to be used
For function which is extended with fixture it's important to write name of that fixture as argument in function
(Example in this file)

"""
import pytest
import sys
from os import path
sys.path.append(r'C:\Users\GennadiiMatveev\Desktop\Training\Python_training\STM\Selenium\Selenium_learning\LearningSelenium')
# from
# from LearningSelenium


@pytest.fixture()
def set_up_and_finish_test():
    print("Launch browser")
    print("Login")
    print("Find product")
    yield
    print("Logoff")
    print("Close browser")


def test_print_function(set_up_and_finish_test):
    print("Some special actions of this function")


@pytest.mark.skip
def test_divide():
    assert 6/2 == 3


@pytest.mark.example_group
def test_subtract():
    assert 10-2 == 8


def test_get_value():
    # TODO finish import from another project
    # value_class = GetAttributeValue()
    # get_value()
    pass
