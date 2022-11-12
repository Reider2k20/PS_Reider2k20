import logging

logging.basicConfig(level = logging.DEBUG,
                    filename = "logs2.log",
                    filemode = "w",
                    format = "%(asctime)s:%(levelname)s:%(message)s")

try:
    print(10/0)
except Exception:
    logging.exception("Except")
