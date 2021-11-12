"""
File to parse node type group
"""

import json
import Annotation

def GroupAlgorithm(plan, start=False):
    """Parser function for node type limit"""
    parsed_plan = Annotation.parse_plan(plan["Plans"][0], start)
    parsed_plan += " " + Annotation.get_conjuction()
    if len(plan["Group Key"]) == 1:
        parsed_plan += "Group the previous operation output with the key "
        #parsed_plan += "The result from the previous operation is grouped together using the key "
        parsed_plan += plan["Group Key"][0].replace("::text", "") + "."
    else:
        parsed_plan += "Group the previous operation output with the key "
        #parsed_plan += "result from the previous operation is grouped together using the key "
        for i in plan["Group Key"][:-1]:
            parsed_plan += i.replace("::text", "") + ", "
        parsed_plan += plan["Group Key"][-1].replace("::text", "") + "."

    return parsed_plan



