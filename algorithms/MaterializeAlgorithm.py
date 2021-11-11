"""
Parser for materialize node type
"""

import json
import Annotation

def MaterializeAlgorithm(plan, start=False):
    """ Materialize parser """
    result = ""

    # Get the text of it's child before if exists
    if "Plans" in plan:
        for child in plan["Plans"]:
            temp = Annotation.parse_plan(child, start)
            result += temp + " "
            if start:
                start = False

    #Parse the materialize
    if plan["Node Type"] == "Materialize":
        result += Annotation.get_conjuction(start)
        result += "The results will be stored in the memory for more efficient access. "

    return result


if __name__ == "__main__":
    PLAN = '''
    {                                             
        "Node Type": "Materialize",                                        
        "Parent Relationship": "Inner",                                    
        "Parallel Aware": false,                                           
        "Startup Cost": 19215.45,                                          
        "Total Cost": 19223.67,                                            
        "Plan Rows": 274,                                                  
        "Plan Width": 15,                                                  
        "Plans": [                                                         
            {                                                                
                "Node Type": "Unrecognize",                                      
                "Strategy": "Sorted",                                          
                "Partial Mode": "Simple",                                      
                "Parent Relationship": "Outer",                                
                "Parallel Aware": false,                                       
                "Startup Cost": 19215.45,                                      
                "Total Cost": 19220.25,                                        
                "Plan Rows": 274,                                              
                "Plan Width": 23,                                              
                "Group Key": ["a_1.author"],                                   
                "Filter": "(count(a_1.author) >= 10)"                        
            }
        ]
    }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(materializeAlgorithm(JSON_PLAN, start=True))
