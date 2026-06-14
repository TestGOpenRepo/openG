import logging


def get_logger():

    logger = logging.getLogger(
        "BANK_RECON"
    )

    logger.setLevel(
        logging.INFO
    )

    handler = logging.FileHandler(
        "logs/reconciliation.log"
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    handler.setFormatter(
        formatter
    )

    logger.addHandler(
        handler
    )

    return logger
