import os
import datetime
import shutil

# directory = "example directory"

# os.makedirs(directory, exist_ok=True)
# with open(os.path.join(directory, "Jan20_42.zip"), "w") as f:
#     f.write("Zip file content")

# shutil.make_archive(directory, "zip", directory)

def create_backup(source_directory):
    if not os.path.exists(source_directory):
        print(f"Error: The directory '{source_directory}' does not exist.")
        return
    
    #Generate a timestamped backup name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}"

    #Create a zip archive of the source directory
    shutil.make_archive(backup_name, 'zip', source_directory)
    print(f"Backup created: {backup_name}.zip")

#Example usage
create_backup("./example_directory")
