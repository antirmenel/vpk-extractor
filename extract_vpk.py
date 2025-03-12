import vpk
import os
from tqdm import tqdm
import zipfile

def extract_vpk_to_zip(vpk_file, output_zip):
    try:
        if not os.path.isfile(vpk_file):
            print(f"Error: The file '{vpk_file}' does not exist. Please check the path and try again.")
            return
        
        output_dir = os.path.dirname(output_zip)
        if not os.path.exists(output_dir):
            print(f"Error: The directory '{output_dir}' does not exist. Please create the directory and try again.")
            return
        
        print("Hang tight, extracting files... This might take a moment.")
        
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            with vpk.VPK(vpk_file) as archive:
                total_files = len(archive)
                total_size = sum(len(archive[filename].read()) for filename in archive)

                with tqdm(total=total_files, desc="Extracting", unit="file", ncols=100, dynamic_ncols=True) as pbar:
                    for filename in archive:
                        file_data = archive[filename].read()
                        zipf.writestr(filename, file_data)

                        pbar.update(1)
                        current_size = len(file_data)
                        pbar.set_postfix(file=f"{filename}", size=f"{current_size/1024:.2f} KB", total_size=f"{total_size/1024:.2f} KB")
            
            print(f"Extraction completed successfully! Files are saved to {output_zip}")
    
    except Exception as e:
        print(f"Error occurred during extraction: {e}")

vpk_file = input("Enter the full path to your VPK file: ").strip('"')
output_zip = input("Enter the full path where you want the extracted ZIP to be saved (end with 'extracted_files.zip'): ").strip('"')

extract_vpk_to_zip(vpk_file, output_zip)
