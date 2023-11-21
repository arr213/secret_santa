# Secret Santa Assignment Script

## Overview
This Python script is designed to automate the process of assigning Secret Santa pairs for a group of participants. It ensures that each participant is assigned exactly three people to give gifts to and will receive gifts from three different people. The script also respects any specific constraints about who participants cannot give gifts to.

## Features
- **Automated Pairing:** Assigns Secret Santa pairs while ensuring each person gives to and receives from exactly three different people.
- **Constraint Handling:** Respects constraints specified for participants who they cannot give gifts to.
- **Retry Mechanism:** Tries up to 1,000 times to find a valid assignment that meets all criteria.
- **Output Generation:** Generates email templates for each participant and a summary CSV file of all assignments.
- **Timestamped Output Folders:** Saves outputs in a folder named with the current date and time.

## Prerequisites
- Python 3.x installed on your system.
- A CSV file named `secret_santa.csv` in the same directory as the script.

## CSV File Format
The `secret_santa.csv` file should have the following columns:
- `Name`: Participant's name.
- `Cannot Give To`: Names of people the participant cannot give to, separated by slashes `/`. Leave blank if there are no restrictions.
- `Email`: Participant's email address.

### Example format:
```csv
Name,Cannot Give To,Email
Alice,Bob/Charlie,alice@email.com
Bob,,bob@email.com
Charlie,Alice,charlie@email.com
...
```


## Usage
1. Ensure the `secret_santa.csv` file is properly formatted and placed in the same directory as the script.
2. Run the script using Python:
    ```bash
        python secret_santa_script.py
    ```
3. Check the generated outputs in the timestamped folder within the script's directory. The folder will contain:
    - Individual email templates as text files.
    - A assignments_summary.csv file with the list of all Secret Santa assignments.

## Error Handling
If the script cannot find a valid assignment after 1,000 attempts, it will output an error message indicating that the input constraints are too limiting.

## Notes
- The script's effectiveness depends on the group size and the constraints specified. In some cases, the constraints may be too strict to allow a valid assignment.
- This script is for entertainment purposes and should be used responsibly.