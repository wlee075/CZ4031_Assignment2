"""
File to parse node type hash
"""

import json
import query_plan_parser.annotation

def hash_parser(plan, start=False):
    """Parser for Hash node type"""

    if "Plans" in plan:
        sentence = query_plan_parser.annotation.parse_plan(plan['Plans'][0], start)
        sentence += " The hash function makes a memory hash with rows from the source."
    else:
        sentence = query_plan_parser.annotation.get_conjuction(start)
        sentence += "the hash function makes a memory hash with rows from the source."

    return sentence

if __name__ == "__main__":
    PLAN = '''
    {                                                    
        "Node Type": "Hash",                               
        "Parent Relationship": "Inner",                    
        "Parallel Aware": false,                           
        "Startup Cost": 16963.36,                          
        "Total Cost": 16963.36,                            
        "Plan Rows": 35630,                                
        "Plan Width": 22,                                  
        "Plans": [                                         
            {                                                
                "Node Type": "Seq Scan",                       
                "Parent Relationship": "Outer",                
                "Parallel Aware": false,                       
                "Relation Name": "publication",                
                "Alias": "b",                                  
                "Startup Cost": 0.00,                          
                "Total Cost": 16963.36,                        
                "Plan Rows": 35630,                            
                "Plan Width": 22,                              
                "Filter": "(year = 2017)"                      
            }                                                
        ]                                                  
    }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(hash_parser(JSON_PLAN, start=True))
