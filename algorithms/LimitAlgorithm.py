"""
File to parse node type limit
"""

import json
import algorithms.Annotation

def LimitAlgorithm(plan, start=False):
    """Parser function for node type limit"""
    parsed_plan = algorithms.Annotation.parse_plan(plan["Plans"][0], start)
    parsed_plan += " Instead of scanning the whole table, it only does so with a limit of "
    total_rows = plan["Plan Rows"]
    parsed_plan += str(total_rows) + " entries."
    return parsed_plan


if __name__ == "__main__":
    PLAN = '''
    {                            
        "Node Type": "Limit",              
        "Parallel Aware": false,           
        "Startup Cost": 0.00,              
        "Total Cost": 0.27,                
        "Plan Rows": 10,                   
        "Plan Width": 106,                 
        "Plans": [
            {                                
                "Node Type": "Seq Scan",       
                "Parent Relationship": "Outer",
                "Parallel Aware": false,       
                "Relation Name": "publication",
                "Alias": "publication",        
                "Startup Cost": 0.00,          
                "Total Cost": 15525.89,        
                "Plan Rows": 574989,           
                "Plan Width": 106              
            }                                
        ]                                  
    }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(limitAlgorithm(JSON_PLAN, start=True))