import pytest

@pytest.mark.skip
def test_MethodTest(setup):
    print("Hello World!")

@pytest.mark.xfail
def test_greet():
    print("Good Morning")


def test_prototypePart2(Prototype2):
    print(Prototype2)

