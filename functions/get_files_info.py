import os

def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.join(working_directory, directory)
        abs_working_directory = os.path.abspath(working_directory)
        abs_target_path = os.path.abspath(full_path)

        dirname = ""
        if directory == ".":
            dirname = "current"
        else:
            dirname = f"'{directory}'"
        content_list = []
        content_list.append(f"Result for {dirname} directory:")

        if os.path.commonpath([abs_working_directory, abs_target_path]) != abs_working_directory:
            content_list.append(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
            result_text = "\n".join(content_list)
            return result_text
        if not os.path.isdir(full_path):
            content_list.append(f'Error: "{directory}" is not a directory')
            result_text = "\n".join(content_list)
            return result_text

        directory_content = os.listdir(full_path)

        for item in directory_content:
            item_path = str(abs_target_path) + os.sep + str(item)
            item_name = item
            item_size = os.path.getsize(item_path)
            item_isdir = os.path.isdir(item_path)
            content_list.append(f"- {item_name}: file_size={item_size}, is_dir={item_isdir}")
        result_text = "\n".join(content_list)
        return result_text
    except Exception as e:
        return f"Error: {e}"