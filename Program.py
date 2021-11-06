from Interface import InterfaceApp
from datetime import datetime

import json
import logging


def init_logger(log_file):
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
    init_logger(log_path)
    logging.info("Start logging")

    db_conf = conf["db"]
    app = InterfaceApp(
        None,
        host=db_conf["host"],
        port=db_conf["port"],
        dbname=db_conf["database"],
        user=db_conf["username"],
        password=db_conf["password"]
    )
    app.title('Postgres Query Explainator')
    app.mainloop()

    logging.info("Finished logging")

if __name__ == "__main__":
    main()
