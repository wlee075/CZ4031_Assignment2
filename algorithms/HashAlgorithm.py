"""
File to parse node type hash
"""

import json
import algorithms.Annotation

def HashAlgorithm(plan, start=False):
    """Parser for Hash node type"""

    if "Plans" in plan:
        sentence = algorithms.Annotation.parse_plan(plan['Plans'][0], start)
        sentence += " The hash function makes a memory hash with rows from the source."
    else:
        sentence = algorithms.Annotation.get_conjuction(start)
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
    print(hashAlgorithm(JSON_PLAN, start=True))
