import ast

class CodeTools:

    def search_function(self, code, function_name):
        tree = ast.parse(code)

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if node.name == function_name:
                    return f"Function '{function_name}' found"

        return "Function not found"

    def analyze_code(self, code):
        try:
            ast.parse(code)
            return "Code syntax looks correct"
        except Exception as e:
            return str(e)