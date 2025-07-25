import gdown
import zipfile
import os


# Google Drive shareable link
file_url = "https://drive.google.com/uc?id=1IuuoZTK8tz9PSyoaoGSR3cNuq5JSJBCA"

# Directory where the file will be downloaded
download_dir = "./dataset"
# os.makedirs(download_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Path for the downloaded zip file
output_zip = os.path.join(download_dir, "train.zip")

# Step 1: Download the zip file
print(f"Downloading the file to {download_dir}...")
gdown.download(file_url, output_zip, quiet=False)

# Step 2: Unzip the downloaded file
print("Unzipping train.zip ...")
output_dir = os.path.join(download_dir, "training_unzipped_files")  # Directory to extract files
os.makedirs(output_dir, exist_ok=True)

with zipfile.ZipFile(output_zip, 'r') as zip_ref:
    zip_ref.extractall(output_dir)

print(f"File unzipped to directory: {output_dir}")

# Step 3: Unzip the downloaded val_quasiraw.zip file
print("Unzipping train_quasiraw file...")
output_dir_val_quasiraw = os.path.join(output_dir, "train_quasiraw")  # Directory to extract files
os.makedirs(output_dir_val_quasiraw, exist_ok=True)
zip_val_quasiraw = os.path.join(output_dir, "train_quasiraw.zip")
with zipfile.ZipFile(zip_val_quasiraw, 'r') as zip_ref:
    zip_ref.extractall(output_dir_val_quasiraw)

print(f"File unzipped to directory: {output_dir}")

# Step 4: Unzip the downloaded val_labels.zip file
print("Unzipping train_labels file...")
output_dir_train_labels = os.path.join(output_dir, "train_labels")  # Directory to extract files
os.makedirs(output_dir_train_labels, exist_ok=True)
zip_train_labels = os.path.join(output_dir, "train_labels.zip")
with zipfile.ZipFile(zip_train_labels, 'r') as zip_ref:
    zip_ref.extractall(output_dir_train_labels)

print(f"File unzipped to directory: {output_dir_train_labels}")