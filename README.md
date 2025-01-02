https://img.shields.io/github/stars/hackernikitaHACK/benv?style=social
https://img.shields.io/github/forks/hackernikitaHACK/benv?style=social
https://img.shields.io/github/issues/hackernikitaHACK/benv?style=social



Если вы хотите, чтобы в вашем скрипте `benv` не использовался `.bat` файл для настройки пути, а путь нужно было бы настраивать вручную, вы можете изменить подход и удалить зависимость от `.bat` файла. Вместо этого пользователь сам должен будет добавить путь в системные переменные `PATH`. Вот как это можно описать в `README.md`:

```markdown
# benv - Windows Bash Virtual Environment Manager

`benv` is a simple command-line utility designed for Windows users that allows you to easily create, manage, and delete virtual Python environments. It provides an easy way to set up a Bash environment within a virtual environment, enabling users to run Bash commands and work within isolated environments.

## Key Features

- **Create virtual environments**: Set up isolated Python environments with ease.
- **Activate and run Bash**: Launch Bash within a virtual environment on Windows.
- **Delete virtual environments**: Easily delete the virtual environments when no longer needed.
  
This project is perfect for those who want to work with Bash in a Windows environment and manage multiple Python virtual environments in a clean and simple manner.

## Installation

### Step 1: Download or Clone the Repository

You can download the source code of `benv` from GitHub or clone the repository using the following command:

```bash
git clone https://github.com/hackernikitaHACK/benv.git
```

### Step 2: Add `benv` to the System `PATH`

To use `benv` from anywhere on your machine, you need to manually add its directory to your system's `PATH`:

1. **Find the directory where you cloned or downloaded the `benv` repository.**

2. **Add the directory to your system's `PATH`:**
   
   - **Windows 10/11**:
     1. Open the Start menu, type `Environment Variables`, and select **Edit the system environment variables**.
     2. In the System Properties window, click the **Environment Variables** button.
     3. Under **System variables**, find and select the **Path** variable, then click **Edit**.
     4. In the Edit Environment Variable window, click **New** and add the full path to the directory where you saved `benv` (e.g., `C:\path\to\benv`).
     5. Click **OK** to apply the changes.

3. **Verify the installation**:

   After adding the directory to the `PATH`, open a new Command Prompt and check if `benv` is recognized by running the following command:

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
