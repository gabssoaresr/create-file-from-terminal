from datetime import datetime
from sys import argv
from os import mkdir, chdir

filename = ""
directories = []

if "-f" in argv:
    index = 0

    for _ in range(len(argv) - 1):
        index += 1
        if argv[_: _ + 1] == ["-f"]:
            break

    filename = argv[index]

    if "-d" in argv:
        index2 = 0

        for _ in range(len(argv) - 1):
            index2 += 1
            if argv[_: _ + 1] == ["-d"]:
                break

        directories = argv[index2:index - 1]
else:
    filename = "file.txt"

    if "-d" in argv:
        index = 0

        for _ in range(len(argv) - 1):
            index += 1
            if argv[_: _ + 1] == ["-d"]:
                break

        directories = argv[index:len(argv)]

file_data = [datetime.today().strftime('%y:%d:%m %H-%M-%S'), "\n"]

while True:
    line = input("Enter content line: ")
    if line == "exit":
        break
    file_data.extend([line])

for directory in directories:
    try:
        mkdir(directory)
    except Exception:
        pass
    chdir(directory)

with open(filename, "w") as f:
    f.writelines(file_data)
