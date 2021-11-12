# Annotate-Query

Project 2 CZ4031 Nanyang Technological University. Script to generate and parse query execution plan from a given query or query plan (in JSON format).

## Getting Started

### Requirements

- Python 3.6 or above (with pip)
- Postgresql 9.6.5 or above

### Usages

- Clone this repo
- Set `PYTHONPATH` to this directory
- Install library from [requirements.txt](requirements.txt) (`pip install -r requirements.txt`)
- Change [config.json](config.json) according to your setting.

**NOTES**: If you want to use queries from this repo make use to initialize the database using [init.sql](data/init.sql).

#### Graphical User Interface (GUI)

- Move to this directory
- Execute `python project.py`
- Amend `host`, `database`, `port`, `username` and `password` if system settings differ from .config file
- To generate query plan: Enter query in `Query` section and press `Explain`
- To parse query plan: Enter query plan in `Query Plan` section or directly press `Parse`

## Source

### Query Executor

Connect to PostgreSQL and act as backend of the GUI. Generate parsed plan strings via the query plan parser.

### Query Plan Parser

Receive query plan in JSON format. Parse the query plan recursively and return the parsed plan string.

## Content

### Handled Operation

The following operation is supported in this [parser](algorithms/):

- Scan
  - Function Scan
  - Seq Scan
  - Index Scan
  - Index Only Scan
  - Values Scan
  - CTE Scan
  - Subquery Scan
- Aggregate
  - Aggregate (plain)
  - Hash Aggregate
  - Group Aggregate
- Join
  - Hash Join
  - Nested Loop
  - Merge Join
- Other
  - Hash
  - Append
  - Result
  - SetOp
  - Group
  - Limit
  - Sort
  - Materialize
  - Unique
- Plan
  - SubPlan
  - InitPlan

### Example Query

The example query can be found [here](data/):
- [Query 1](data/q1.sql)
- [Query 3](data/q3.sql)
- [Query 5](data/q5.sql)
- [Query 6](data/q6.sql)
- [Query 10](data/q10.sql)
- [Query 12](data/q12.sql)
- [Query 14](data/q14.sql)
- [Query 19](data/q19.sql)

