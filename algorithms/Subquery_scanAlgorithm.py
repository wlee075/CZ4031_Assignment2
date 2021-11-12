"""
Subquery scan parser
"""

import json
import Annotation

def Subquery_scanAlgorithm(plan, start=False):
    """ Subquery scan parser """
    result = ''

    if 'Plans' in plan:
        for child in plan['Plans']:
            result += Annotation.parse_plan(child, start) + " "
            if start:
                start = False

    result += Annotation.get_conjuction(start)
    result += 'Perform subquery scan on the output of '
    result += 'earlier operations without any changes to the result '
    """
    result += 'Subquery Scan is performed on the result from '
    result += 'the previous operations and output the result without any changes '
    result += '(the purpose of Subquery scan is mainly for internal bookkeeping).'
    """
    return result


