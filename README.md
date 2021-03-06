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
- Select SQL from button selections. Alternatively, enter query in `Query` section and press `Explain` to generate query plan 
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

