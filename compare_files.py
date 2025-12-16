import os

VERSIONS_DIR = "versions"

def compare_files(file1, file2):
    path1 = os.path.join(VERSIONS_DIR, file1)
    path2 = os.path.join(VERSIONS_DIR, file2)

    if not os.path.exists(path1) or not os.path.exists(path2):
        print("❌ One or both files do not exist")
        return

    with open(path1, "r", encoding="utf-8") as f1:
        lines1 = f1.readlines()

    with open(path2, "r", encoding="utf-8") as f2:
        lines2 = f2.readlines()

    print("\n--- File Difference ---")

    max_len = max(len(lines1), len(lines2))

    for i in range(max_len):
        l1 = lines1[i].strip() if i < len(lines1) else ""
        l2 = lines2[i].strip() if i < len(lines2) else ""

        if l1 != l2:
            if l1:
                print(f"- {l1}")
            if l2:
                print(f"+ {l2}")

# -------- USER INPUT --------
file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")

compare_files(file1, file2)
