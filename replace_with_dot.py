import os
import glob


def main():
    # Get a list of all files in the current directory
    files = glob.glob("*")

    # Iterate over the files
    for file in files:
        # Replace spaces in the file name with dots
        new_name = file.replace(" ", ".")
        # Rename the file
        os.rename(file, new_name)

if __name__ == "__main__":
    main()
