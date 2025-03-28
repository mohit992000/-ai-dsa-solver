import random
import string
import re
import keyword
from typing import Dict

class SolutionGenerator:
    def __init__(self):
        """ Initializes a basic AI-powered solution generator. """
        self.template_solutions = {
            "array": "def solve_problem(arr):\n    return max(arr)\n",
            "linked list": (
                "class ListNode:\n"
                "    def __init__(self, val=0, next=None):\n"
                "        self.val = val\n"
                "        self.next = next\n\n"
                "def solve_problem(head):\n"
                "    return head.val if head else None\n"
            ),
            "binary search": (
                "def solve_problem(arr, target):\n"
                "    left, right = 0, len(arr) - 1\n"
                "    while left <= right:\n"
                "        mid = (left + right) // 2\n"
                "        if arr[mid] == target:\n"
                "            return mid\n"
                "        elif arr[mid] < target:\n"
                "            left = mid + 1\n"
                "        else:\n"
                "            right = mid - 1\n"
                "    return -1\n"
            )
        }

    def _randomize_names(self, code: str) -> str:
        """ Obfuscates only variable names, preserving Python keywords, built-ins, and function names. """
        
        # Reserved words we should never obfuscate
        python_builtins = {
            "max", "min", "sum", "len", "sorted", "range", "print",
            "map", "filter", "zip", "abs", "list", "set", "dict",
            "tuple", "enumerate", "any", "all", "round", "input"
        }
        
        protected_words = set(keyword.kwlist) | python_builtins | {"solve_problem", "self"}

        # Extract all valid identifiers
        words = re.findall(r"\b[a-zA-Z_][a-zA-Z0-9_]*\b", code)
        random.shuffle(words)

        replacements = {}
        for word in words:
            if word not in protected_words and word.isidentifier():
                if word not in replacements:
                    replacements[word] = ''.join(random.choices(string.ascii_letters, k=8))

        # Apply safe replacements using word boundaries
        for old, new in replacements.items():
            code = re.sub(r'\b' + re.escape(old) + r'\b', new, code)

        return code

    def generate_solution(self, problem_statement: str, parsed_data: Dict) -> str:
        """ Generates a solution based on detected data structures. """
        for ds in parsed_data['data_structures']:
            if ds in self.template_solutions:
                return self._randomize_names(self.template_solutions[ds])
        return "def solve_problem():\n    pass  # No specific solution found"

# Optional local test
if __name__ == "__main__":
    generator = SolutionGenerator()
    parsed_data = {"data_structures": ["array"], "problem_types": ["searching"], "constraints": ["O(n)"]}
    print("Generated Solution:\n", generator.generate_solution("Find the maximum element in an array.", parsed_data))




 
        
