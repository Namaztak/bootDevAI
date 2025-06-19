import os

def get_file_content(working_directory, file_name):
    full_path_cwd = os.path.abspath(working_directory)

    if not os.path.abspath(os.path.join(full_path_cwd, file_name)).startswith(full_path_cwd):
        print(f'Error: Cannot read "{file_name}" as it is outside the permitted working directory')
        return
    if not os.path.isfile(os.path.join(working_directory, file_name)):
        print(f'Error: File not found or is not a regular file: "{file_name}"')
        return
    with open(os.path.join(working_directory, file_name), 'r') as file:
        contents = file.read()
        if len(contents) > 10000:
            contents = contents[:10000] + f'[...File "{file_name}" truncated at 10000 characters]'
        return contents