"""
Parser for nested loop node type
"""

import json
import Annotation

def Nested_loopAlgorithm(plan, start=False):
    """ Nested Loop Parser """
    result = ""

    # Get the text of its child
    temp = Annotation.parse_plan(plan["Plans"][0], start)
    result += temp + " "
    temp = Annotation.parse_plan(plan["Plans"][1])
    result += temp + " "


    # Parse the nested loop
    result += "Next, return the join between both scans as new rows"
    #result += "Afterwards, the join result between both scan results are returned as new rows."

    return result



