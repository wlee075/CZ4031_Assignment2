"""
Parser for CTE scan node type
"""

import json
import query_plan_parser.annotation

def cte_scan_parser(plan, start=False):
    """ CTE Scan parser """
    result = query_plan_parser.annotation.get_conjuction(start)

    # Parse the values scan
    if plan["Node Type"] == "CTE Scan":
        result += "it does a CTE scan throughout the table "
        result += str(plan["CTE Name"]) + " which will be stored in the memory "
        if "Index Cond" in plan:
            result += " with condition(s) "+ plan["Index Cond"].replace('::text', '')
        result += "."

        if "Filter" in plan:
            result += " The results will be filtered by "+ plan["Filter"].replace('::text', '') +"."

    return result


if __name__ == "__main__":
    PLAN = '''
   {                                             
       "Node Type": "CTE Scan",                  
        "Parent Relationship": "Outer",           
        "Parallel Aware": false,                  
        "CTE Name": "x",                          
        "Alias": "x",                             
        "Startup Cost": 0.00,                     
        "Total Cost": 11651.98,                   
        "Plan Rows": 582599,                      
        "Plan Width": 218       
     }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(cte_scan_parser(JSON_PLAN, start=True))
