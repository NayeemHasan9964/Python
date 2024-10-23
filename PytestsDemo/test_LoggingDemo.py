import  logging

def test_LoggingDemo():
    logger = logging.getLogger(__name__)

    #To give File location or file name we should use logging class
    fileHandler = logging.FileHandler("logFile.log")

    # Now Giving a Format to logs to print in the File
    LogFormat  = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(LogFormat)

    # Where it should print
    logger.addHandler(fileHandler)

    # To set-Level for the log
    logger.setLevel(logging.CRITICAL)

    logger.debug("statement about Debug")
    logger.info("To Know Info about the Test Result")
    logger.warning("To print a Warning Message")
    logger.error("To print Error Message")
    logger.critical("Crtical Issue")