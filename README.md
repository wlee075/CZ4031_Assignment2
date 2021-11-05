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

#### Command Line Interface (CLI)

##### Input: Query

- Move to this directory
- Execute `python explain_cli.py`
- Enter query in CLI (end query with `;`)

##### Input: Query Plan (JSON formatted file)

- Move to this directory
- Execute `python explain_cli.py [path_to_query_plan_json_file]` (e.g. `python explain_cli.py data/q1.json`)

#### Graphical User Interface (GUI)

- Move to this directory
- Execute `python explain_app.py`
- Enter `host`, `database`, `port`, `username` and `password`
- To generate query plan: Enter query in `Query` section and press `Explain`
- To parse query plan: Enter query plan in `Query Plan` section or directly press `Parse`

### Test

#### Parser test

To test the each individual parser. Just move to `query_plan_parser/` and execute `python [parser_name].py`. It will run unit test in each parser.

## Source

### Query Executor

Connect to PostgreSQL and act as backend of the CLI and GUI. Use query plan parser to generate parsed plan string.

### Query Plan Parser

Receive query plan in JSON format. Parse the query plan recursively and return the parsed plan string.

## Content

### Handled Operation

The following operation is supported in this [parser](query_plan_parser/):

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

