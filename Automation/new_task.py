import os
import datetime
from datetime import datetime, timedelta

path = "C:/Python_Workshop"
archive_folder = os.path.join(path, "Archive")

# Create "Archive" folder if it doesn't exist
if not os.path.exists(archive_folder):
    os.makedirs(archive_folder)

print("Files and directories in '% s':" % path)

# Calculate cutoff date for files older than 7 days
cutoff_date = datetime.now() - timedelta(days=7)

obj = os.scandir(path)
for entry in obj:
    if entry.is_file():
        file_path = os.path.join(path, entry.name)
        file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))

        # Check if the file is older than the cutoff date
        if file_mtime < cutoff_date:
            # Move file to "Archive" folder
            os.rename(file_path, os.path.join(archive_folder, entry.name))
            print(f"Moved: {entry.name}")
    elif entry.is_dir() and entry.name != "Archive":
        print(f"Directory: {entry.name}")

# Confirm deletion of the "Archive" folder
confirm = input("Do you want to delete the 'Archive' folder? (yes/no): ").strip().lower()
if confirm == "yes":
    for entry in os.scandir(archive_folder):
        os.remove(entry.path)
    os.rmdir(archive_folder)
    print("'Archive' folder deleted.")
else:
    print("Deletion canceled.")
