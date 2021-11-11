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


if __name__ == "__main__":
    PLAN = '''
    {                                                        
       "Node Type": "Aggregate",                                      
       "Strategy": "Sorted",                                          
       "Partial Mode": "Simple",  
       "Parent Relationship": "InitPlan",                                    
       "Parallel Aware": false,                                       
       "Startup Cost": 513461.61,                                     
       "Total Cost": 519210.47,                                       
       "Plan Rows": 220200,                                           
       "Plan Width": 15,                                              
       "Group Key": ["a.author", "something else"],                                     
       "Filter": "(count(a.author) > 20)",
       "Plans": [                                         
            {                                                
            "Node Type": "Seq Scan",                       
            "Parent Relationship": "Outer",                
            "Parallel Aware": false,                       
            "Relation Name": "publication",                
            "Alias": "a",                                  
            "Startup Cost": 0.00,                          
            "Total Cost": 102857.50,                       
            "Plan Rows": 164431,                           
            "Plan Width": 23,                              
            "Filter": "(year = 2017)"                      
            }                                                
        ]
    }
    '''
    JSON_PLAN = json.loads(PLAN)
    print(AggregateAlgorithm(JSON_PLAN, isStart=True))

    PLAN2 = '''
    {                                                   
        "Node Type": "Aggregate",                                 
        "Strategy": "Hashed",                                     
        "Partial Mode": "Simple",                                 
        "Parallel Aware": false,                                  
        "Startup Cost": 40297.34,                                 
        "Total Cost": 40494.72,                                   
        "Plan Rows": 19738,                                       
        "Plan Width": 23,                                       
        "Group Key": ["b.author"],                              
        "Plans": [                                                
            {                                                       
                "Node Type": "Unrecognize",                           
                "Parent Relationship": "Outer",                       
                "Parallel Aware": false,                              
                "Join Type": "Inner",                                 
                "Startup Cost": 16963.82,                             
                "Total Cost": 40198.65,                               
                "Plan Rows": 19738,                                   
                "Plan Width": 15
            }
        ]
    }
    '''
    JSON_PLAN2 = json.loads(PLAN2)
    print(AggregateAlgorithm(JSON_PLAN2))
