import re
from typing import Dict

class ProblemParser:
    def __init__(self):
        """ Initializes the problem parser to detect problem patterns. """
        self.data_structures = [
            "array", "linked list", "graph", "tree", "stack", "queue", "heap", "hashmap"
        ]
        self.problem_types = [
            "sorting", "searching", "dynamic programming", "recursion", "bit manipulation"
        ]

    def parse(self, problem_statement: str) -> Dict:
        """ Parses the problem statement to extract key details. """
        problem_statement = problem_statement.lower()
        detected_structures = [ds for ds in self.data_structures if ds in problem_statement]
        detected_types = [pt for pt in self.problem_types if pt in problem_statement]
        constraints = re.findall(r"O\([^)]*\)|time complexity:.*|space complexity:.*", problem_statement)

        return {
            "data_structures": detected_structures or ["Unknown"],
            "problem_types": detected_types or ["Unclassified"],
            "constraints": constraints or ["Not Mentioned"]
        }

# Example Usage
if __name__ == "__main__":
    parser = ProblemParser()
    problem = "Find the largest element in an array in O(n) time complexity."
    print("Parsed Problem:", parser.parse(problem))
