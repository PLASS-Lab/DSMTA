import gdown
import zipfile
import os

# Google Drive shareable link
file_url = "https://drive.google.com/uc?id=1bSSrI63FtNlo5h0zPOGCtARhNdiI9ixS"

# Directory where the file will be downloaded
download_dir = "./dataset"
os.makedirs(download_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Path for the downloaded zip file
output_zip = os.path.join(download_dir, "validation.zip")

# Step 1: Download the zip file
print(f"Downloading the file to {download_dir}...")
gdown.download(file_url, output_zip, quiet=False)

# Step 2: Unzip the downloaded file
print("Unzipping the file...")
output_dir = os.path.join(download_dir, "unzipped_files")  # Directory to extract files
os.makedirs(output_dir, exist_ok=True)

with zipfile.ZipFile(output_zip, 'r') as zip_ref:
    zip_ref.extractall(output_dir)

print(f"File unzipped to directory: {output_dir}")

# Step 3: Unzip the downloaded val_quasiraw.zip file
print("Unzipping val_quasiraw file...")
output_dir_val_quasiraw = os.path.join(output_dir, "val_quasiraw")  # Directory to extract files
os.makedirs(output_dir_val_quasiraw, exist_ok=True)
zip_val_quasiraw = os.path.join(output_dir, "val_quasiraw.zip")
with zipfile.ZipFile(zip_val_quasiraw, 'r') as zip_ref:
    zip_ref.extractall(output_dir_val_quasiraw)

print(f"File unzipped to directory: {output_dir}")

# Step 4: Unzip the downloaded val_labels.zip file
print("Unzipping val_labels file...")
output_dir_val_labels = os.path.join(output_dir, "val_labels")  # Directory to extract files
os.makedirs(output_dir_val_labels, exist_ok=True)
zip_val_labels = os.path.join(output_dir, "val_labels.zip")
with zipfile.ZipFile(zip_val_labels, 'r') as zip_ref:
    zip_ref.extractall(output_dir_val_labels)

print(f"File unzipped to directory: {output_dir_val_labels}")

