import os
import shutil

directory = "example directory"

os.makedirs(directory, exist_ok=True)
with open(os.path.join(directory, "Jan20_42.zip"), "w") as f:
    f.write("Zip file content")

shutil.make_archive(directory, "zip", directory)
