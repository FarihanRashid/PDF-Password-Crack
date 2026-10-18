# PDF Unlocker Setup

This folder contains a simple script to remove PDF restrictions using a local Python virtual environment.

## Steps

1. Open PowerShell in this folder.
2. Create the virtual environment:

   .env\Scripts\activate  # use Command Prompt
   # or
   .\.env\Scripts\Activate.ps1  # use PowerShell

3. Install dependencies:

   pip install -r requirements.txt

4. Edit `unlock.py` and replace `your_file.pdf` with your actual PDF filename.

5. Run the script:

   python unlock.py

6. Check `unlocked_file.pdf` for the output.

## Notes

- The virtual environment stays inside the `.env` folder.
- Deleting `.env` removes the installed packages and Python environment.
- This setup does not affect system Python or global packages.
