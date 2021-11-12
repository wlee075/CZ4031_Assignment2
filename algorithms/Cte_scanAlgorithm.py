"""
Parser for CTE scan node type
"""

import json
import Annotation

def Cte_scanAlgorithm(plan, start=False):
    """ CTE Scan parser """
    result = Annotation.get_conjuction(start)

    # Parse the values scan
    if plan["Node Type"] == "CTE Scan":
        result += "Perform CTE scan "
        #result += "Perform CTE scan throughout the table "
        result += str(plan["CTE Name"]) + " which will be stored in the memory "
        if "Index Cond" in plan:
            result += " with condition(s) "+ plan["Index Cond"].replace('::text', '')
        result += "."

        if "Filter" in plan:
            result += " Filter output by "+ plan["Filter"].replace('::text', '') +"."       
            #result += " The results will be filtered by "+ plan["Filter"].replace('::text', '') +"."

    return result
