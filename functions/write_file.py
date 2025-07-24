import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:    
        full_path = os.path.join(working_directory, file_path)
        abs_working_directory = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(full_path)

        if os.path.commonpath([abs_working_directory, abs_file_path]) != abs_working_directory:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        with open(abs_file_path, "w") as f:
              f.write(content)
              return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
    
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write input to a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file": types.Schema(
                type=types.Type.STRING,
                description="The file to write to, relative to the working directory. If not provided, returns an error.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file specified."
            )
        },
    ),
)