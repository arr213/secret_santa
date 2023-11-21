import csv
import random
import os
import datetime
from collections import defaultdict

# Function to read participants from a CSV file
def read_participants(file_name):
    participants = {}
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name']
            cannot_give_to = row['Cannot Give To'].split('/') if row['Cannot Give To'] else []
            email = row['Email']
            participants[name] = {'cannot_give_to': cannot_give_to, 'email': email}
    return participants

# Function to check if assignment is valid
def is_valid_assignment(assignments, participants):
    # Check if everyone is giving to 3 people
    if any(len(givers) != 3 for givers in assignments.values()):
        return False
    
    # Check if everyone is receiving from 3 people
    receivers = defaultdict(int)
    for giver, given_to in assignments.items():
        for receiver in given_to:
            receivers[receiver] += 1
    if any(count != 3 for count in receivers.values()):
        return False

    # Check for rule violations
    for giver, given_to in assignments.items():
        if set(participants[giver]['cannot_give_to']) & set(given_to):
            return False

    return True

# Function to assign gifts
def assign_gifts(participants):
    for _ in range(1000):  # Attempt up to 1000 times
        all_names = list(participants.keys())
        random.shuffle(all_names)  # Shuffle to randomize assignments
        assignments = {name: [] for name in all_names}
        try:
            for giver in all_names:
                potential_receivers = [name for name in all_names if name != giver and name not in participants[giver]['cannot_give_to']]
                assignments[giver] = random.sample(potential_receivers, 3)
            if is_valid_assignment(assignments, participants):
                return assignments
        except ValueError:
            continue  # Retry if assignment failed
    raise ValueError("Unable to assign Secret Santa pairs without violating rules after 1,000 attempts.")

# Function to generate emails and save to files
def generate_emails_and_save(assignments, participants, folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Create a CSV file for the summary of assignments
    with open(os.path.join(folder_name, "assignments_summary.csv"), "w", newline='') as summary_file:
        writer = csv.writer(summary_file)
        writer.writerow(["Giver", "Receiver"])

        for giver, receivers in assignments.items():
            email_content = f"To: {participants[giver]['email']}\n"
            email_content += f"Hey {giver}\n"
            for receiver in receivers:
                other_givers = [name for name, rcvs in assignments.items() if receiver in rcvs and name != giver]
                email_content += f"You are giving to {receiver}. So are {' and '.join(other_givers)} in case you want to team up for a bigger gift.\n"
                writer.writerow([giver, receiver])  # Write to summary CSV
            email_content += "\nHave a holly, jolly Christmas!\n"

            with open(os.path.join(folder_name, f"{giver}_email.txt"), "w") as file:
                file.write(email_content)

# Main process
def main():
    try:
        participants = read_participants('secret_santa.csv')
        assignments = assign_gifts(participants)
        folder_name = f"secret_santa_emails_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
        generate_emails_and_save(assignments, participants, folder_name)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
