import time
import traceback
from typing import Dict, List

class ExecutionEngine:
    def __init__(self):
        """ Initializes the execution engine. """
        self.execution_timeout = 5

    def execute_solution(self, solution_code: str, test_cases: List[Dict]) -> Dict:
        """ Runs the AI-generated solution and validates against test cases. """
        results = {}
        try:
            exec_locals = {}
            exec(solution_code, {}, exec_locals)  # Executes the generated code in an isolated environment
            solution_func = exec_locals[list(exec_locals.keys())[0]]  # Retrieves function reference

            for case in test_cases:
                input_data = case["input"]
                expected_output = case["output"]
                start_time = time.time()

                try:
                    result = solution_func(*input_data)  # Calls the generated function with test input
                    exec_time = time.time() - start_time
                    results[str(input_data)] = {
                        "result": result,
                        "expected": expected_output,
                        "correct": result == expected_output,
                        "execution_time": round(exec_time, 4)
                    }
                except Exception as e:
                    results[str(input_data)] = {"error": str(e), "correct": False}

        except Exception as e:
            results["error"] = traceback.format_exc()
        
        return results

# Example Usage
if __name__ == "__main__":
    engine = ExecutionEngine()
    generated_code = "def solve_problem(arr):\n    return max(arr)\n"
    test_cases = [{"input": [[1, 2, 3, 4, 5]], "output": 5}]
    print("Execution Results:", engine.execute_solution(generated_code, test_cases))
