"""
File to parse node type unique
"""

import json
import Annotation

def UniqueAlgorithm(plan, start=False):
    """Parser function for node type unique"""
    parsed_plan = Annotation.parse_plan(plan["Plans"][0], start) + " "
    parsed_plan += Annotation.get_conjuction()
    parsed_plan += "it will scan each sorted data row and"
    parsed_plan += "discard rows with values mirroring the previous row"
    return parsed_plan


