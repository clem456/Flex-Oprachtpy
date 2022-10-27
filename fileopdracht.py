import os

currentfile = os.getcwd()

files = os.scandir(currentfile)

for file in files:
    if file.is_file():
        print(file.name, "is een bestand")
    elif file.is_dir():
        print(file.name, "is een map")
    else:
        print(file.name, "is onbekend")
