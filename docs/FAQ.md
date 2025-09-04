# Frequently Asked Questions (FAQ)

## General Questions

### 1. The app doesn't start on Windows/macOS

See the **"Security Notice"** section in the [README](../README.md) for instructions on how to bypass OS security blocks.

### 2. Where do I get the JSON files?

Follow the guide: [How to Request and Download Your Instagram Data](docs/INSTAGRAM_DATA_GUIDE.md).

### 3. Is my data safe?

Yes, all processing is done locally. No data is sent online, and no Instagram credentials are required.

### 4. What version of Python do I need?

Python 3.10 or newer is recommended.

### 5. How do I update the app?

Download the latest release from [GitHub Releases](https://github.com/SmartsvXD/InstaUnfollowerFinder/releases) and replace the old files.

### 6. Can I use this on Linux?

Yes, but only the source code version. The compiled app is available for Windows and macOS.

### 7. Who developed this?

SmartsvXD, Italy, 2024-2025.

---

## CLI Questions

### 1. I get errors like 'ModuleNotFoundError: No module named colorama'

Make sure you ran `pip install .` in the main project folder (where `pyproject.toml` is located).

### 2. I can't see the list of unfollowers

Check that you placed the JSON files (`followers.json` and `following_1.json`) in the correct folder (main project directory).

### 3. How do I add someone to the whitelist in CLI?

Edit the `whitelist.json` file manually and add the usernames you want to whitelist.

---

## GUI Questions

### 1. How do I add someone to the whitelist in GUI?

Click the blue plus next to the username in the app interface.

### 2. How do I open an Instagram profile from the app?

Click on the username in the unfollower list to open their Instagram page in your default browser.
