#!/bin/bash

# Define possible directories
DIR1="$HOME/Documents/system"
DIR2="$HOME/system"

# Function to check and run the commands if directory exists
run_script() {
    if [ -d "$1" ]; then
        cd "$1" || exit
        echo "Changed directory to $1"

        # Create a virtual environment
        python3 -m venv myenv
        echo "Virtual environment 'myenv' created"

        # Activate the virtual environment
        source myenv/bin/activate
        echo "Virtual environment 'myenv' activated"

        # Run the Python script
        python playsound.py
        echo "Python script 'playsound.py' executed"
    else
        return 1
    fi
}

# Try the first directory
if ! run_script "$DIR1"; then
    # If the first directory doesn't exist, try the second one
    if ! run_script "$DIR2"; then
        echo "Neither $DIR1 nor $DIR2 exists"
        exit 1
    fi
fi
