"""
Parser for GroupAggregate node type
"""
import Annotation
import json
def AggregateAlgorithm(queryplan, isStart=False):
    """ Parser for Aggregate node type """

    if queryplan["Strategy"] == "Sorted":
        parsedplan = Annotation.parse_plan(queryplan["Plans"][0], isStart) + " "
        parsedplan += Annotation.get_conjuction()

        if "Group Key" in queryplan:
            parsedplan += "The result is grouped by "
            for group_key in queryplan["Group Key"]:
                parsedplan += group_key.replace("::text", "") + ", "
            parsedplan = parsedplan[:-2]
        if "Filter" in queryplan:
            parsedplan += " and bounded with the condition(s) " + queryplan["Filter"].replace("::text", "")
        parsedplan += "."
        return parsedplan

    if queryplan["Strategy"] == "Hashed":
        text = Annotation.get_conjuction()

        if len(queryplan["Group Key"]) == 1:
            text += "It hashes all the rows based on the key "
            text += queryplan["Group Key"][0].replace("::text", "") + ", "
        else:
            text += "It hashes all the rows based on the keys "
            for i in queryplan["Group Key"]:
                text += i.replace("::text", "") + ", "
        text += "then returns the desired row after processing."

        parsedplan = Annotation.parse_plan(queryplan["Plans"][0], isStart)
        parsedplan += " " + text
        return parsedplan

    if queryplan["Strategy"] == "Plain":
        parsedplan = Annotation.parse_plan(queryplan["Plans"][0], isStart) + " "
        parsedplan += Annotation.get_conjuction()
        parsedplan += "The result will be aggregated."
        return parsedplan

