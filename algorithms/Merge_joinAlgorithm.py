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
    result += 'the result from previous operation is then joined using Merge Join'

    if 'Merge Cond' in plan:
        result += ' with condition ' + plan['Merge Cond'].replace("::text", "")

    if 'Join Type' == 'Semi':
        result += ' but only the row from the left relation will be returned.'
    else:
        result += '.'

    return result


if __name__ == "__main__":
    PLAN = '''
    {                                                   
        "Node Type": "Merge Join",                                             
        "Parent Relationship": "Outer",                                        
        "Parallel Aware": false,                                               
        "Join Type": "Inner",                                                  
        "Startup Cost": 48100.69,                                              
        "Total Cost": 48128.80,                                                
        "Plan Rows": 575,                                                      
        "Plan Width": 15,                                                      
        "Merge Cond": "((a.author)::text = (a_1.author)::text)",
        "Plans" :[
            {
                "Node Type": "Unrecognize"
            }
        ]
    }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(merge_joinAlgorithm(JSON_PLAN, start=True))
