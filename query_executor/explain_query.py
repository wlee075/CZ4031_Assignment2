"""
Class to explain query plan (without execution)
"""

import json
import logging
import psycopg2

from query_plan_parser.annotation import parse_plan

class Explain:
    """ Class to explain query """
    def __init__(
            self, host, port, dbname, user, password,
            desc=True, voice=False, debug=False
        ):
        """ init Explain """
        conn_string = "host='%s' port='%s' dbname='%s' user='%s' password='%s'"%(
            host, port, dbname, user, password)
        self.conn = psycopg2.connect(conn_string)
        self.cursor = self.conn.cursor()
        
        logging.info("Connected to database: " + conn_string)

        self.desc = desc
        self.debug = debug

        self.query = ""
        self.query_plan = {}
        self.parsed_plan = ""


    def explain(self, query=None):
        """ explain query """
        if query:
            self.query = query

        logging.info("Generating query plan for: " + self.query)
        try:
            self.cursor.execute("EXPLAIN (FORMAT JSON) " + self.query)
            plan = self.cursor.fetchall()
            self.query_plan = plan[0][0][0]["Plan"]
        except:
            logging.error("Generate query plan execution failed")
            self.query_plan = {}
            self.parsed_plan = "Generate query plan execution failed"
            raise
        finally:
            logging.info("Generated query plan: " + json.dumps(self.query_plan, indent=4))

        return self.query_plan
        
    def loop_explain(self):
        """ continuously explain queries """
        print("postgres=# Please input query (end with ';')")
        next_line = ""
        self.query = ""
        while next_line.strip().lower() != "quit":
            next_line = input("postgres=# ")
            self.query += "\n" + next_line.strip()
            if self.query[-1] == ";":
                try:
                    self.explain()
                    self.parse()
                except Exception as exception:
                    logging.error("Error for Explain.explain(): " + str(exception))
                finally:
                    if self.debug:
                        print(json.dumps(self.query_plan, indent=4))
                    if self.desc:
                        print(self.parsed_plan)
                    self.query = ""
    
    def parse(self, query_plan=None):
        """ Parse query plan """
        if query_plan:
            self.query_plan = query_plan

        logging.info("Parsing plan: " + json.dumps(self.query_plan, indent=4))
        try:
            self.parsed_plan = parse_plan(self.query_plan, start=True)
        except:
            logging.error("Parse query plan execution failed")
            self.parsed_plan = "Parse query plan execution failed"
            raise
        finally:
            logging.info("Parsed plan: " + self.parsed_plan)

        return self.parsed_plan
        
