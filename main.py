import os
from shutil import rmtree

origin = "cbr_files"
temp_dir = "temp_dir"
final_dir = "cbz_files"

files = os.listdir(origin)

for i in range(len(files)):
    # Make temporary extraction directory
    os.mkdir(temp_dir)
    
    # Extract rar-compressed files into temp directory
    extract_command = f"unrar e \"{origin}/{files[i]}\" {temp_dir}/"
    os.system(extract_command)

    # Compress extracted files into open .cbz format
    zip_command = f"zip -r \"{final_dir}/{files[i][:-3]}cbz\" {temp_dir}/"
    os.system(zip_command)

    # Remove temporary extraction directory
    rmtree(temp_dir)
