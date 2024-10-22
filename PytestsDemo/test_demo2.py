import pytest

@pytest.mark.usefixtures("setup")
class TestingFixtures:
    def test_fixtureCalling(self):
        print("CallingFixture")

    def test_fixtureCallingDemo1(self):
        print("CallingFixture1")

    def test_fixtureCallingDmo2(self):
        print("CallingFixture2")




