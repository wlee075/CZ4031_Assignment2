"""
Parser for append node type
"""

import json
import Annotation

def AppendAlgorithm(plan, start=False):
    """ Append Parser """
    result = ""

    # Get the text of it's child before if exists
    if "Plans" in plan:
        for child in plan["Plans"]:
            temp = Annotation.parse_plan(child, start)
            if start:
                start = False
            result += temp + " "

    #Parse the values scan
    if plan["Node Type"] == "Append":
        result += Annotation.get_conjuction(start)
        result += "combine the scan results."

    return result


