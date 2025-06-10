import os

def get_files_info(working_directory, directory=None):
    full_path_cwd = os.path.abspath(working_directory)

    if not os.path.abspath(os.path.join(full_path_cwd, directory)).startswith(full_path_cwd):
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return
    if not os.path.isdir(os.path.join(working_directory, directory)):
        print(f'Error: "{directory}" is not a directory')
        return
    wanted_dir = os.path.join(full_path_cwd, directory)
    for file in os.listdir(wanted_dir):
        print(f'{file}: file_size={os.path.getsize(os.path.join(wanted_dir, file))}, is_dir={os.path.isdir(os.path.join(wanted_dir, file))}')
