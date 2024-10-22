import pytest


@pytest.mark.usefixtures("passingData")
class TestExample2:
    def test_gettingData(self,passingData):
        print(passingData[1])



