import subprocess

def install_dependencies(requirements_file):
    try:
        subprocess.check_call(["pip", "install", "-r", requirements_file])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to install dependencies. {e}")

if __name__ == "__main__":
    requirements_file = "requirements.txt"  # Path to requirements.txt file
    install_dependencies(requirements_file)