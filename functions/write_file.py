import os

def write_file(working_directory, file_name, content):
    full_path_cwd = os.path.abspath(working_directory)

    if not os.path.abspath(os.path.join(full_path_cwd, file_name)).startswith(full_path_cwd):
        print(f'Error: Cannot write "{file_name}" as it is outside the permitted working directory')
        return
    if not os.path.exists(os.path.join(working_directory, file_name)):
        # Create the file if it doesn't exist
        open(os.path.join(working_directory, file_name), 'x').close()
    with open(os.path.join(working_directory, file_name), 'w') as file:
        file.write(content)
    return f'Successfully wrote to "{file_name}" ({len(content)} characters written)'