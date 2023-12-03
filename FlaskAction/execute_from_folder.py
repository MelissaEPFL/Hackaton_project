import importlib.util
import os

def execute_function_from_module(path, function_name):
    if os.path.isfile(path):
        spec = importlib.util.spec_from_file_location("module.name", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        function = getattr(module, function_name)
        return function()
    else:
        print("File does not exist")
        return None

if __name__ == "__main__":
    # Usage
    print(execute_function_from_module("./button/3/update.py", "main_update"))