import sys
import os
from typing import List
from datetime import datetime


class FileCreator:
    def create_directories(self, path_parts: List[str]) -> str:
        path = os.path.join(*path_parts)
        os.makedirs(path, exist_ok=True)
        return path

    def create_file_with_content(self, file_path):
        content_lines = []
        while True:
            line = input("Enter content line: ")
            if line.strip().lower() == "stop":
                break
            content_lines.append(line)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_exists = os.path.exists(file_path)

        with open(file_path, "a") as file:
            if file_exists:
                file.write("\n")
            file.write(f"{timestamp}\n")
            for i, line in enumerate(content_lines, start=1):
                file.write(f"{i} {line}\n")

    def process_arguments(self, args):
        args = sys.argv[1:]
        dir_path = os.getcwd()
        if not args:
            print(
                "Usage: python create_file.py -d [directories] -f [file_name]"
            )
            return

        if "-d" in args:
            d_index = args.index("-d")
            directories = []
            for arg in args[d_index + 1:]:
                if arg.startswith("-"):
                    break
                directories.append(arg)
            dir_path = (
                self.create_directories(directories)
                if directories else os.getcwd()
            )
            

        if "-f" not in args:
            return

        f_index = args.index("-f")
        file_name = args[f_index + 1]
        file_path = os.path.join(dir_path, file_name)
        self.create_file_with_content(file_path)


def main():
    args = sys.argv[1:]
    FileCreator().process_arguments(args)


if __name__ == "__main__":
    main()
