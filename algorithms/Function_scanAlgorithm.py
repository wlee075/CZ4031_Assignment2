"""
File to parse node type function scan
"""

import json
import algorithms.Annotation

def Function_scanAlgorithm(plan, start=False):
    """ Parser for Function Scan node type """
    parsed_plan = algorithms.Annotation.get_conjuction(start)
    parsed_plan += "it runs the function " + plan["Function Name"]
    parsed_plan += " and returns the recordset created."
    return parsed_plan


if __name__ == "__main__":
    PLAN = '''
    {                                    
        "Node Type": "Function Scan",      
        "Parent Relationship": "Outer",    
        "Parallel Aware": false,           
        "Function Name": "generate_series",
        "Alias": "i",                      
        "Startup Cost": 0.00,              
        "Total Cost": 12.50,               
        "Plan Rows": 1000,                 
        "Plan Width": 8                    
    }                                                                         
    '''
    JSON_PLAN = json.loads(PLAN)
    print(function_scanAlgorithm(JSON_PLAN, start=True))
