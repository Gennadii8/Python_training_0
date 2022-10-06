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

If there is a need to make a fixture for many functions, it's worth using conftest.py
Use like in function test_print_function_1(set_up_and_tear_down_test) - just add it like an argument
But better use scope and autouse as a parameters of fixture
autouse=True -> every function will automatically use fixture (no need to write argument in every function)
scope="session" means that fixture will start before first testing function and finish only after all testing functions
scope="function" means that fixture will set before every function and tear down after every function
many other parameters available (check documentation)

In case, where it's needed to check many different arguments in same case (%different login/password combinations,
2 things can be used:
1)params in fixture - @pytest.fixture(params=["a", "b"]) : (parametrized_fixture and test_example_function in this file)
2)parametrize - @pytest.mark.parametrize("a, b, final", [(2, 6, 8), (2, 6, 9), (2, 6, 10)]) (example below).

Also, it's possible to parametrize tests launching with parameters (example in conftest.py :
functions set_up_and_tear_down_test_222 + pytest_addoption + browser). It's just an example of parameters, it doesn't
launch different browsers, just printing different text. for launch pytest -v -s --browser chrome

"""
import pytest


@pytest.fixture()
def set_up_and_finish_test():
    print("Launch browser")
    print("Login")
    print("Find product")
    yield
    print("Logoff")
    print("Close browser")


@pytest.fixture(params=["a", "b"])
def parametrized_fixture(request):
    print(request.param)
    return request.param


@pytest.mark.parametrize("a, b, final", [(2, 6, 8), (2, 6, 9), (2, 6, 10)])
def test_adding(a, b, final):
    assert a + b == final


def test_example_function(parametrized_fixture):
    print(f"example_function - {parametrized_fixture}")


def test_print_function(set_up_and_finish_test):
    print("Some special actions of this function")


def test_print_function_1(set_up_and_tear_down_test):
    print("Some special actions of this function 111")


def test_print_function_2():
    print("Some special actions of this function 222")


@pytest.mark.skip
def test_divide():
    assert 6/2 == 3


@pytest.mark.example_group
def test_subtract():
    assert 10-2 == 8

