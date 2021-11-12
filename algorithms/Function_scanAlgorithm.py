"""
File to parse node type function scan
"""

import json
import Annotation

def Function_scanAlgorithm(plan, start=False):
    """ Parser for Function Scan node type """
    parsed_plan = Annotation.get_conjuction(start)
    parsed_plan += "Executes function " + plan["Function Name"]
    parsed_plan += " and returns the recordset created."
    return parsed_plan


