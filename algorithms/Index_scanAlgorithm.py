"""
Parser for index scan node type
"""

import json
import Annotation

def Index_scanAlgorithm(plan, start=False):
    """ Index Scan parser """
    result = Annotation.get_conjuction(start)

    #Parse the index scan or index only scan
    if plan["Node Type"] == "Index Scan":
        result += "Perform index scan with index table "+ plan["Index Name"]
        #result += "index scan is done by using an index table "+ plan["Index Name"]
        if "Index Cond" in plan:
            result += " based on the conditions "+ plan["Index Cond"].replace('::text', '')
            #result += " with the conditions "+ plan["Index Cond"].replace('::text', '')
        result += ". Once done, matched rows in " + plan["Relation Name"]
        #result += ". Next, it opens the " + plan["Relation Name"]
        result += " table are returned."
        #result += " table and fetches rows pointed by index matched in the scan."

        if "Filter" in plan:
            result += " Filter output by "+ plan["Filter"].replace('::text', '') +"."
            #result += " The result is then filtered by "+ plan["Filter"].replace('::text', '') +"."

    elif plan["Node Type"] == "Index Only Scan":
        result += "Perform index scan with index table "+ plan["Index Name"]
        #result += "It does an index scan by using an index table "+ plan["Index Name"]
        if "Index Cond" in plan:
            result += " with condition(s) "+ plan["Index Cond"].replace('::text', '')
        result += ". Return any matches found as the result."
        #esult += ". It returns the matches found in index table scan as the result."
        if "Filter" in plan:
            result += " Filter output by "+ plan["Filter"].replace('::text', '') +"."
            #result += " The result is then filtered by "+ plan["Filter"].replace('::text', '') +"."

    return result


