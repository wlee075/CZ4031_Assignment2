"""
File for Hash Join 
"""

import json
import Annotation

def Hash_joinAlgorithm(plan, start=False):
    """ Hash join parser """
    result = ""

    result += Annotation.parse_plan(plan["Plans"][1], start) + " "
    result += Annotation.parse_plan(plan["Plans"][0]) + " "

    result += "Hash join the result from the earlier operation "
    #result += "The result from previous operation is joined using Hash "
    result += plan["Join Type"] + " Join"
    if 'Hash Cond' in plan:
        result += ' with the condition ' + plan['Hash Cond'].replace("::text", "") + '.'
    else:
        result += '.'

    return result


