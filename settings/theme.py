# import os
import subprocess

def get_color(color):
    # Run the command and capture its output
    output = subprocess.check_output(['theme-compositor', '--get-theme-color', color])

    # Decode the output from bytes to a string
    output_str = output.decode()

    # Print the output
    return output_str.strip()
