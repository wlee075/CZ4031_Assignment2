"""
File to parse node type seq scan
"""

import json
import Annotation

def Seq_scanAlgorithm(plan, start=False):
    """ Parser for the Seq Scan Node Type"""
    sentence = Annotation.get_conjuction(start)
    sentence += "Perform sequential scan on relation "
    if "Relation Name" in plan:
        sentence += plan['Relation Name']
    if "Alias" in plan:
        if plan['Relation Name'] != plan['Alias']:
            sentence += " whose alias is "
            sentence += plan['Alias']
    sentence += "."
    if "Filter" in plan:
        sentence += " The condition "
        sentence += plan['Filter'].replace("::text", "")
        sentence += " binds this operation"
        sentence += "."

    return sentence


