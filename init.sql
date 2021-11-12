CREATE TABLE region(
    r_regionkey integer NOT NULL,
	r_name character(25) COLLATE pg_catalog."default" NOT NULL,
	r_comment character varying(152) COLLATE pg_catalog."default",
	CONSTRAINT region_pkey PRIMARY KEY (r_regionkey)
)
WITH(
	OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.region 
	OWNER to postgres;

CREATE TABLE public.nation(
    n_nationkey integer NOT NULL,
	n_name character(25) COLLATE pg_catalog."default" NOT NULL,
	n_regionkey integer NOT NULL,
	n_comment character varying(152) COLLATE pg_catalog."default",
	CONSTRAINT nation_pkey PRIMARY KEY (n_nationkey),
	CONSTRAINT nfk_nation FOREIGN KEY (n_regionkey)
		REFERENCES public.region (r_regionkey) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)
WITH (
	OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.nation 
	OWNER to postgres;

CREATE TABLE part(
    p_partkey integer NOT NULL,
	p_name character varying(55) COLLATE pg_catalog."default" NOT NULL,
	p_mfgr character(25) COLLATE pg_catalog."default" NOT NULL,
	p_brand character(10) COLLATE pg_catalog."default" NOT NULL,
	p_type character varying(25) COLLATE pg_catalog."default" NOT NULL,
	p_size integer NOT NULL,
	p_container character(10) COLLATE pg_catalog."default" NOT NULL,
	p_retailprice numeric(15,2) NOT NULL,
	p_comment character varying(23) COLLATE pg_catalog."default" NOT NULL,
	CONSTRAINT part_pkey PRIMARY KEY (p_partkey)
)
WITH (
	OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.part 
	OWNER to postgres;

CREATE TABLE public.supplier(
    s_suppkey integer NOT NULL,
	s_name character(25) COLLATE pg_catalog."default" NOT NULL,
	s_address character varying(40) COLLATE pg_catalog."default" NOT NULL,
	s_nationkey integer NOT NULL,
	s_phone character(15) COLLATE pg_catalog."default" NOT NULL,
	s_acctbal numeric(15,2) NOT NULL,
	s_comment character varying(101) COLLATE pg_catalog."default" NOT NULL,
	CONSTRAINT supplier_pkey PRIMARY KEY (s_suppkey),
	CONSTRAINT fk_supplier FOREIGN KEY (s_nationkey)
		REFERENCES public.nation (n_nationkey) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
	
)
WITH (
	OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.supplier 
	OWNER to postgres;

CREATE TABLE partsupp(
    ps_partkey integer NOT NULL,
	ps_suppkey integer NOT NULL,
	ps_availqty integer NOT NULL,
	ps_supplycost numeric(15,2) NOT NULL,
	ps_comment character varying(199) COLLATE pg_catalog."default" NOT NULL,
	CONSTRAINT partsupp_pkey PRIMARY KEY (ps_partkey,ps_suppkey),
	CONSTRAINT fk_ps_suppkey_partkey FOREIGN KEY (ps_partkey)
		REFERENCES public.part (p_partkey) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,	
	CONSTRAINT fk_ps_suppkey_suppkey FOREIGN KEY (ps_suppkey)
		REFERENCES public.supplier (s_suppkey) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION	
)
WITH (
	OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.partsupp
	OWNER to postgres;

CREATE TABLE customer(
   c_custkey integer NOT NULL,
   c_name character varying(25) COLLATE pg_catalog."default" NOT NULL,
   c_address character varying(40) COLLATE pg_catalog."default" NOT NULL,
   c_nationkey integer NOT NULL,
   c_phone character(15) COLLATE pg_catalog."default" NOT NULL,
   c_acctbal numeric(15,2) NOT NULL,
   c_mktsegment character(10) COLLATE pg_catalog."default" NOT NULL,
   c_comment character varying(117) COLLATE pg_catalog."default" NOT NULL,
   CONSTRAINT customer_pkey PRIMARY KEY (c_custkey),
   CONSTRAINT fk_customer FOREIGN KEY (c_nationkey)
		REFERENCES public.nation (n_nationkey) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)
WITH (
	OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.customer
	OWNER to postgres;

CREATE TABLE orders(
   o_orderkey integer NOT NULL,
   o_custkey integer NOT NULL,
   o_orderstatus character(1) COLLATE pg_catalog."default" NOT NULL,
   o_totalprice numeric(15,2) NOT NULL,
   o_orderdate date NOT NULL,
   o_orderpriority character(15) COLLATE pg_catalog."default" NOT NULL,
   o_clerk character(15) COLLATE pg_catalog."default" NOT NULL,
   o_shippriority integer NOT NULL,
   o_comment character varying(79) COLLATE pg_catalog."default" NOT NULL,
   CONSTRAINT orders_pkey PRIMARY KEY (o_orderkey),
   CONSTRAINT fk_orders FOREIGN KEY (o_custkey)
		REFERENCES public.customer (c_custkey) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)
WITH (
	OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.orders
	OWNER to postgres;

CREATE TABLE lineitem(
   l_orderkey integer NOT NULL,
   l_partkey integer NOT NULL,
   l_suppkey integer NOT NULL,
   l_linenumber integer NOT NULL,
   l_quantity numeric(15,2) NOT NULL,
   l_extendedprice numeric(15,2) NOT NULL,
   l_discount numeric(15,2) NOT NULL,
   l_tax numeric(15,2) NOT NULL,
   l_returnflag character(1) COLLATE pg_catalog."default" NOT NULL,
   l_linestatus character(1) COLLATE pg_catalog."default" NOT NULL,
   l_shipdate date NOT NULL,
   l_commitdate date NOT NULL,
   l_receiptdate date NOT NULL,
   l_shipinstruct character(25) COLLATE pg_catalog."default" NOT NULL,
   l_shipmode character(10) COLLATE pg_catalog."default" NOT NULL,
   l_comment character varying(44) COLLATE pg_catalog."default" NOT NULL,
   CONSTRAINT lineitem_pkey PRIMARY KEY (l_orderkey, l_partkey, l_suppkey, l_linenumber),
   CONSTRAINT fk_lineitem_orderkey FOREIGN KEY (l_orderkey)
		REFERENCES public.orders (o_orderkey) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
   CONSTRAINT fk_lineitem_partkey FOREIGN KEY (l_partkey)
		REFERENCES public.part (p_partkey) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
   CONSTRAINT fk_lineitem_suppkey FOREIGN KEY (l_suppkey)
		REFERENCES public.supplier (s_suppkey) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)
WITH (
	OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.lineitem
	OWNER to postgres;

COPY region(r_regionkey, r_name, r_comment)
FROM 'C:\Users\wyman\OneDrive\Desktop\CZ4031_Assignment2\data\region.csv'
DELIMITER ','
CSV HEADER;

COPY nation(n_nationkey, n_name, n_regionkey, n_comment)
FROM 'C:\Users\wyman\OneDrive\Desktop\CZ4031_Assignment2\data\nation.csv'
DELIMITER ','
CSV HEADER;

COPY part(p_partkey, p_name, p_mfgr, p_brand, p_type, p_size, p_container, p_retailprice, p_comment)
FROM 'C:\Users\wyman\OneDrive\Desktop\CZ4031_Assignment2\data\part.csv'
DELIMITER ','
CSV HEADER;

COPY supplier(s_suppkey, s_name, s_address, s_nationkey, s_phone, s_acctbal, s_comment)
FROM 'C:\Users\wyman\OneDrive\Desktop\CZ4031_Assignment2\data\supplier.csv'
DELIMITER ','
CSV HEADER;

COPY partsupp(ps_partkey, ps_suppkey, ps_availqty, ps_supplycost, ps_comment)
FROM 'C:\Users\wyman\OneDrive\Desktop\CZ4031_Assignment2\data\partsupp.csv'
DELIMITER ','
CSV HEADER;

COPY customer(c_custkey, c_name, c_address, c_nationkey, c_phone, c_acctbal, c_mktsegment, c_comment)
FROM 'C:\Users\wyman\OneDrive\Desktop\CZ4031_Assignment2\data\customer.csv'
DELIMITER ','
CSV HEADER;

COPY orders(o_orderkey, o_custkey, o_orderstatus, o_totalprice, o_orderdate, o_orderpriority, o_clerk, o_shippriority, o_comment)
FROM 'C:\Users\wyman\OneDrive\Desktop\CZ4031_Assignment2\data\orders.csv'
DELIMITER ','
CSV HEADER;

COPY lineitem(l_orderkey,l_partkey,l_suppkey,l_linenumber,l_quantity,l_extendedprice,l_discount,l_tax,l_returnflag,l_linestatus,l_shipdate,l_commitdate,l_receiptdate,l_shipinstruct,l_shipmode,l_comment)
FROM 'C:\Users\wyman\OneDrive\Desktop\CZ4031_Assignment2\data\lineitem.csv'
DELIMITER ','
CSV HEADER;