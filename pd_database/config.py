import logging

class Logger:
    def __init__(self, log_level: int=logging.INFO):
        self.logger = logging.getLogger("central_logger")
        self.logger.setLevel(log_level)

        # create console handler
        ch = logging.StreamHandler()
        ch.setLevel(log_level)

        # create formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)

        # add the handler to the logger
        self.logger.handlers = []
        self.logger.addHandler(ch)

    def log(self, message: str, level: str="info") -> None:
        if level == "info":
            self.logger.info(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        elif level == "critical":
            self.logger.error(message)
        