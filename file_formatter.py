#auto format files to be lowercase have spaces not dashes or camel case

import os

code_folder = os.getcwd()
exclude_folders = ["Plugins", "Testing"]

def format_name(name):
    return name.lower().replace("-", " ")

def folder_iter_2(path):
    with os.scandir(path) as parent_entries:
        for entry in parent_entries:
            if entry.is_file():
                continue
            with os.scandir(entry.path) as child_entries:
                for child_entry in child_entries:
                    if child_entry.is_file() or child_entry.name in exclude_folders:
                        continue
                    else:
                        os.rename(entry.path + "\\" + child_entry.name, entry.path + "\\" + format_name(child_entry.name))
                        print("formatting " + entry.path + "\\" + child_entry.name + " to " + entry.path + "\\" + format_name(child_entry.name))

if __name__ == "__main__":
    folder_iter_2(code_folder)