"""
Parser for values scan node type
"""

import json
import Annotation

def Values_scanAlgorithm(plan, start=False):
    """ Value Scan Parser """
    result = Annotation.get_conjuction(start)
    result += "It will perform a scan over the queried values."
    #result += "It does a scan through the given values from the query."

    return result


    
