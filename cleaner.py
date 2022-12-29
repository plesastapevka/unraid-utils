import os
import glob
import re


def main():
    # Get a list of all files in the current directory
    files = glob.glob("*")

    # Iterate over the files
    for file in files:
        # Replace spaces and dashes in the file name with dots
        name = file.replace(" ", ".").replace("-", "")
        new_name = re.sub(r'(?<=\d)\.(?=E)', '', name)
        # Rename the file
        os.rename(file, new_name)


if __name__ == "__main__":
    main()
