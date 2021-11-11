"""
Parser for sort node type
"""

import json
import Annotation

def SortAlgorithm(plan, start=False):
    """ Sort Parser """
    result = ""

    # Get the text of it's child before if exists
    if "Plans" in plan:
        for child in plan["Plans"]:
            temp = Annotation.parse_plan(child, start)
            result += temp + " "
            if start:
                start = False

    # Parse the Sort
    if plan["Node Type"] == "Sort":
        result += Annotation.get_conjuction(start)
        result += "The result is sorted by using attribute "
        if "DESC" in str(plan["Sort Key"]):
            result += str(plan["Sort Key"]).replace('DESC', '')+" in descending order."

        else:
            result += str(plan["Sort Key"])+ "."

    return result


if __name__ == "__main__":
    PLAN = '''
    {                                             
        "Node Type": "Sort",               
        "Parent Relationship": "Outer",    
        "Parallel Aware": false,           
        "Startup Cost": 31061.74,          
        "Total Cost": 32518.24,            
        "Plan Rows": 582599,               
        "Plan Width": 100,                 
        "Sort Key": ["title"],             
        "Plans": [                         
            {                                
                "Node Type": "Seq Scan",       
                "Parent Relationship": "Outer",
                "Parallel Aware": false,       
                "Relation Name": "publication",
                "Alias": "publication",        
                "Startup Cost": 0.00,          
                "Total Cost": 15558.99,        
                "Plan Rows": 582599,           
                "Plan Width": 100              
            }                                
        ]           
    }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(sortAlgorithm(JSON_PLAN, start=True))
