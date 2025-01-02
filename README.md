https://img.shields.io/github/stars/hackernikitaHACK/benv?style=social
https://img.shields.io/github/forks/hackernikitaHACK/benv?style=social
https://img.shields.io/github/issues/hackernikitaHACK/benv?style=social



```markdown
# benv - Virtual Environment Manager

`benv` is a command-line utility that helps you create, manage, and delete virtual environments in Python. This tool also allows you to activate the environment and run Bash within it. It is designed to be simple and easy to use.

## Features

- **Create virtual environments**: Quickly set up a Python environment with `benv --create <env_name>`.
- **Activate the environment**: Launch Bash in the virtual environment with `benv --bash <env_name>`.
- **Delete virtual environments**: Remove virtual environments with `benv --delete <env_name>`.

## Installation

### Step 1: Download or Clone the Repository

You can download the source code of `benv` from GitHub or clone the repository using the following command:

```bash
git clone https://github.com/hackernikitaHACK/benv.git
```

### Step 2: Set up `benv` (Windows Only)

1. **Navigate to the `benv` directory** where you downloaded or cloned the repository.

2. **Add the `benv` folder to your system's `PATH`**:

    - Open a Command Prompt as Administrator.
    - Run the following command to add the `benv` folder to your `PATH`:

    ```bash
    python setting.bat
    ```

    This batch file automatically adds the `benv` directory to your system's `PATH` so that you can run `benv` from anywhere on your machine.

### Step 3: Verify Installation

To verify that the installation was successful and `benv` is available in your `PATH`, run the following command in any Command Prompt:

```bash
benv --help
```

If everything is set up correctly, you should see the usage instructions for `benv`.

## Usage

### 1. Create a Virtual Environment

To create a new virtual environment, run:

```bash
benv --create <env_name>
```

Replace `<env_name>` with the name you want to give your environment.

### 2. Activate the Virtual Environment and Run Bash

To activate an existing environment and run Bash inside it, use the following command:

```bash
benv --bash <env_name>
```

### 3. Delete a Virtual Environment

If you want to delete an environment, run:

```bash
benv --delete <env_name>
```

This will remove the specified environment from your system.

## Troubleshooting

- If you encounter an issue where the `benv` command is not recognized, make sure that the `benv` folder is correctly added to your system's `PATH`. You can check this by running `echo %PATH%` in the Command Prompt to ensure the `benv` folder is included.

## Contributing

We welcome contributions to the `benv` project! To contribute, please follow these steps:

1. Fork the repository.
2. Clone your forked repository to your local machine.
3. Make your changes.
4. Submit a pull request with a description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
