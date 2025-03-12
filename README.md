
# VPK to ZIP Extraction Tool

This Python script extracts files from a **VPK (Valve Pak)** archive and saves them as a **ZIP** file.  
The tool uses the `vpk` library to read VPK files and the `zipfile` module to create a compressed ZIP archive.

## Features

- Extracts all files from a VPK archive.
- Displays a progress bar during extraction using `tqdm`.
- Allows the user to specify the VPK file and output ZIP file paths.
- Handles large VPK files efficiently by reading and writing in chunks.
- Simple command-line interface for ease of use.

## Requirements

- **Python 3.x**
- Required libraries:
  - `vpk` (for reading VPK files)
  - `tqdm` (for the progress bar)

You can install the required libraries by running:

```
pip install vpk tqdm
```


## Important Notes
Ensure that the path to your VPK file is correct and points to a valid VPK file.

The output path should **end** with **extracted_files.zip** to specify where the ZIP file will be saved.

You might need **Administrator privileges** to run the script, especially if you encounter permission issues.  

To run the script as an Administrator:

Windows: Right-click on Command Prompt and select "Run as Administrator".

## Troubleshooting
**1. Invalid VPK File**
If the script fails with the error File is not VPK (invalid magic), ensure that you’re using a valid VPK file.  
You can verify the integrity of the VPK file using tools like GCFScape or VPKTool.

**2. Permission Denied**
If you encounter permission issues, try running the terminal as an Administrator:

Windows: Right-click on Command Prompt and select "Run as Administrator".

**3. Missing Libraries**  
If you see errors about missing libraries, install the required packages by running:

```
pip install vpk tqdm
```
## License
This project is licensed under the MIT License.   




**Made with ❤️ by Menel**
