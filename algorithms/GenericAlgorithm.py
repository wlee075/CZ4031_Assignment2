"""
Generic Parser
"""

import json
import Annotation

def GenericAlgorithm(plan, start=False):
    """ Parse unknown node_type """
    parsed_plan = Annotation.get_conjuction(start)
    parsed_plan += "Perform " + plan["Node Type"] + "."
    if "Plans" in plan:
        for child in plan["Plans"]:
            parsed_plan += " " + Annotation.parse_plan(child)
    return parsed_plan


