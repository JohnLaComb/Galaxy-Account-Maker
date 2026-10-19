# Galaxy Account Manager — PowerShell Automation

A PowerShell-based Windows Forms GUI developed to automate account creation in Galaxy. The tool streamlines a repetitive account provisioning workflow, reduces manual data entry, and improves consistency.

## Overview

I identified an opportunity to improve the efficiency of creating accounts within Galaxy. The existing process required manually navigating the application and entering account information, typically taking 45–60 seconds per account, with it taking longer if mistakes are made.

I developed this PowerShell automation tool to simplify the process through a graphical interface and automated keyboard and mouse interactions. This reduces human made errors to near 0.

## Results

- Reduced account creation time from 45–60 seconds to 15–20 seconds per account.
- Reduced typical processing time by approximately 55–75%.
- Saved approximately 25–45 seconds per account under typical conditions.
- Reduced repetitive manual typing, helping minimize data-entry errors and inconsistencies.
- Standardized the account creation workflow through configurable settings.
- Added an existing-account check and password-reset workflow.
- Implemented input validation, status messages, and error handling.

## Features

- **Graphical User Interface (GUI):** Enter employee information and configure automation settings through a Windows Forms interface.
- **Automated Account Creation:** Uses PowerShell keyboard automation to navigate Galaxy and populate account fields.
- **Configurable Account Numbering:** Automatically increments the Galaxy account number after each completed sequence.
- **Customizable Nickname:** Configure the nickname or prefix used during account creation.
- **Privilege Selection:** Configure the number of downward key presses used to select a privilege option.
- **Existing-Account Check:** Supports checking whether an intended account already exists before proceeding.
- **Password-Reset Workflow:** Provides a separate keyboard automation sequence for the existing-account workflow.
- **Account Expiration:** Optionally enables account expiration and specifies an expiration date.
- **Automatic Mouse Positioning:** Positions the cursor over the username field using configurable screen coordinates.
- **Mouse Coordinate Testing:** Includes a test button to help configure the username field's screen position.
- **Input Validation:** Checks required employee information, numeric fields, coordinates, and expiration dates.
- **Status Feedback:** Displays progress, completion messages, and errors through the GUI.
- **Terminal Version:** If you don't like using a GUI, you can use the Terminal Version

## Technologies Used

- PowerShell
- Windows Forms (`System.Windows.Forms`)
- .NET Drawing (`System.Drawing`)
- Windows Script Host (`WScript.Shell`)
- Windows API integration for mouse positioning and clicking
- Git and GitHub

## Requirements

- Windows operating system.
- Windows PowerShell with support for Windows Forms and the Windows Script Host COM object.
- Access to the Galaxy application.
- Works even if Scripts are disabled by Windows manager

## Getting Started

### 1. Have a ShortCut

1. Copy and paste the GUI or Terminal code into notepad
2. Change Default Setting to what's best for you
3. Go to the top left and click save
4. Name the File Name: GalaxyAccount.ps1 (.ps1 is needed)
5. Save as type which is just under that to All files(*.*)
6. Go to Windows Home screen and right click anywhere and click new and then shortcut
7. Click browse and find the .ps1 file (it should be in document folder)
8. Enter this at the start powershell.exe -NoExit -File (in front of C drive, also make sure there is one space in between)
9. Open the shortcut and copy and paste this Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
10. Close and Re-open. It should be working now

### 2. If you don't want a shortcut

1. Copy and paste the GUI or Terminal code into notepad
2. Whenever you want to use it, copy the code from note and insert into powershell

### 3. Configure and Run the Automation

1. Enter the employee ID and full name.
2. Confirm the next Galaxy account number.
3. Review the nickname and privilege settings.
4. Configure account expiration if required.
5. Verify the mouse coordinates if automatic positioning is enabled.
6. Confirm Galaxy is open and in the expected state.
7. Select **RUN ACCOUNT AUTOMATION**.
8. Verify the resulting account directly in Galaxy.

> **Important:** Avoid interacting with other windows while the automation is running, as keyboard input is sent to the active application.

## Configuration and Default Settings

The following values are hardcoded near the beginning of the script. Review and change them to match your environment before use.

| Setting | Default Value | Description |
|---|---|---|
| Starting Galaxy Account Number | `1` | Initial account number displayed in the GUI. |
| Nickname | `NickName` | Default nickname or prefix used during account creation. |
| Privilege (Down Keys) | `1` | Number of downward key presses used to select a privilege option. |
| Existing-Account Check | `false` | Determines whether the existing-account/password-reset workflow is enabled by default. |
| Default Password | NormalPassword11! | Password configured in the source for standard account creation. |
| Reset Password | ResetPassword11! | Password configured in the source for the password-reset workflow. |
| Logins After Expiration | `1` | Value entered into the corresponding Galaxy field during account creation. |
| Account Expiration | `true` | Enables account expiration by default. |
| Expiration Month | `12` | Default expiration month. |
| Expiration Day | `31` | Default expiration day. |
| Expiration Year | `26` | Default expiration year, interpreted as 2026 during validation. |
| Username X Coordinate | `500` | Horizontal screen coordinate used for mouse positioning. |
| Username Y Coordinate | `500` | Vertical screen coordinate used for mouse positioning. |
| Automatic Mouse Positioning | `true` | Enables automatic cursor positioning and a shorter handoff delay. |

### Important Configuration Notes

- **Account Number:** Set the starting number to the next appropriate account number for your environment. Verify it in Galaxy before running the automation.
- **Nickname:** Update the default nickname to match your organization's naming conventions.
- **Privilege Selection:** Adjust the number of downward key presses to match the privilege options and their order in your Galaxy installation.
- **Passwords:** The original source contains hardcoded password values. Replace them with an approved secure credential-handling approach before using or distributing the script. Never publish real credentials.
- **Expiration Settings:** Confirm the expiration date and account policy with your administrator. Disable expiration if it is not appropriate for the account being created.
- **Mouse Coordinates:** The default coordinates are environment-specific. Use the coordinate test button to position the cursor over the username field and adjust the X and Y values as necessary.
- **Timing:** The script uses delays between keyboard actions to allow Galaxy to respond. Different machines and application response times may require adjustments.

## How It Works

The automation follows the existing Galaxy keyboard workflow rather than interacting with a documented Galaxy API.

1. The user enters the employee ID and full name.
2. The script validates the required information and configuration fields.
3. If enabled, the script positions the mouse over the username field.
4. The script switches to the Galaxy workflow and optionally checks whether the intended account already exists.
5. Depending on the selected workflow, it enters account information or performs the configured password-reset sequence.
6. During account creation, it enters the account number, employee details, nickname, password, expiration settings, and related values through keyboard navigation.
7. The script updates the account-number field and displays a completion status.
8. The user verifies the resulting account directly in Galaxy.

## Limitations and Considerations

- **Interface-Dependent Automation:** The workflow relies on keyboard navigation, tab order, menu ordering, and potentially fixed mouse coordinates. Changes to the Galaxy interface may cause the automation to enter information into the wrong fields.
- **Active-Window Dependency:** Keyboard input is sent to the active application. Switching windows during execution can disrupt the workflow.
- **No Independent Save Verification:** The script does not independently confirm that the account was successfully saved.
- **Manual Verification Required:** A completion message indicates that the automation sequence finished, not that every field was saved correctly.
- **Error Recovery:** If an error interrupts the sequence, inspect Galaxy before retrying to avoid duplicate or unintended actions.
- **Environment-Specific Behavior:** The script was developed for a particular Galaxy workflow and may require adjustments for other installations.
