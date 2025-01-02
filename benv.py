import os
import shutil
import sys
import subprocess
import venv

# Function to create a virtual environment
def create_virtual_env(env_name):
    if not os.path.exists(env_name):
        venv.create(env_name, with_pip=True)
        print(f"Virtual environment '{env_name}' successfully created.")
    else:
        print(f"Virtual environment '{env_name}' already exists.")

# Function to activate and run Bash in the environment
def run_bash_in_env(env_name):
    activate_script = os.path.join(env_name, "Scripts", "activate.bat")  # Windows-specific
    if not os.path.exists(activate_script):
        print(f"Activation script not found. Please check if the virtual environment '{env_name}' exists.")
        return

    print(f"Launching Bash in virtual environment '{env_name}'...")
    subprocess.run(["cmd", "/k", activate_script])

# Function to delete a virtual environment
def delete_virtual_env(env_name):
    if os.path.exists(env_name):
        shutil.rmtree(env_name)
        print(f"Virtual environment '{env_name}' successfully deleted.")
    else:
        print(f"Virtual environment '{env_name}' not found.")

# Command handler
def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  benv --create <env_name>   # Create a virtual environment")
        print("  benv --bash <env_name>     # Activate Bash in the environment")
        print("  benv --delete <env_name>   # Delete a virtual environment")
        sys.exit(1)

    command = sys.argv[1]
    if command == "--create":
        if len(sys.argv) < 3:
            print("Error: Environment name is missing.")
            print("Usage: benv --create <env_name>")
            sys.exit(1)
        env_name = sys.argv[2]
        create_virtual_env(env_name)

    elif command == "--bash":
        if len(sys.argv) < 3:
            print("Error: Environment name is missing.")
            print("Usage: benv --bash <env_name>")
            sys.exit(1)
        env_name = sys.argv[2]
        run_bash_in_env(env_name)

    elif command == "--delete":
        if len(sys.argv) < 3:
            print("Error: Environment name is missing.")
            print("Usage: benv --delete <env_name>")
            sys.exit(1)
        env_name = sys.argv[2]
        delete_virtual_env(env_name)

    else:
        print(f"Unknown command: {command}")
        print("Available commands:")
        print("  benv --create <env_name>   # Create a virtual environment")
        print("  benv --bash <env_name>     # Activate Bash in the environment")
        print("  benv --delete <env_name>   # Delete a virtual environment")

if __name__ == "__main__":
    main()