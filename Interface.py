"""
Application for query interface (Windows Compatible)
"""
import json
import json
import logging
import psycopg2

from algorithms.Annotation import parse_plan
try:
    # python 2.x
    from Tkinter import *
except ImportError:
    # python 3.x
    from tkinter import *

class InterfaceApp(Tk):
    """ App class for Query Plan """
    def __init__(self, parent, host, port, dbname, user, password):
        self.explanator = Explain(
            host, port, dbname, user, password,
            desc=False, voice=False, debug=False
        )

        Tk.__init__(self, parent)
        self.parent = parent
        self.minsize(width=800, height=500)
        self.initialize(host, port, dbname, user, password)

    def initialize(self, host, port, dbname, user, password):
        """ GUI Initialization """
        self.label_host = Label(self, text="Host:", width=10, anchor="w")
        self.label_host.grid(column=0, row=0, columnspan=1, sticky='W')
        self.entry_var_host = StringVar()
        self.entry_host = Entry(self, textvariable=self.entry_var_host)
        self.entry_host.grid(column=1, row=0, columnspan=3, sticky='EW')
        self.entry_var_host.set(host)

        self.label_database = Label(self, text="Database:", width=10, anchor="w")
        self.label_database.grid(column=0, row=1, columnspan=1, sticky='W')
        self.entry_var_database = StringVar()
        self.entry_database = Entry(self, textvariable=self.entry_var_database)
        self.entry_database.grid(column=1, row=1, columnspan=3, sticky='EW')
        self.entry_var_database.set(dbname)

        self.label_port = Label(self, text="Port:", width=10, anchor="w")
        self.label_port.grid(column=0, row=2, columnspan=1, sticky='W')
        self.entry_var_port = StringVar()
        self.entry_port = Entry(self, textvariable=self.entry_var_port)
        self.entry_port.grid(column=1, row=2, columnspan=3, sticky='EW')
        self.entry_var_port.set(port)

        self.label_username = Label(self, text="Username:", width=10, anchor="w")
        self.label_username.grid(column=0, row=3, columnspan=1, sticky='W')
        self.entry_var_username = StringVar()
        self.entry_username = Entry(self, textvariable=self.entry_var_username)
        self.entry_username.grid(column=1, row=3, columnspan=3, sticky='EW')
        self.entry_var_username.set(user)

        self.label_password = Label(self, text="Password:", width=10, anchor="w")
        self.label_password.grid(column=0, row=4, columnspan=1, sticky='W')
        self.entry_var_password = StringVar()
        self.entry_password = Entry(self, show='*', textvariable=self.entry_var_password)
        self.entry_password.grid(column=1, row=4, columnspan=3, sticky='EW')
        self.entry_var_password.set(password)

        '''button to derive query plan'''
        self.label_query = Label(self, text="Query:", anchor="w")
        self.label_query.grid(column=0, row=5, columnspan=1, sticky='W')
        self.frame_query = Frame(self)
        self.frame_query.grid(column=1, row=6, columnspan=6, rowspan=1, sticky='W')
        self.button_query = Button(
            self.frame_query, text="Derive query plan",
            width=20, command=self.explain_query)
        self.button_query.pack(side=BOTTOM)
        self.entry_query = Text(self.frame_query, height=10, wrap=WORD)
        self.entry_query.pack(side='left', fill='both', expand=True)
        self.scrollbar_query = Scrollbar(self.frame_query)
        self.entry_query.config(yscrollcommand=self.scrollbar_query.set)
        self.scrollbar_query.config(command=self.entry_query.yview)
        self.grid()
        self.scrollbar_query.pack(side='right', fill='y')

        '''button to parse query plan, annotate'''
        self.label_plan = Label(self, text="Query Plan:", anchor="w")
        self.label_plan.grid(column=0, row=8, columnspan=1, sticky='W')
        self.frame_plan = Frame(self)
        self.frame_plan.grid(column=1, row=9, columnspan=6, rowspan=1, sticky='W')
        self.button_plan = Button(
            self.frame_plan, text="Parse",
            width=20, command=self.parse_plan)
        self.button_plan.pack(side=BOTTOM)
        self.entry_plan = Text(self.frame_plan, height=10, wrap=WORD)
        self.entry_plan.pack(side='left', fill='both', expand=True)
        self.scrollbar_plan = Scrollbar(self.frame_plan)
        self.entry_plan.config(yscrollcommand=self.scrollbar_plan.set)
        self.scrollbar_plan.config(command=self.entry_plan.yview)
        self.grid()
        self.scrollbar_plan.pack(side='right', fill='y')

        self.label_parsed_plan = Label(self, text="Parsed Query Plan:", anchor="w")
        self.label_parsed_plan.grid(column=0, row=10, columnspan=1, sticky='W')
        self.frame_parsed_plan = Frame(self)
        self.frame_parsed_plan.grid(column=1, row=11, columnspan=6, rowspan=1, sticky='W')
        #self.button_parsed_plan.pack(side=BOTTOM)
        self.entry_parsed_plan = Text(self.frame_parsed_plan, height=10, wrap=WORD)
        self.entry_parsed_plan.pack(side='left', fill='both', expand=True)
        self.scrollbar_parsed_plan = Scrollbar(self.frame_parsed_plan)
        self.entry_parsed_plan.config(yscrollcommand=self.scrollbar_parsed_plan.set)
        self.scrollbar_parsed_plan.config(command=self.entry_parsed_plan.yview)
        self.grid()
        self.scrollbar_parsed_plan.pack(side='right', fill='y')

    def explain_query(self):
        """ Explain query """
        self.explanator = Explain(
            host=self.entry_var_host.get(),
            port=self.entry_var_port.get(),
            dbname=self.entry_var_database.get(),
            user=self.entry_var_username.get(),
            password=self.entry_var_password.get(),
            desc=False, voice=False, debug=False
        )
        query = self.entry_query.get("1.0", END)
        query_plan = self.explanator.explain(query=query)
        self.entry_plan.delete("1.0", END)
        self.entry_plan.insert("1.0", json.dumps(query_plan, indent=4))

    def parse_plan(self):
        """ Parse query plan """
        query_plan = json.loads(self.entry_plan.get("1.0", END))
        parsed_plan = self.explanator.parse(query_plan)
        self.entry_parsed_plan.delete("1.0", END)
        self.entry_parsed_plan.insert("1.0", json.dumps(parsed_plan, indent=4))

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
