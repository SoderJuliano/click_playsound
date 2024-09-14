
# Keypress Sound Script with systemd Service

This project provides a Python script that plays a sound file when a specific key is pressed. It also includes a `systemd` service file to run the script as a background service that starts automatically on system boot.

## Overview

- The script listens for key presses and plays a sound when a key is pressed.
- It uses `pygame` for sound playback and `pynput` for keyboard interaction.
- A `systemd` service can be set up to ensure the script runs automatically in the background.

## Requirements

- **Python 3.x**: Ensure Python 3 is installed on your system.
- **pygame**: A Python package used to handle sound playback.
- **systemd**: For managing the service and making the script run at startup.

## Quick Setup (Updated: 14-09-24)

### Step 1: Run the Setup Script
1. Go to the downloaded repository and find the file `clicker.sh`.
2. Run the following commands in your terminal:
   ```bash
   chmod +x clicker.sh
   ./clicker.sh
   ```

This script will handle most of the setup process for you.

---

## Old Instructions (Manual Setup)

### Installation and Setup

#### 1. Set Up Python Virtual Environment

1. Navigate to the project directory:
   ```bash
   cd /home/soder/Documents/system
   ```

2. Create a Python virtual environment:
   ```bash
   python3 -m venv myenv
   ```

3. Activate the virtual environment:
   ```bash
   source myenv/bin/activate
   ```

4. Install the required Python packages:
   ```bash
   pip install pygame pynput
   ```

#### 2. Add the Script to `systemd` (Optional)

To ensure the script runs automatically on boot as a background service:

1. Create a systemd service file:
   ```bash
   sudo nano /etc/systemd/system/keylistener.service
   ```

2. Add the following content to the service file:
   ```ini
   [Unit]
   Description=Keypress Sound Service
   After=network.target

   [Service]
   ExecStart=/home/soder/Documents/system/myenv/bin/python /home/soder/Documents/system/keylistener.py
   WorkingDirectory=/home/soder/Documents/system
   StandardOutput=inherit
   StandardError=inherit
   Restart=always
   User=your-username

   [Install]
   WantedBy=multi-user.target
   ```

3. Enable and start the service:
   ```bash
   sudo systemctl enable keylistener.service
   sudo systemctl start keylistener.service
   ```

---

## Usage

Once set up, the script will listen for key presses and play a sound whenever a key is pressed. If set up with `systemd`, the script will start automatically on boot.

---

## Troubleshooting

- **No sound?** Ensure your sound file (`key_press.wav`) is in the same directory as the script.
- **Virtual environment issues?** Ensure you've activated the virtual environment before running the script.

---

## License

This project is licensed under the MIT License.

---

This README should provide a clear guide for users to set up, use, and troubleshoot your keypress sound script!