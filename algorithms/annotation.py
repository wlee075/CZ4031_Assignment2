"""
Main file to parse query plan
"""

import random

import algorithms.generic_parser as generic
import algorithms.hash_join_parser as hash_join
import algorithms.sort_parser as sort
import algorithms.aggregate_parser as aggregate
import algorithms.seq_scan_parser as seq_scan
import algorithms.hash_parser as hash_parser
import algorithms.merge_join_parser as merge_join
import algorithms.limit_parser as limit
import algorithms.unique_parser as unique
import algorithms.function_scan_parser as function_scan
import algorithms.index_scan_parser as index_scan
import algorithms.values_scan_parser as values_scan
import algorithms.nested_loop_parser as nested_loop
import algorithms.cte_scan_parser as cte_scan
import algorithms.append_parser as append
import algorithms.materialize_parser as materialize
import algorithms.subquery_scan_parser as subquery_scan
import algorithms.setop_parser as setop
import algorithms.group_parser as group

class ParserSelector:
    """ ParserSelectorClass """
    def __init__(self):
        """ Init Class """
        
        self.generic_parser = generic.generic_parser

        self.Hash_Join = hash_join.hash_join_parser
        self.Sort = sort.sort_parser
        self.Aggregate = aggregate.aggregate_parser
        self.Seq_Scan = seq_scan.seq_scan_parser
        self.Hash = hash_parser.hash_parser
        self.Merge_Join = merge_join.merge_join_parser
        self.Limit = limit.limit_parser
        self.Unique = unique.unique_parser
        self.Function_Scan = function_scan.function_scan_parser
        self.Index_Scan = index_scan.index_scan_parser
        self.Index_Only_Scan = index_scan.index_scan_parser
        self.Values_Scan = values_scan.values_scan_parser
        self.Nested_Loop = nested_loop.nested_loop_parser
        self.CTE_Scan = cte_scan.cte_scan_parser
        self.Append = append.append_parser
        self.Materialize = materialize.materialize_parser
        self.Subquery_Scan = subquery_scan.subquery_scan_parser
        self.SetOp = setop.setop_parser
        self.Group = group.group_parser

def parse_plan(plan, start=False):

    """ Parse json format of query plan """
    
    selector = ParserSelector()
    try:
        parser = getattr(selector, plan["Node Type"].replace(" ", "_"))
    except:
        parser = selector.generic_parser
    parsed_plan = init_plan(plan, start)
    parsed_plan += parser(plan, start)
    return parsed_plan

CONJUNCTION_LIST = ["Next, ", "Afterwards, ", "Thereafter, ", "Subsequently, ", "Then, "]

def get_conjuction(start=False):

    """ Get random conjuction """
    
    if start:
        return "Firstly, "
    return random.choice(CONJUNCTION_LIST)

def init_plan(plan, start=False):

    """ Check for InitPlan """
    
    result = ""

    if "Parent Relationship" in plan:
        if plan["Parent Relationship"] == "InitPlan":
            result = get_conjuction(start)
            result += "the " + plan["Node Type"]
            result += " node and its subsequent child node will be executed first"
            result += " since the result from this node needs to be calculated initially"
            result += " and it is only calculated once for the whole query. "
            result += "The plan is as follows: "

    return result
