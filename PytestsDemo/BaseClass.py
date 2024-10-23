import inspect
import  logging



class Loggers:
    def getLoggers(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        # To give File location or file name we should use logging class
        fileHandler = logging.FileHandler("logFile.log")
        # Now Giving a Format to logs to print in the File
        LogFormat = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(LogFormat)
        # Where it should print
        logger.addHandler(fileHandler)
        # To set-Level for the log
        logger.setLevel(logging.INFO)
        return logger
