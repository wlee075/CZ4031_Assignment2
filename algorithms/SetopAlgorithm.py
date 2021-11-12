"""
Parser for SetOp node type
"""

import json
import Annotation

def SetopAlgorithm(plan, start=False):
    """ SetOp Parser """
    result = Annotation.parse_plan(plan["Plans"][0], start)
    result += " " + Annotation.get_conjuction()
    result += "It finds the "
    cmd_name = str(plan["Command"])
    if cmd_name == "Except" or cmd_name == "Except All":
        result += "differences "
    else:
        result += "similarities "
    result += "between the two previously scanned tables using the "
    result += plan["Node Type"] + " operation."

    return result


