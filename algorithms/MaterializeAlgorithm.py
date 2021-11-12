"""
Parser for materialize node type
"""

import json
import Annotation

def MaterializeAlgorithm(plan, start=False):
    """ Materialize parser """
    result = ""

    # Get the text of it's child before if exists
    if "Plans" in plan:
        for child in plan["Plans"]:
            temp = Annotation.parse_plan(child, start)
            result += temp + " "
            if start:
                start = False

    #Parse the materialize
    if plan["Node Type"] == "Materialize":
        result += Annotation.get_conjuction(start)
        result += "Store the results in memory to eliminate latency and disk storage overhead. "
        #result += "The results will be stored in the memory for more efficient access. "

    return result

