"""
File to parse node type group
"""

import json
import query_plan_parser.annotation

def group_parser(plan, start=False):
    """Parser function for node type limit"""
    parsed_plan = query_plan_parser.annotation.parse_plan(plan["Plans"][0], start)
    parsed_plan += " " + query_plan_parser.annotation.get_conjuction()
    if len(plan["Group Key"]) == 1:
        parsed_plan += "the result from the previous operation is grouped together using the key "
        parsed_plan += plan["Group Key"][0].replace("::text", "") + "."
    else:
        parsed_plan += "result from the previous operation is grouped together using the key "
        for i in plan["Group Key"][:-1]:
            parsed_plan += i.replace("::text", "") + ", "
        parsed_plan += plan["Group Key"][-1].replace("::text", "") + "."

    return parsed_plan


if __name__ == "__main__":
    PLAN = '''
    {                                      
        "Node Type": "Group",                
        "Parent Relationship": "Outer",      
        "Parallel Aware": false,             
        "Startup Cost": 0.42,                
        "Total Cost": 60853.79,              
        "Plan Rows": 574989,                 
        "Plan Width": 106,                   
        "Group Key": ["pub_key", "year"],            
        "Plans": 
        [                           
            {                                  
                "Node Type": "Index Scan",       
                "Parent Relationship": "Outer",  
                "Parallel Aware": false,         
                "Scan Direction": "Forward",     
                "Index Name": "publication_pkey",
                "Relation Name": "publication",  
                "Alias": "publication",          
                "Startup Cost": 0.42,            
                "Total Cost": 59416.31,          
                "Plan Rows": 574989,             
                "Plan Width": 106                
            }                                  
        ]                                    
    }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(group_parser(JSON_PLAN, start=True))
