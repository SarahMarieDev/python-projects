# Password Manager

This project is a simple password manager application built using Python and Tkinter. It allows users to generate and save passwords securely.

## Features

- **Password Generation**: Generates random passwords including letters, numbers, and symbols.
- **Save Passwords**: Saves passwords along with the website and login information.
- **Clipboard Copy**: Automatically copies the generated password to the clipboard.
- **Custom Dialog**: Custom confirmation dialog before saving the password.

## Requirements

- Python 3.9
- Tkinter (usually included with Python installations)
- pyperclip

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/password-manager.git
    cd password-manager
    ```

2. **Install dependencies**:
    ```sh
    pip install pyperclip
    ```

## Usage

1. **Run the application**:
    ```sh
    python password_manager.py
    ```

2. **Generate Password**:
    - Click on the "Generate Password" button to create a random password.

3. **Save Password**:
    - Enter the website and login details.
    - Click "Add" to save the password.
4. **Search for login details**:
    - Enter the website and click "Search".
