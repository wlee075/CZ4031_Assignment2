from Interface import InterfaceApp
from datetime import datetime

import json
import logging


def initialiseLogger(log_file):
    """ Initialize logger """
    logging.basicConfig(
        filename=log_file,
        filemode='w',
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s][%(message)s]'
    )

def main():
    """ Main function to explain query """
    config_path = "config.json"
    with open(config_path, "r") as conf_file:
        conf = json.load(conf_file)

    log_path = conf["log"]["log_path"] + datetime.now().strftime("parser_%Y_%m_%d_%H_%M.log")
    initialiseLogger(log_path)
    logging.info("Begin logging")

    db_conf = conf["db"]
    app = InterfaceApp(
        None,
        hostName=db_conf["host"],
        portName=db_conf["port"],
        dbName=db_conf["database"],
        userName=db_conf["username"],
        password=db_conf["password"]
    )
    app.title('Postgres Explanator')
    app.mainloop()

    logging.info("End logging")

if __name__ == "__main__":
    main()
