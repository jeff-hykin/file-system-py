import file_system_py as FS


*folders, name, extension = FS.path_pieces("/this/is/a/filepath.txt")
print(f'''*folders = {folders}''')

FS.remove("./a folder")
FS.remove("./a file")


FS.list_paths_in("./thing/things")
FS.list_basenames_in("./thing/things")
FS.list_file_paths_in("./thing/things")
FS.list_folder_paths_in("./thing/things")