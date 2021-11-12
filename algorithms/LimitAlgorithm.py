"""
File to parse node type limit
"""

import json
import Annotation

def LimitAlgorithm(plan, start=False):
    """Parser function for node type limit"""
    parsed_plan = Annotation.parse_plan(plan["Plans"][0], start)
    parsed_plan += " Scan scope is limited to "
    #parsed_plan += " Instead of scanning the whole table, it only does so with a limit of "
    total_rows = plan["Plan Rows"]
    parsed_plan += str(total_rows) + " entries."
    return parsed_plan

