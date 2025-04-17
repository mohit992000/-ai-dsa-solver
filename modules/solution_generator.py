import random
import string
import re
import keyword
from typing import Dict

class SolutionGenerator:
    def __init__(self):
        """ Initializes a basic AI-powered solution generator with support for both data structures and problem types. """
        self.template_solutions = {
            #Structure-Based
            "array": (
                "def solve_problem(arr):\n"
                "    return max(arr)\n"
            ),

        "linked list": (
            "class ListNode:\n"
            "    def __init__(self, val=0, next=None):\n"
            "        self.val = val\n"
            "        self.next = next\n\n"
            "def solve_problem(head):\n"
            "    return head.val if head else None\n"
        ),

        "stack": (
            "def solve_problem(operations):\n"
            "    stack = []\n"
            "    for op in operations:\n"
            "        if op == 'pop':\n"
            "            stack.pop()\n"
            "        else:\n"
            "            stack.append(op)\n"
            "    return stack\n"
        ),

        "queue": (
            "from collections import deque\n"
            "def solve_problem(operations):\n"
            "    q = deque()\n"
            "    for op in operations:\n"
            "        if op == 'dequeue':\n"
            "            q.popleft()\n"
            "        else:\n"
            "            q.append(op)\n"
            "    return list(q)\n"
        ),

        #  Type-Based 
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
        ),

        "sorting": (
            "def solve_problem(arr):\n"
            "    return sorted(arr)\n"
        ),

        "recursion": (
            "def solve_problem(n):\n"
            "    if n == 0:\n"
            "        return 1\n"
            "    return n * solve_problem(n - 1)\n"
        ),

        "traversal": (
            "class TreeNode:\n"
            "    def __init__(self, val=0, left=None, right=None):\n"
            "        self.val = val\n"
            "        self.left = left\n"
            "        self.right = right\n\n"
            "def solve_problem(root):\n"
            "    result = []\n"
            "    def inorder(node):\n"
            "        if not node:\n"
            "            return\n"
            "        inorder(node.left)\n"
            "        result.append(node.val)\n"
            "        inorder(node.right)\n"
            "    inorder(root)\n"
            "    return result\n"
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
        """ Generates a solution based on detected problem types and data structures. Priority is given to problem types. """

        # 1. Try to match by problem type
        for ptype in parsed_data.get('problem_types', []):
            if ptype in self.template_solutions:
                print(f"📘 Using solution template for problem type: {ptype}")
                return self._randomize_names(self.template_solutions[ptype])

        # 2. If not found, match by data structure
        for ds in parsed_data.get('data_structures', []):
            if ds in self.template_solutions:
                print(f"📗 Using solution template for data structure: {ds}")
                return self._randomize_names(self.template_solutions[ds])

        # 3. Fallback message
        print("⚠️ No matching template found. Returning default function.")
        return "def solve_problem():\n    pass  # No specific solution found"

    def _randomize_names(self, code: str) -> str:
        """ Obfuscates variable names, preserving keywords and function names. """
        excluded = set(keyword.kwlist + dir(__builtins__) + ['solve_problem'])
        identifiers = set(re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', code))
        substitutions = {name: self._generate_random_name() for name in identifiers if name not in excluded}

        for orig, new in substitutions.items():
            code = re.sub(rf'\b{orig}\b', new, code)
        return code

    def _generate_random_name(self, length: int = 8) -> str:
        return ''.join(random.choices(string.ascii_letters, k=length))

# 🔍 Local test
if __name__ == "__main__":
    generator = SolutionGenerator()
    test_data = {
        "data_structures": ["tree"],
        "problem_types": ["traversal"]
    }
    print("Generated Solution:\n", generator.generate_solution("Traverse a binary tree in inorder.", test_data))


 
        
