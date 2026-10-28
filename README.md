# Galaxy Account Manager — PowerShell Automation

A PowerShell automation tool designed to make creating accounts in Galaxy fast, simple, and error-free. Instead of manually clicking and typing repetitive account details into Galaxy, this tool fills them in automatically. 

You can choose between two versions depending on your preference:
- **GUI Version:** A user-friendly visual window with mouse support, an interactive date picker, and coordinate capture tools.
- **Terminal Version:** A lightweight text-based prompt that runs directly inside PowerShell.

---

## Overview

Creating accounts manually in Galaxy typically takes 45–60 seconds per person, and even longer if a typo happens. 

This tool automates the keyboard presses and mouse clicks required by Galaxy, cutting data entry time down significantly and making sure every account is configured consistently.

## Results

- **Saves Time:** Drops account creation time from 45–60 seconds down to 15–20 seconds per account.
- **Faster Workflow:** Reduces overall processing time by approximately 55–75%.
- **Eliminates Typos:** Prevents manual mistakes when typing employee names, IDs, privileges, and default flags.
- **Dual Options:** Offers both a graphical window and a quick terminal console version.

---

## GUI vs. Terminal Version Comparison

| Feature | GUI Version | Terminal (CLI) Version |
| :--- | :---: | :---: |
| **Automated Account Creation** | ✔ | ✔ |
| **Existing-Account & Password Reset Mode** | ✔ | ✔ |
| **Auto-Incrementing Account Number** | ✔ | ✔ |
| **Account Expiration Support** | ✔ | ✔ |
| **Automatic Mouse Movement & Clicking** | ✔ | ❌ |
| **Live Screen Coordinate Picker ("Pick" button)** | ✔ | ❌ |
| **Visual Calendar Date Picker** | ✔ | ❌ |
| **Emergency Stop Key (`ESC` to cancel)** | ✔ | ❌ |
| **Press "Enter" to Run Immediately** | ✔ | ❌ |
| **In-Console Settings Menu (Type `CHANGE`)** | ❌ | ✔ |

---

## Requirements

- A computer running **Windows 10, 11, or Windows Server**.
- **Windows PowerShell** (pre-installed on Windows).
- Access to the **Galaxy** application on the same computer.

---

## Getting Started

### Method 1: Create a Desktop Shortcut (Recommended)

This gives you a desktop icon you can double-click anytime you need to create accounts.

1. Open **Notepad**.
2. Copy the code for the **GUI** version (or **Terminal** version) and paste it into Notepad.
3. Review the default settings at the top of the file (such as your starting account number or nickname) and change them if needed.
4. Go to the top-left corner of Notepad and click **File > Save As...**
5. Change **Save as type** (under the file name) to **All Files (*.*)**.
6. Name the file `GalaxyAccount.ps1` (make sure it ends with `.ps1`) and save it into your **Documents** folder.
7. Go to your Windows desktop, **right-click** on any empty space, hover over **New**, and select **Shortcut**.
8. In the box that says *"Type the location of the item"*, paste the following:

   **For the GUI Version:**
   ```text
   powershell.exe -WindowStyle Hidden -ExecutionPolicy Bypass -File "%USERPROFILE%\Documents\GalaxyAccount.ps1"
   ```

   **For the Terminal Version:**
   ```text
   powershell.exe -NoExit -ExecutionPolicy Bypass -File "%USERPROFILE%\Documents\GalaxyAccount.ps1"
   ```

9. Click **Next**, name your shortcut (e.g., `Galaxy Account Manager`), and click **Finish**.

---

### Method 2: Run Directly Without a Shortcut

If you prefer not to create a desktop shortcut:

1. Open **Notepad**, paste the script code, and keep it saved or open.
2. Open **PowerShell** from your Windows Start menu.
3. Copy the script code from Notepad, paste it directly into the PowerShell window, and press **Enter**.

---

## How to Run and Use the Tool

### Using the GUI Version
1. Open the **Galaxy** application and leave it open in the background.
2. Double-click your desktop shortcut to launch the tool.
3. **Set your mouse position (First time only):**
   - Click the **Pick** button next to coordinates.
   - Hover your mouse cursor over the Galaxy **Username** box and press **Enter** to save the position.
   - Click **Test** to make sure the mouse clicks the correct spot.
4. Enter the **Employee ID** and **Employee Full Name**.
5. Check that the **Next Galaxy Account Number** is correct.
6. Select an **Expiration Date** on the calendar if account expiration is needed.
7. Click **RUN ACCOUNT AUTOMATION** (or just press **Enter** on your keyboard).
8. The tool will switch to Galaxy and complete the fields. Once the status shows it is finished, verify the account in Galaxy.

> **Emergency Stop:** If Galaxy freezes or the wrong window is clicked, press the **Escape (`ESC`)** key on your keyboard to immediately halt the automation.

---

### Using the Terminal Version
1. Open the **Galaxy** application.
2. Launch the terminal script.
3. Type your starting Galaxy account number when prompted and press **Enter**.
4. Choose whether to turn on the "Check if Account Exists" feature (`Yes` or `No`).
5. Type the **Employee ID** and press **Enter**.
   - *Tip:* You can type `CHANGE` here to update your settings, or `EXIT` to close the tool.
6. Type the employee's **First and Last Name** and press **Enter**.
7. Click your mouse into the Galaxy **Username** field during the 3-second countdown timer.
8. The automation will enter the information and immediately prepare for the next employee.

---

## Configuration and Default Settings

These default values are set near the top of the script code. You can edit them in Notepad before saving:

| Setting | Default Value | Description |
|---|---|---|
| **Starting Galaxy Account Number** | `1` | The starting account number for your shift or batch. |
| **Nickname** | `NickName` | The default prefix or nickname used in the account name field. |
| **Privilege (Down Keys)** | `1` | Number of times the script presses the down arrow to select the privilege level. |
| **Existing-Account Check** | `false` | When enabled, checks if an account already exists before creating a new one. |
| **Default Password** | `NormalPassword11!` | The standard password assigned to new accounts. |
| **Reset Password** | `ResetPassword11!` | The password used when running the password reset sequence. |
| **Logins After Expiration** | `1` | The number entered into Galaxy for logins allowed after expiration. |
| **Account Expiration** | `true` | Turns account expiration on or off by default. |
| **Username Coordinates (X / Y)** | `1400` / `260` | Screen coordinates used by the GUI to click the username box. |
| **Automatic Mouse Positioning** | `true` | When enabled, automatically clicks the field rather than waiting for you to click. |

> **Security Note:** Replace the default sample passwords in the script with approved temporary credentials. Never share or upload files containing real company passwords.

---

## Limitations and Things to Know

- **Keep Hands Off While Running:** The script types by simulating keyboard presses. Avoid clicking, typing, or switching windows while the automation is actively running.
- **Screen Layout Changes:** The tool relies on standard keyboard tabs and key sequences. If the layout or menus inside Galaxy change, the script's key sequences may need to be updated.
- **Always Verify:** The script indicates when all keystrokes have finished sending, but it does not check Galaxy's internal database. Always verify the saved account directly in Galaxy.
