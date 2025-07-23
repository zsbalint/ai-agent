import os

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