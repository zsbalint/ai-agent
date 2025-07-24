import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    try:
        full_path = os.path.join(working_directory, file_path)
        abs_working_directory = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(full_path)

        if os.path.commonpath([abs_working_directory, abs_file_path]) != abs_working_directory:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found.'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        
        args_for_run = ["python", file_path]
        if args:
             for arg in args:
                  args_for_run.append(arg)
        
        run_result = subprocess.run(args_for_run, timeout=30, capture_output=True, cwd=abs_working_directory)

        output = ""
        if run_result.stdout.strip() == "" and run_result.stderr.strip() == "":
             return "No output produced."
        output += f"STDOUT: {run_result.stdout} \n STDERR: {run_result.stderr}"
        if run_result.returncode != 0:
             output += f"\n Process exited with code {run_result.returncode}"
        return output
    except Exception as e:
        return f"Error: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a python file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file": types.Schema(
                type=types.Type.STRING,
                description="The file to run, relative to the working directory. If not provided, returns an error.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="The arguments for the program which is going to be run. If empty, just call the file without arguments."
            )
        },
    ),
)