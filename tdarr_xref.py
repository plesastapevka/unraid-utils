import csv
import os
import PTN

# Open the CSV file
with open("/Users/plesasta_pevka/Downloads/tdarr_files.csv", "r") as csv_file:
    # Create a CSV reader object
    reader = csv.DictReader(csv_file)

    # Iterate over the rows in the CSV file
    for row in reader:
        # Get the filename for the current row
        file_path = row["_id"]

        # Construct the full file path
        last_path = os.path.basename(os.path.normpath(file_path))
        file_title = PTN.parse(last_path)
        print(file_title)

        # file_path = os.path.join("/mnt/user/plex/downloads", filename)

        # Check if the file or folder exists
        # if os.path.exists(file_path):
            # If it does, delete it
            # if os.path.isfile(file_path):
                # os.remove(file_path)
            # else:
            #     shutil.rmtree(file_path)
