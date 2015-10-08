import logging, config

logging.basicConfig(filename=config.LOG_FILENAME,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

def logMessage(message):
    logging.info(message)

if __name__ == "__main__":
    logMessage("test")