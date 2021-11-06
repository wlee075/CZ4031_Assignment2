"""
Parser for GroupAggregate node type
"""

import json
import algorithms.Annotation

def AggregateAlgorithm(plan, start=False):
    """ Parser for Aggregate node type """

    if plan["Strategy"] == "Sorted":
        parsed_plan = algorithms.Annotation.parse_plan(plan["Plans"][0], start)

        parsed_plan += " " + algorithms.Annotation.get_conjuction()

        if "Group Key" in plan:
            parsed_plan += "the result is grouped by "
            for group_key in plan["Group Key"]:
                parsed_plan += group_key.replace("::text", "") + ", "
            parsed_plan = parsed_plan[:-2]
        if "Filter" in plan:
            parsed_plan += " and bounded with the condition(s) " + plan["Filter"].replace("::text", "")
        parsed_plan += "."
        return parsed_plan

    if plan["Strategy"] == "Hashed":
        sentence = algorithms.Annotation.get_conjuction()

        if len(plan["Group Key"]) == 1:
            sentence += "it hashes all the rows based on the key "
            sentence += plan["Group Key"][0].replace("::text", "") + ", "
        else:
            sentence += "it hashes all the rows based on the keys "
            for i in plan["Group Key"]:
                sentence += i.replace("::text", "") + ", "
        sentence += "then returns the desired row after processing."

        parsed_plan = algorithms.Annotation.parse_plan(plan["Plans"][0], start)
        parsed_plan += " " + sentence
        return parsed_plan

    if plan["Strategy"] == "Plain":
        parsed_plan = algorithms.Annotation.parse_plan(plan["Plans"][0], start) + " "
        parsed_plan += algorithms.Annotation.get_conjuction()
        parsed_plan += "the result will be aggregated."
        return parsed_plan


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
    print(AggregateAlgorithm(JSON_PLAN, start=True))

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