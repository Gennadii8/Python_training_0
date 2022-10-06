import pytest


@pytest.fixture(autouse=False, scope="function")
def set_up_and_tear_down_test_():
    print("Launch browser")
    print("Login")
    print("Find product")
    yield
    print("Logoff")
    print("Close browser")


@pytest.fixture(autouse=True, scope="session")
def set_up_and_tear_down_test_222(browser):
    if browser == "chrome":
        print("Launch chrome")
    elif browser == "firefox":
        print("Launch firefox")
    else:
        print("Provide valid browser")
    print("Login")
    print("Find product")
    yield
    print("Logoff")
    print("Close browser")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(autouse=True, scope="session")
def browser(request):
    return request.config.getoption("--browser")
