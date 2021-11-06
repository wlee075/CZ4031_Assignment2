"""
Subquery scan parser
"""

import json
import algorithms.Annotation

def Subquery_scanAlgorithm(plan, start=False):
    """ Subquery scan parser """
    result = ''

    if 'Plans' in plan:
        for child in plan['Plans']:
            result += algorithms.Annotation.parse_plan(child, start) + " "
            if start:
                start = False

    result += algorithms.Annotation.get_conjuction(start)
    result += 'Subquery Scan is performed on the result from '
    result += 'the previous operations and output the result without any changes '
    result += '(the purpose of Subquery scan is mainly for internal bookkeeping).'

    return result

if __name__ == "__main__":
    PLAN = '''
    {                                                   
        "Node Type": "Subquery Scan",                                     
        "Parent Relationship": "Outer",                                   
        "Parallel Aware": false,                                          
        "Alias": "tmp_a",                                                 
        "Startup Cost": 48103.23,                                         
        "Total Cost": 48113.40,                                           
        "Plan Rows": 170,                                                 
        "Plan Width": 15,                                                 
        "Filter": "(NOT (hashed SubPlan 1))",
        "Plans":[
            {
                "Node Type": "Another Operation"
            }
        ]
    }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(subquery_scanAlgorithm(JSON_PLAN, start=True))
