import os
import webbrowser

def launch_website():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the parent directory (common root)
    common_root = os.path.abspath(os.path.join(script_dir, os.pardir, os.pardir))

    # Path to the index.html file of your website
    website_index = os.path.join(common_root, 'GreenRoots', 'app', 'index.html')

    # Open the website in the default web browser
    webbrowser.open(website_index)
    print("Website launched successfully.")

if __name__ == "__main__":
    launch_website()
