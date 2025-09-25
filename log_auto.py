import os
import zipfile
import shutil
import sys

def open_file(path):
    os.startfile(path)

def get_file_from_path(input_path):
    input_path = os.path.normpath(input_path)
    parts = input_path.split(os.sep)

    curr_path = parts[0] + os.sep
    working_dir = os.getcwd()

    for i in range(1, len(parts)):
        next_part = parts[i]
        candidate_path = os.path.join(curr_path, next_part)
        candidate_zip = candidate_path + ".zip"

        if os.path.isfile(candidate_zip):
            # Found a zip file instead of a folder
            extract_dir = os.path.join(working_dir, os.path.basename(next_part))
            if not os.path.exists(extract_dir):
                print(f"Extracting {candidate_zip} -> {extract_dir}")
                with zipfile.ZipFile(candidate_zip, 'r') as zf:
                    zf.extractall(extract_dir)
            curr_path = extract_dir
        else:
            curr_path = candidate_path

    return curr_path

if __name__ == "__main__":
    # Check if command line argument is given
    if len(sys.argv) != 2:
        print("Usage: python script.py <full_file_path>")
        sys.exit(1)

    input_path = sys.argv[1]  # Take input from command line

    final_file = get_file_from_path(input_path)

    if os.path.isfile(final_file):
        working_dir = os.getcwd()
        dest_file = os.path.join(working_dir, os.path.basename(final_file))
        shutil.copy2(final_file, dest_file)

        print(f"Downloaded to: {dest_file}")
        print(f"Opening: {dest_file}")
        open_file(dest_file)
    else:
        print("File not found:", final_file)




import os

# Map network drive
os.system(r'net use Z: \\10.13.66.64\up /user:karthik tiger')

# Delete network drive
os.system(r'net use Z: /delete /y')


import os

# Input UNC path
input_path = r"\\10.13.66.64\karthik\abc\01_xyz\star\02_abc\sample.log"

# Map UNC root to Z: drive
UNC_ROOT = r"\\10.13.66.64\karthik"
DRIVE_LETTER = "Z:"

# Check that input_path starts with UNC root
if input_path.startswith(UNC_ROOT):
    # Remove UNC root from path
    relative_path = input_path[len(UNC_ROOT):]
    # Ensure no leading backslash
    if relative_path.startswith("\\"):
        relative_path = relative_path[1:]
    # Join with drive letter
    new_path = os.path.join(DRIVE_LETTER + os.sep, relative_path)
    print(new_path)
else:
    print("Input path does not start with expected UNC root.")


