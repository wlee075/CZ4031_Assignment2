"""
File to parse node type unique
"""

import json
import Annotation

def UniqueAlgorithm(plan, start=False):
    """Parser function for node type unique"""
    parsed_plan = Annotation.parse_plan(plan["Plans"][0], start) + " "
    parsed_plan += Annotation.get_conjuction()
    parsed_plan += "on the sorted data, it scans each row and "
    parsed_plan += "discards the rows with the same value as the previous row."
    return parsed_plan

if __name__ == "__main__":
    PLAN = '''
    {                                                                    
       "Node Type": "Unique",                                                     
       "Parallel Aware": false,                                                   
       "Startup Cost": 38090.22,                                                  
       "Total Cost": 38111.80,                                                    
       "Plan Rows": 200,                                                          
       "Plan Width": 15,
       "Plans": [
            {                                                                
                "Node Type": "Sort",                                           
                "Parent Relationship": "Outer",                                
                "Parallel Aware": false,                                       
                "Startup Cost": 19045.11,                                      
                "Total Cost": 19045.78,                                        
                "Plan Rows": 267,                                              
                "Plan Width": 15,                                              
                "Sort Key": ["a.author"]
            }
        ]
    }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(uniqueAlgorithm(JSON_PLAN, start=True))
    
