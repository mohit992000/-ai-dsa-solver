from modules.problem_parser import ProblemParser
from modules.solution_generator import SolutionGenerator
from modules.execution_engine import ExecutionEngine
from modules.security_module import SecurityModule

class DSASolver:
    def __init__(self):
        """ Initializes all modules for the AI-powered DSA Solver. """
        self.parser = ProblemParser()
        self.generator = SolutionGenerator()
        self.executor = ExecutionEngine()
        self.security = SecurityModule()

    def solve(self, problem: str, test_cases: list):
        """ Main function to process the problem and provide a validated solution. """
        
        # Step 1: Parse the problem statement
        parsed_data = self.parser.parse(problem)
        print("\n🔍 Parsed Data:", parsed_data)

        # Step 2: Generate a solution using AI
        generated_code = self.generator.generate_solution(problem, parsed_data)
        print("\n🤖 Generated Code:\n", generated_code)

        # Step 3: Encrypt & Decrypt the AI-generated solution
        encrypted_code = self.security.encrypt_code(generated_code)
        decrypted_code = self.security.decrypt_code(encrypted_code)
        print("\n🔐 Encrypted Code:", encrypted_code)
        print("\n🔓 Decrypted Code:\n", decrypted_code)

        # Step 4: Execute the solution and validate test cases
        results = self.executor.execute_solution(decrypted_code, test_cases)
        print("\n✅ Execution Results:", results)

        return results

# Example Usage
if __name__ == "__main__":
    solver = DSASolver()
    
    problem_statement = "Perform binary search on an array to find a target element."
    
    test_cases = [
        {"input": [[1, 2, 3, 4, 5], 3], "output": 2},
        {"input": [[1, 2, 3, 4, 5], 1], "output": 0},
        {"input": [[1, 2, 3, 4, 5], 5], "output": 4},
        {"input": [[1, 2, 3, 4, 5], 6], "output": -1}
    ]

    solver.solve(problem_statement, test_cases)
    

    # 👇 Force binary search for this test
    parsed_data = {
        "data_structures": ["binary search"],
        "problem_types": ["search"],
        "constraints": ["O(log n)"]
    }

    # Use generator directly to test (skip auto-parser temporarily)
    from modules.solution_generator import SolutionGenerator
    from modules.execution_engine import ExecutionEngine
    from modules.security_module import SecurityModule

    generator = SolutionGenerator()
    executor = ExecutionEngine()
    security = SecurityModule()

    code = generator.generate_solution(problem_statement, parsed_data)
    encrypted = security.encrypt_code(code)
    decrypted = security.decrypt_code(encrypted)

    print("\n🤖 Generated Code:\n", code)
    print("\n🔐 Encrypted Code:", encrypted)
    print("\n🔓 Decrypted Code:\n", decrypted)

    results = executor.execute_solution(decrypted, test_cases)
    print("\n✅ Execution Results:", results)
