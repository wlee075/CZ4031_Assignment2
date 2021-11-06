"""
Parser for append node type
"""

import json
import algorithms.Annotation

def AppendAlgorithm(plan, start=False):
    """ Append Parser """
    result = ""

    # Get the text of it's child before if exists
    if "Plans" in plan:
        for child in plan["Plans"]:
            temp = algorithms.Annotation.parse_plan(child, start)
            if start:
                start = False
            result += temp + " "

    #Parse the values scan
    if plan["Node Type"] == "Append":
        result += algorithms.Annotation.get_conjuction(start)
        result += "all of the scan results is combined into one."

    return result


if __name__ == "__main__":
    PLAN = '''
    {                             
       "Node Type": "Append",              
       "Parallel Aware": false,            
       "Startup Cost": 0.00,               
       "Total Cost": 40150.02,             
       "Plan Rows": 1902002,               
       "Plan Width": 22,                   
       "Plans": [                          
            {                                 
                "Node Type": "Seq Scan",        
                "Parent Relationship": "Member",
                "Parallel Aware": false,        
                "Relation Name": "publication", 
                "Alias": "publication",         
                "Startup Cost": 0.00,           
                "Total Cost": 15558.99,         
                "Plan Rows": 582599,            
                "Plan Width": 21                
            },                                
            {                                 
                "Node Type": "Seq Scan",        
                "Parent Relationship": "Member",
                "Parallel Aware": false,        
                "Relation Name": "pub_auth",    
                "Alias": "pub_auth",            
                "Startup Cost": 0.00,           
                "Total Cost": 24591.03,         
                "Plan Rows": 1319403,           
                "Plan Width": 23                
            }                                 
        ]                                   
    }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(appendAlgorithm(JSON_PLAN, start=True))