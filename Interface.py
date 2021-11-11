"""
Application for query interface (Windows Compatible)
"""
import json
import json
import logging
import psycopg2

from Annotation import parse_plan
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
        self.minsize(1900,900)
        self.maxsize(1900,900)
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
        
        self.label_query = Label(self, text="", anchor="w")
        self.label_query.grid(column=0, row=5, columnspan=1, sticky='W'
        )
        '''button to derive query plan'''
        # self.frame_query = Frame(self)
        # self.frame_query.grid(column=0, row=6,  sticky='W')
        self.label_query = Label(self, text="Query:", anchor="w")
        self.label_query.grid(column=0, row=6, columnspan=1, sticky='W')
        self.frame_query = Frame(self)
        self.frame_query.grid(column=1, row=6,  sticky='W')
        

        '''button for queries'''     
        self.button_set = Button(
            self.frame_query, text="q1",
            width=5,command=self.q1_plan)
        self.button_set.pack(side=LEFT)

        self.button_set = Button(
            self.frame_query, text="q3",
            width=5,command=self.q3_plan)
        self.button_set.pack(side=LEFT)
        
        self.button_set = Button(
            self.frame_query, text="q5",
            width=5,command=self.q5_plan)
        self.button_set.pack(side=LEFT)

        self.button_set = Button(
            self.frame_query, text="q6",
            width=5,command=self.q6_plan)
        self.button_set.pack(side=LEFT)

        self.button_set = Button(
            self.frame_query, text="q10",
            width=5,command=self.q10_plan)
        self.button_set.pack(side=LEFT)

        self.button_set = Button(
            self.frame_query, text="q12",
            width=5,command=self.q12_plan)
        self.button_set.pack(side=LEFT)

        self.button_set = Button(
            self.frame_query, text="q14",
            width=5,command=self.q14_plan)
        self.button_set.pack(side=LEFT)

        self.button_set = Button(
            self.frame_query, text="q19",
            width=5,command=self.q19_plan)
        self.button_set.pack(side=LEFT)

      
        self.frame_query = Frame(self)
        self.entry_query = Text(self.frame_query, height=10, wrap=WORD)
        self.frame_query.grid(column=1, row=8, columnspan=3, sticky='W')
        self.entry_query.pack(side=LEFT)
        #self.entry_query.pack(side='left', fill='both', expand=True)
        # self.scrollbar_query = Scrollbar(self.frame_query)
        # self.entry_query.config(yscrollcommand=self.scrollbar_query.set)
        # self.scrollbar_query.config(command=self.entry_query.yview)
        # self.entry_query.grid(column=1, row=8, columnspan=1, sticky='W')
        #self.scrollbar_query.pack(side='right', fill='y')

        self.frame_query = Frame(self)
        self.frame_query.grid(column=1, row=9, columnspan=3, sticky='W')
        self.button_query = Button(
            self.frame_query, text="Derive query plan",
            width=20, command=self.explain_query)
        self.button_query.pack(side=LEFT)

        '''button to parse query plan, annotate'''
        self.frame_query = Frame(self)
        self.frame_query.grid(column=0, row=10, columnspan=3, sticky='W')
        self.label_query = Label(self.frame_query, text="", anchor="w")
        self.label_query.pack(side=LEFT)
        self.frame_query = Frame(self)
        self.frame_query.grid(column=0, row=11, columnspan=3, sticky='nw')
        self.label_plan = Label(self.frame_query, text="Query Plan:", anchor="nw")
        self.label_plan.pack(side=LEFT)
        self.entry_plan = Text(self, height=10, wrap=WORD)
        self.entry_plan.grid(column=1, row=11, columnspan=3, sticky='W')
        self.button_plan = Button(
            self, text="Parse",
            width=20, command=self.parse_plan)
        self.button_plan.grid(column=1, row=12, columnspan=3, sticky='W')
        # self.label_plan.grid(column=0, row=8, columnspan=1, sticky='W')
        # self.frame_plan = Frame(self)
        # self.frame_plan.grid(column=1, row=9, columnspan=6, rowspan=1, sticky='W')
        
       
        # self.entry_plan.pack(side='left', fill='both', expand=True)
        # self.scrollbar_plan = Scrollbar(self.frame_plan)
        # self.entry_plan.config(yscrollcommand=self.scrollbar_plan.set)
        # self.scrollbar_plan.config(command=self.entry_plan.yview)
        # self.grid()
        # self.scrollbar_plan.pack(side='right', fill='y')

        self.label_query = Label(self, text="", anchor="nw")
        self.label_query.grid(column=0, row=13, columnspan=3, sticky='nw')
        self.frame_query = Frame(self)
        self.frame_query.grid(column=0, row=14, columnspan=3, sticky='nw')
        self.label_parsed_plan = Label(self.frame_query, text="Parsed Query Plan:", anchor="nw")
        self.label_parsed_plan.pack(side=LEFT)
        self.entry_parsed_plan = Text(self.frame_query, height=10, wrap=WORD)
        self.entry_parsed_plan.pack(side='left', fill='both', expand=True)
        # self.frame_parsed_plan = Frame(self)
        # self.frame_parsed_plan.grid(column=1, row=11, columnspan=6, rowspan=1, sticky='W')
        # #self.button_parsed_plan.pack(side=BOTTOM)
       
        # self.scrollbar_parsed_plan = Scrollbar(self.frame_parsed_plan)
        # self.entry_parsed_plan.config(yscrollcommand=self.scrollbar_parsed_plan.set)
        # self.scrollbar_parsed_plan.config(command=self.entry_parsed_plan.yview)
        # self.grid()
        # self.scrollbar_parsed_plan.pack(side='right', fill='y')


    def q1_plan(self):
        self.entry_query.delete("1.0", END)
        self.entry_query.insert("1.0","SELECT l_returnflag,l_linestatus,sum(l_quantity) as sum_qty,sum(l_extendedprice) as sum_base_price,sum(l_extendedprice * (1 - l_discount)) as sum_disc_price,sum(l_extendedprice * (1 - l_discount) * (1 + l_tax)) as sum_charge,avg(l_quantity) as avg_qty,avg(l_extendedprice) as avg_price,avg(l_discount) as avg_disc,count(*) as count_order FROM lineitem WHERE l_shipdate <= date '1998-12-01' - interval '90' day GROUP BY l_returnflag,l_linestatus ORDER BY l_returnflag,l_linestatus;")

    def q10_plan(self):
        self.entry_query.delete("1.0", END)
        self.entry_query.insert("1.0","SELECT c_custkey,c_name,sum(l_extendedprice * (1 - l_discount)) as revenue,c_acctbal,n_name,c_address,c_phone,c_comment FROM customer,orders,lineitem,nation WHERE c_custkey = o_custkey AND l_orderkey = o_orderkey AND o_orderdate >= date '1993-10-01' AND o_orderdate < date '1993-10-01' + interval '3' month AND l_returnflag = 'R' AND c_nationkey = n_nationkey GROUP BY c_custkey,c_name,c_acctbal,c_phone,n_name,c_address,c_comment ORDER BY revenue desc LIMIT 20;")

    def q12_plan(self):
        self.entry_query.delete("1.0", END)
        self.entry_query.insert("1.0","SELECT l_shipmode,sum(case when o_orderpriority = '1-URGENT' OR o_orderpriority = '2-HIGH' then 1 else 0 end) as high_line_count,sum(case when o_orderpriority <> '1-URGENT' AND o_orderpriority <> '2-HIGH' then 1 else 0 end) AS low_line_count FROM orders,lineitem WHERE o_orderkey = l_orderkey AND l_shipmode in ('MAIL', 'SHIP') AND l_commitdate < l_receiptdate AND l_shipdate < l_commitdate AND l_receiptdate >= date '1994-01-01' AND l_receiptdate < date '1994-01-01' + interval '1' year GROUP BY l_shipmode ORDER BY l_shipmode;")

    def q14_plan(self):
        self.entry_query.delete("1.0", END)
        self.entry_query.insert("1.0","SELECT 100.00 * sum(case when p_type like 'PROMO%' then l_extendedprice * (1 - l_discount) else 0 end) / sum(l_extendedprice * (1 - l_discount)) as promo_revenue FROM lineitem,part WHERE l_partkey = p_partkey AND l_shipdate >= date '1995-09-01' AND l_shipdate < date '1995-09-01' + interval '1' month;")

    def q19_plan(self):
        self.entry_query.delete("1.0", END)
        self.entry_query.insert("1.0","SELECT sum(l_extendedprice* (1 - l_discount)) as revenue FROM lineitem,part WHERE (p_partkey = l_partkey AND p_brand = 'Brand#12' AND p_container in ('SM CASE', 'SM BOX', 'SM PACK', 'SM PKG') AND l_quantity >= 1 AND l_quantity <= 1 + 10 AND p_size between 1 AND 5 AND l_shipmode in ('AIR', 'AIR REG') AND l_shipinstruct = 'DELIVER IN PERSON') OR (p_partkey = l_partkey AND p_brand = 'Brand#23' AND p_container in ('MED BAG', 'MED BOX', 'MED PKG', 'MED PACK') AND l_quantity >= 10 AND l_quantity <= 10 + 10 AND p_size between 1 AND 10 AND l_shipmode in ('AIR', 'AIR REG') AND l_shipinstruct = 'DELIVER IN PERSON') OR (p_partkey = l_partkey AND p_brand = 'Brand#34' AND p_container in ('LG CASE', 'LG BOX', 'LG PACK', 'LG PKG') AND l_quantity >= 20 AND l_quantity <= 20 + 10 AND p_size between 1 AND 15 AND l_shipmode in ('AIR', 'AIR REG') AND l_shipinstruct = 'DELIVER IN PERSON');")

    def q3_plan(self):
        self.entry_query.delete("1.0", END)
        self.entry_query.insert("1.0","SELECT l_orderkey,sum(l_extendedprice * (1 - l_discount)) as revenue,o_orderdate,o_shippriority FROM customer,orders,lineitem WHERE c_mktsegment = 'BUILDING' AND c_custkey = o_custkey AND l_orderkey = o_orderkey AND o_orderdate < date '1995-03-15' AND l_shipdate > date '1995-03-15' GROUP BY l_orderkey,o_orderdate,o_shippriority ORDER BY revenue desc,o_orderdate LIMIT 20;")

    def q5_plan(self):
        self.entry_query.delete("1.0", END)
        self.entry_query.insert("1.0","SELECT n_name,sum(l_extendedprice * (1 - l_discount)) as revenue FROM customer,orders,lineitem,supplier,nation,region WHERE c_custkey = o_custkey AND l_orderkey = o_orderkey AND l_suppkey = s_suppkey AND c_nationkey = s_nationkey AND s_nationkey = n_nationkey AND n_regionkey = r_regionkey AND r_name = 'ASIA' AND o_orderdate >= date '1994-01-01' AND o_orderdate < date '1994-01-01' + interval '1' year GROUP BY n_name ORDER BY revenue desc;")

    def q6_plan(self):
        self.entry_query.delete("1.0", END)
        self.entry_query.insert("1.0","SELECT sum(l_extendedprice * l_discount) as revenue FROM lineitem WHERE l_shipdate >= date '1994-01-01' AND l_shipdate < date '1994-01-01' + interval '1' year AND l_discount between 0.06 - 0.01 AND 0.06 + 0.01 AND l_quantity < 24;")

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
