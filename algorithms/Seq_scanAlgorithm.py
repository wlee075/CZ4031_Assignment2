"""
File to parse node type seq scan
"""

import json
import Annotation

def Seq_scanAlgorithm(plan, start=False):
    """ Parser for the Seq Scan Node Type"""
    sentence = Annotation.get_conjuction(start)
    sentence += "it does a sequential scan on relation "
    if "Relation Name" in plan:
        sentence += plan['Relation Name']
    if "Alias" in plan:
        if plan['Relation Name'] != plan['Alias']:
            sentence += " with an alias of "
            sentence += plan['Alias']
    sentence += "."
    if "Filter" in plan:
        sentence += " This is bounded by the condition "
        sentence += plan['Filter'].replace("::text", "")
        sentence += "."

    return sentence

if __name__ == "__main__":
    PLAN = '''
    {                                
        "Node Type": "Seq Scan",       
        "Parent Relationship": "Outer",
        "Parallel Aware": false,       
        "Relation Name": "publication",
        "Alias": "publication",        
        "Startup Cost": 0.00,          
        "Total Cost": 15525.89,        
        "Plan Rows": 574989,           
        "Plan Width": 0                
    }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(seq_scanAlgorithm(JSON_PLAN, start=True))
