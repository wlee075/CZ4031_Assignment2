"""
File to parse node type hash
"""

import json
import Annotation

def HashAlgorithm(plan, start=False):
    """Parser for Hash node type"""

    if "Plans" in plan:
        sentence = Annotation.parse_plan(plan['Plans'][0], start)
        sentence += " Create memory hash by hashing source rows."
    else:
        sentence = Annotation.get_conjuction(start)
        sentence += " Create memory hash by hashing source rows."

    return sentence

