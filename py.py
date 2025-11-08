import os
import shutil

base_file = "project_base.txt"

# check if base file exists
if not os.path.exists(base_file):
    with open(base_file, "w") as f:
        f.write("It is version 1\n")
    print("✅ Base file created and also version also created")

# create 'versions' folder if not exists
if not os.path.exists("versions"):
    os.mkdir("versions")

# count existing versions
version_count = len(os.listdir("versions")) + 1

# check if base file exists
if os.path.exists(base_file):
    # create new version file
    new_version = f"versions/project_v{version_count}.txt"
    shutil.copy(base_file, new_version)
    print(f"✅ New version created: {new_version}")
else:
    print("❌ Base file not found.")
