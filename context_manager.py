import os

class ContextManager:

    def __init__(self, project_path):
        self.project_path = project_path

    def get_project_files(self):
        files = []
        for root, dirs, filenames in os.walk(self.project_path):
            for file in filenames:
                if file.endswith(".py"):
                    files.append(os.path.join(root, file))
        return files

    def read_file(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()