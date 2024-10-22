import pytest

@pytest.fixture(scope="class")
def setup():
    print("I am Fixture")
    yield
    print("I will be called in last")

@pytest.fixture()
def passingData():
    print("Passing Data to Methods")
    return ["Alex" "Mercer", "Prototype"]