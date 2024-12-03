
# Deployment Script for ResearchMaestro System with MyGPT Inclusion
import zipapp
import os
import hashlib

def calculate_file_hash(file_path, hash_algorithm="sha256"):
    """Calculate the hash of the file for integrity verification."""
    hash_func = hashlib.new(hash_algorithm)
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def create_package_with_metadata(source_dir, output_file, metadata_file, entry_point=None):
    """Package the ResearchMaestro system, include MyGPT, and generate metadata."""
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory {source_dir} does not exist.")

    # Ensure MyGPT files are present
    mygpt_path = os.path.join(source_dir, "MyGPT")
    if not os.path.exists(mygpt_path):
        raise FileNotFoundError("MyGPT folder is missing. Please add it before packaging.")

    # Create the package
    zipapp.create_archive(source_dir, target=output_file, main=entry_point)
    print(f"Package created: {output_file}")

    # Generate the hash
    package_hash = calculate_file_hash(output_file)
    print(f"SHA-256 hash of the package: {package_hash}")

    # Save the metadata
    with open(metadata_file, "w") as meta_file:
        meta_file.write(f"Package: {output_file}\n")
        meta_file.write(f"SHA-256: {package_hash}\n")
    print(f"Metadata saved to: {metadata_file}")

if __name__ == "__main__":
    source_directory = "/mnt/data/ResearchMaestroTest"
    output_filename = "/mnt/data/ResearchMaestroChatGPT.pyz"
    metadata_filename = "/mnt/data/ResearchMaestroChatGPT_Metadata.txt"
    entry_point = "ResearchMaestro_Module:ResearchMaestro"  # Example entry point
    create_package_with_metadata(source_directory, output_filename, metadata_filename, entry_point)
