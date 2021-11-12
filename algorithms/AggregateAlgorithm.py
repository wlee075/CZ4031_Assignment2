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
            parsedplan += "Group result by "
            for group_key in queryplan["Group Key"]:
                parsedplan += group_key.replace("::text", "") + ", "
            parsedplan = parsedplan[:-2]
        if "Filter" in queryplan:
            parsedplan += " and bind them with the following condition(s) " + queryplan["Filter"].replace("::text", "")
        parsedplan += "."
        return parsedplan

    if queryplan["Strategy"] == "Hashed":
        text = Annotation.get_conjuction()

        if len(queryplan["Group Key"]) == 1:
            text += "All rows hashed based on the keys "
            text += queryplan["Group Key"][0].replace("::text", "") + ", "
        else:
            text += "All rows hashed based on the keys "
            for i in queryplan["Group Key"]:
                text += i.replace("::text", "") + ", "
        text += " and after processing, the desired row is returned"

        parsedplan = Annotation.parse_plan(queryplan["Plans"][0], isStart)
        parsedplan += " " + text
        return parsedplan

    if queryplan["Strategy"] == "Plain":
        parsedplan = Annotation.parse_plan(queryplan["Plans"][0], isStart) + " "
        parsedplan += Annotation.get_conjuction()
        parsedplan += "Aggregate the result."
        return parsedplan

