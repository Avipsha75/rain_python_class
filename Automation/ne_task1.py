import os
import datetime

# Scan the example_directory and its subdirectories
for root, dirs, files in os.walk("./example_directory"):
    for file in files:
        file_path = os.path.join(root, file)
        # Check if the file is older than 1 minute
        file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        if datetime.datetime.now() - file_mtime > datetime.timedelta(minutes=1):
            try:
                # Ask for confirmation to delete the file
                user_input = input(f"Do you want to delete {file_path}? (y/n): ").strip().lower()
                if user_input == "y":
                    os.remove(file_path)
                    print(f"Deleted {file_path}")
                else:
                    print(f"Skipped {file_path}")
            except OSError as e:
                print(f"Error deleting {file_path}: {e}")