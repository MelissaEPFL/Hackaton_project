import subprocess
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the PowerShell script
script_path = os.path.join(current_dir, 'script.ps1')

# Launch the PowerShell script
subprocess.run(['powershell', '-File', script_path])
