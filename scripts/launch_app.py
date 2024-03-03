import os
import webbrowser

def launch_website():
    # Path to the directory containing your website
    website_dir = 'app/'

    # Check if the directory exists
    if os.path.exists(website_dir):
        # Get the absolute path of the directory
        abs_website_dir = os.path.abspath(website_dir)
        
        # Open the website in the default web browser
        webbrowser.open('file://' + abs_website_dir + '/index.html')
        print("Website launched successfully.")
    else:
        print("Error: Website directory not found.")

if __name__ == "__main__":
    launch_website()