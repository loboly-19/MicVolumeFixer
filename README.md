# Microphone Volume Monitor

This Python script utilizes the PyCAW and COMTypes libraries to monitor and maintain your microphone input volume in Windows.  It actively counteracts applications that try to lower your microphone volume.

**Features**

* Checks your default microphone volume level.
* Automatically raises the volume back to 100% if it detects a decrease below 95%.
* Runs continuously in the background.
* only consume 0.8mb of RAM.

**Usage**

1. **Dependencies:**  Ensure you have PyCAW and COMTypes installed. You can usually do this with `pip install pycaw comtypes`.
2. **Run the Script:** Execute the Python script. It will begin monitoring your microphone volume.

**Customization**

* Modify the `time.sleep(3)` parameter to change the check frequency.
* Change the threshold (currently 95%) for when the volume will be reset.

**Note:** This script is designed for Windows environments.
