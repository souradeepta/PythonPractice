"""create a comprehensive json parser"""

from typing import List, Mapping
import json
import pprint


def parseUsingLibrary(input) -> Mapping:
    """loads takes string and load takes a file path"""

    with open(input, 'r') as file:
        data = json.load(file)
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(data)

# TODO: Work on a lexer
def parseJson(input) -> Mapping:
    with open(input, 'r') as file:
        data = file.read()
        # print(type(data))
        pass
    
def parseDicttoJson(input: Mapping) -> 

if __name__ == "__main__":
    parseJson("sample.json")
