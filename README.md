# Cryptography-Network-Security-MiniProject


--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

# Keylogger Awareness Project

## Overview

This project demonstrates the potential risks associated with keyloggers and emphasizes the importance of cybersecurity awareness. It aims to educate users about the dangers of clicking unknown links and downloading unfamiliar files. By simulating a keylogger, the project highlights how easily sensitive information can be captured and misused.

## Features

- **Keylogger Simulation**: A script that captures keystrokes and sends them via email to demonstrate how keyloggers operate.
- **Web Interface**: A simple web page that simulates a phishing scenario, encouraging users to activate a "coupon code" that triggers the keylogger.
- **Automated Execution**: The keylogger runs automatically when the user interacts with the web page, mimicking real-world phishing attacks.
- **Educational Content**: Information on how keyloggers work, their potential impacts, and how to protect against them.

## How It Works

1. **Setup**:
   - The web server hosts a page with an enticing offer to activate a coupon code.
   - When the user clicks the button, a batch file executes the keylogger script.

2. **Keylogger Functionality**:
   - The keylogger captures keystrokes and periodically sends the log to a specified email address.
   - After running for a specified duration, the keylogger stops to prevent continuous logging.

3. **Demonstration**:
   - This project is intended for educational purposes to demonstrate how easily keyloggers can capture sensitive information.

## Key Components

- **Python Keylogger Script**: Captures and emails keystrokes.
- **Batch File**: Automates the execution of the keylogger.
- **HTML/CSS/JavaScript**: Creates the phishing-like web page.
- **SMTP**: Sends captured keystrokes to the specified email.




