# Instagram Unfollower Finder

A lightweight tool that helps you manage your Instagram connections efficiently.

Easily identify the people you follow but who don't follow you back —  
**No password or username required, and 100% privacy-friendly!**

<p align="center">
  <img src="assets/demo.gif" alt="App Demo" width="600"/>
</p>

## ❓ What is this?

Instagram (via Meta) allows you to download your personal data — including your followers and following lists.  
This tool compares those lists locally to show you who doesn’t follow you back. It’s fast, simple, and keeps your data safe on your device.

## 📗 Quick Guide

### Run Compiled

#### Step 1: Download the app

- Download the correct compiled version for your system from [GitHub Releases](https://github.com/SmartsvXD/InstaUnfollowerFinder/releases).
- Install and run the app.

#### Step 2: Find Unfollowers

- Click on **"Open Meta Account Center"**.
- Download Instagram information (explained below).
- Click on **"Find Unfollowers"**, and select `followers.json` and `following_1.json` from the folder `connections/followers_and_following` inside the folder you downloaded from Instagram (once you have extracted the ZIP file). If everything is done correctly it should show the list of accounts.

#### Step 3: Extra Features

- By clicking on the username of the unfollower you can open their Instagram page on your default browser.
- By clicking on the blue plus on the left of each username you can add it to the whitelist.

### Run Raw Code

#### Step 0: Install Python (if necessary)

- If you don’t have Python installed, you can download it from the [official Python website](https://www.python.org/).

#### Step 1: Clone the repository

- Clone the repository.

#### Step 2: Download Instagram information

- Read **How to Request and Download Your Instagram Data** below.
  
#### Step 3a: Run the code with the GUI

- Move to the cloned repository folder with  

  ``` bash
  cd path/to/InstaUnfollowerFinder
  ```

- Run `main.py` with  

  ``` bash
  python3 main.py
  ```

- Then follow **Step 2: Find Unfollowers** from the **Run Compiled** section.

#### Step 3b: Run the code in the terminal

- Open  

  ``` text
  ~/connections/followers_and_following
  ```

- Move `followers.json` and `following_1.json` in the cloned repository folder.
- Move to the cloned repository folder with  

  ``` bash
  cd path/to/InstaUnfollowerFinder
  ```

- Run `main.py` with  

  ``` bash
  python3 main.py -t
  ```

  and select **"Find unfollowers"**, if everything is done correctly it should print the list of accounts.

### How to Request and Download Your Instagram Data

- Open Instagram on your browser (make sure you're logged in).
- Click on **"More"**, in the lower left corner of the screen.
- Click on **"Settings"**.
- Click on **"Accounts Center"**, which will take you to the Meta Accounts Center.
- Click on **"Your information and permissions"**.
- Click on **"Download your information"**.
- Click on **"Download or transfer information"**.
- Select your Instagram account.
- Click on **"Some of your information"**.
- Under the **“Connections”** tab, select **“Followers and following”**, then click **“Next”**. \
  (This will make you download only the followers and following lists)
- Choose **"Download to device"**, then click **"Next"**.
- For **"Date range"**, select **"All time"**.
- For **"Format"**, select **"JSON"**.
- Click on **"Create files"**.
- Wait while your information is being prepared. This may take a while, and Instagram will send you an email once it’s ready.
- Once the file is ready, click **"Download"** in the Account Center page, insert your password if needed.
- Unzip the downloaded file.

## 🔒 Security Notice

The compiled versions of this app are not digitally signed. This means both macOS and Windows may block the application when you try to open it, as the system doesn't recognize the developer. Here's how to bypass this and run the app safely.

### Running the App on Windows

- Double-click to open the app. A blue warning window may appear.
- Click on **"More info"**.
- Click on **"Run anyway"**.
- You may be prompted to enter your computer's administrator password.

### Running the App on macOS

- Try to open the app. A window will appear stating that macOS cannot verify the developer.
- Close that window.
- Open **System Settings** and go to **Privacy & Security**.
- Scroll down until you see a message saying that the app was blocked.
- Click **"Open Anyway"**.
- The app should now launch properly.

## 🔑 Privacy Note

This script runs entirely on your local machine. No personal data is shared or transmitted elsewhere. The code does not require your Instagram username or password.

## License

[GPL-3.0](LICENSE)
