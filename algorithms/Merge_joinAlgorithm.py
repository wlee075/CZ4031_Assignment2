"""
Merge Join parser
"""

import json
import Annotation

def Merge_joinAlgorithm(plan, start=False):
    """ Merge Join parser """
    result = ''

    if 'Plans' in plan:
        for child in plan['Plans']:
            result += Annotation.parse_plan(child, start) + " "
            if start:
                start = False

    result += Annotation.get_conjuction(start)
    result += 'Merge Join is performed on the output'
    #result += 'the result from previous operation is then joined using Merge Join'

    if 'Merge Cond' in plan:
        result += ' with condition ' + plan['Merge Cond'].replace("::text", "")

    if 'Join Type' == 'Semi':
        result += ' however only the left relation\'s row is returned'
        #result += ' but only the row from the left relation will be returned.'
    else:
        result += '.'

    return result


