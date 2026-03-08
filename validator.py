import ast

class Validator:

    def syntax_check(self, code):

        try:
            ast.parse(code)
            return True, "Syntax OK"

        except Exception as e:
            return False, str(e)

    def security_check(self, code):

        risky_patterns = ["eval(", "exec("]

        for pattern in risky_patterns:
            if pattern in code:
                return False, "Potential security risk detected"

        return True, "Security check passed"