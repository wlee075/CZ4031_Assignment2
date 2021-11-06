"""
Parser for sort node type
"""

import json
import algorithms.Annotation

def sortAlgorithm(plan, start=False):
    """ Sort Parser """
    result = ""

    # Get the text of it's child before if exists
    if "Plans" in plan:
        for child in plan["Plans"]:
            temp = algorithms.Annotation.parse_plan(child, start)
            result += temp + " "
            if start:
                start = False

    # Parse the Sort
    if plan["Node Type"] == "Sort":
        result += algorithms.Annotation.get_conjuction(start)
        result += "the result is sorted by using attribute "
        if "DESC" in plan["Sort Key"]:
            result += str(plan["Sort Key"].replace('DESC', '')) +" in descending order."
        elif "INC" in plan["Sort Key"]:
            result += str(plan["Sort Key"].replace('INC', '')) +" in increasing order."
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
