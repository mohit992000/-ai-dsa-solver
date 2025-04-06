import re
from typing import Dict

class ProblemParser:
    def __init__(self):
        self.known_structures = {
            "array": ["array", "list of integers", "sequence"],
            "linked list": ["linked list", "nodes linked"],
            "stack": ["stack", "last in first out", "push", "pop"],
            "queue": ["queue", "first in first out", "enqueue", "dequeue"],
            "tree": ["tree", "binary tree", "nodes in tree", "root", "leaf", "subtree"],
            "graph": ["graph", "edges", "vertices", "adjacency", "connected"],
            "matrix": ["matrix", "2d array", "grid", "row", "column"],
            "heap": ["heap", "priority queue", "min-heap", "max-heap"],
            "hashmap": ["hashmap", "dictionary", "map", "key-value", "lookup"]
        }

        self.known_problem_types = {
            "binary search": ["binary search", "logarithmic time search"],
            "sorting": ["sort", "sorted", "arranged in order"],
            "traversal": ["traverse", "inorder", "preorder", "postorder", "level order", "dfs", "bfs"],
            "recursion": ["recursive", "recursively", "base case", "call itself"],
            "dynamic programming": ["dp", "memoization", "overlapping subproblems", "bottom-up", "top-down"],
        }

    def parse(self, problem: str) -> Dict:
        problem = problem.lower()
        detected_structures = []
        detected_types = []

        for key, phrases in self.known_structures.items():
            if any(p in problem for p in phrases):
                detected_structures.append(key)

        for key, phrases in self.known_problem_types.items():
            if any(p in problem for p in phrases):
                detected_types.append(key)

        return {
            "data_structures": detected_structures or ["Unclassified"],
            "problem_types": detected_types or ["Unclassified"],
            "constraints": ["Not Mentioned"]  # We can enhance this later
        }

# Example Usage
if __name__ == "__main__":
    parser = ProblemParser()
    problem = "Find the largest element in an array in O(n) time complexity."
    print("Parsed Problem:", parser.parse(problem))
