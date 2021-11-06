"""
Parser for values scan node type
"""

import json
import algorithms.Annotation

def Values_scanAlgorithm(plan, start=False):
    """ Value Scan Parser """
    result = algorithms.Annotation.get_conjuction(start)
    result += "it does a scan through the given values from the query."

    return result

if __name__ == "__main__":
    PLAN = '''
    {                                             
        "Node Type": "Values Scan",
        "Parallel Aware": false,   
        "Alias": "*VALUES*",       
        "Startup Cost": 0.00,      
        "Total Cost": 0.04,        
        "Plan Rows": 3,            
        "Plan Width": 36           
    }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(values_scanAlgorithm(JSON_PLAN, start=True))
    
