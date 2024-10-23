from logging import getLogger
from venv import logger

import pytest

from PytestsDemo.BaseClass import Loggers


@pytest.mark.usefixtures("passingData")
class TestExample2(Loggers):
    def test_gettingData(self,passingData):
        log = self.getLoggers()
        log.info(passingData[0])
        log.info(passingData[1])





