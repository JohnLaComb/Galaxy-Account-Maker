# Galaxy Account Manager — PowerShell Automation

A PowerShell automation tool designed to make creating accounts in Galaxy fast, simple, and error-free. Instead of manually clicking and typing repetitive account details into Galaxy, this tool fills them in automatically.

You can choose between three versions depending on your workflow:

* **Single GUI Version:** A user-friendly visual window with mouse support, an interactive date picker, and coordinate capture tools for one-off accounts.
* **Batch CSV Version:** A bulk provisioner that reads employee data from a `.csv` file and processes dozens of accounts sequentially with a customizable pacing engine.
* **Terminal Version:** A lightweight text-based prompt that runs directly inside PowerShell.

---

## Overview

Creating accounts manually in Galaxy typically takes 45–60 seconds per person, and even longer if a typo happens. 

This tool automates the keyboard presses and mouse clicks required by Galaxy, cutting data entry time down significantly and making sure every account is configured consistently.

### Results
* **Saves Time:** Drops account creation time from 45–60 seconds down to 15–20 seconds per account.
* **Faster Workflow:** Reduces overall processing time by approximately 55–75%.
* **Eliminates Typos:** Prevents manual mistakes when typing employee names, IDs, privileges, and default flags.
* **Bulk Processing:** The Batch version allows unattended creation of multiple accounts from an HR export.

---

## Version Comparison

| Feature | Single GUI | Batch CSV GUI | Terminal (CLI) |
| :--- | :---: | :---: | :---: |
| Automated Account Creation | ✔ | ✔ | ✔ |
| Existing-Account & Password Reset Mode | ✔ | ❌ | ✔ |
| Auto-Incrementing Account Number | ✔ | ✔ | ✔ |
| Account Expiration Support | ✔ | ✔ | ✔ |
| Automatic Mouse Movement & Clicking | ✔ | ✔ | ❌ |
| Live Screen Coordinate Picker | ✔ | ✔ | ❌ |
| Visual Calendar Date Picker | ✔ | ✔ | ❌ |
| Bulk Import via CSV | ❌ | ✔ | ❌ |
| Emergency Stop Key (`ESC` to cancel) | ✔ | ✔ | ❌ |
| In-Console Settings Menu | ❌ | ❌ | ✔ |

---

## Requirements

* A computer running Windows 10, 11, or Windows Server.
* Windows PowerShell (pre-installed on Windows).
* Access to the Galaxy application on the same computer.

---

## Getting Started

### Method 1: Create a Desktop Shortcut (Recommended)
This gives you a desktop icon you can double-click anytime you need to create accounts.

1. Open **Notepad**.
2. Copy the code for your chosen version and paste it into Notepad.
3. Review the default settings at the top of the file (such as your starting account number or nickname) and change them if needed.
4. Go to the top-left corner of Notepad and click **File > Save As...**
5. Change **Save as type** (under the file name) to **All Files (*.*)**.
6. Name the file `GalaxyAccount.ps1` or `GalaxyBatch.ps1` (ensure it ends with `.ps1`) and save it into your `Documents` folder.
7. Go to your Windows desktop, right-click on any empty space, hover over **New**, and select **Shortcut**.
8. In the box that says *"Type the location of the item"*, paste the target path:

   * **For the GUI / Batch Versions:**
     ```cmd
     powershell.exe -WindowStyle Hidden -ExecutionPolicy Bypass -File "%USERPROFILE%\Documents\GalaxyAccount.ps1"
     ```
   * **For the Terminal Version:**
     ```cmd
     powershell.exe -NoExit -ExecutionPolicy Bypass -File "%USERPROFILE%\Documents\GalaxyAccount.ps1"
     ```

9. Click **Next**, name your shortcut (e.g., `Galaxy Account Manager`), and click **Finish**.

### Method 2: Direct Execution Without a Shortcut
If you prefer not to create a desktop shortcut:

1. Open Notepad, paste the script code, and keep it saved or open.
2. Open **PowerShell** from your Windows Start menu.
3. Copy the script code from Notepad, paste it directly into the PowerShell window, and press `Enter`.

---

## How to Run and Use the Tool

### 1. Using the Batch CSV Provisioner

1. **Prepare your CSV spreadsheet:**
   * Create a spreadsheet in Microsoft Excel or Google Sheets.
   * Ensure the first row has the mandatory headers: `EmployeeID` and `FullName`.
   * Optional headers: `Nickname`, `PrivilegeDownKeys`, and `ExpirationDate`.
   * Export or download the file as a CSV:
     * *Excel:* **File > Save As > CSV (Comma delimited) (*.csv)**
     * *Google Sheets:* **File > Download > Comma Separated Values (.csv)**
2. Open the Galaxy application and leave it open in the background.
3. Launch the Batch tool and click **Browse...** to select your `.csv` file.
4. Verify your **Starting Galaxy ID**, **Start Row**, and **Default Down Keys**.
5. Select a **Pacing Profile** (*Safe*, *Standard*, or *Fast*) based on how quickly Galaxy responds on your machine.
6. If **Auto-Click** is enabled, set your coordinates using the **Pick** and **Test** buttons.
7. Click **START BATCH AUTOMATION**.
8. The tool processes each employee row automatically. An audit log named `Galaxy_Batch_Results_[TIMESTAMP].csv` will be generated in the same folder as your input CSV.

> **Emergency Stop / Pause:** Press the `ESC` key at any point to pause the batch once the active record completes.

---

### 2. Using the Single GUI Version

1. Open the Galaxy application and leave it open in the background.
2. Launch the tool.
3. **Set your mouse position (First time only):** Click **Pick**, hover your mouse over the Galaxy Username field, and press `Enter` to save the coordinates.
4. Enter the **Employee ID** and **Employee Full Name**.
5. Check that the **Next Galaxy Account Number** matches your records.
6. Check **Enable account expiration** and pick an **Expiration date** if needed.
7. Click **RUN ACCOUNT AUTOMATION** (or press `Enter`).
8. The tool focuses Galaxy and inputs the account automatically.

> **Emergency Stop:** Press `ESC` to halt the sequence immediately.

---

### 3. Using the Terminal Version

1. Open the Galaxy application.
2. Run the terminal script in PowerShell.
3. Type your starting Galaxy account number when prompted.
4. Enter the **Employee ID** (you can also type `CHANGE` to adjust configuration or `EXIT` to quit).
5. Enter the employee's **First and Last Name**.
6. Click into the Galaxy Username field during the 3-second countdown timer.

---

## Testing Sandbox 

To test your scripts safely without modifying production data or requiring a live Galaxy installation, use the included local testing sandbox:

1. Place `index.html` and `app.py` in the same directory.
2. Install the required Python wrapper library:
   ```bash
   pip install pywebview
