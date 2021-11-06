"""
Parser for values scan node type
"""

import json
import algorithms.annotation

def values_scan_parser(plan, start=False):
    """ Value Scan Parser """
    result = algorithms.annotation.get_conjuction(start)
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
    print(values_scan_parser(JSON_PLAN, start=True))
    
