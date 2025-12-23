import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="app.log",
    filemode="a"
)

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

#download pandas numpy matplotlib seaborn scikit-learn requests tiflon beautifulsoup4 
#set up: conda 