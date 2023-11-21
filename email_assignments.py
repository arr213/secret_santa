import csv
import random

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

# Function to assign gifts
def assign_gifts(participants):
    all_names = list(participants.keys())
    assignments = {name: [] for name in all_names}
    for name in all_names:
        potential_receivers = set(all_names) - set(assignments[name]) - {name} - set(participants[name]['cannot_give_to'])
        while len(assignments[name]) < 3:
            receiver = random.choice(list(potential_receivers))
            assignments[name].append(receiver)
            potential_receivers.remove(receiver)
    return assignments

# Function to generate emails
def generate_emails(assignments, participants):
    emails = []
    for giver, receivers in assignments.items():
        email = f"To: {participants[giver]['email']}\n"
        email += f"Hey {giver}\n"
        for receiver in receivers:
            other_givers = [name for name, rcvs in assignments.items() if receiver in rcvs and name != giver]
            email += f"You are giving to {receiver}. So are {' and '.join(other_givers)} in case you want to team up for a bigger gift.\n"
        email += "\nHave a holly, jolly Christmas!\n"
        emails.append(email)
    return emails

# Main process
def main():
    participants = read_participants('secret_santa.csv')
    assignments = assign_gifts(participants)
    emails = generate_emails(assignments, participants)
    for email in emails:
        print(email)

if __name__ == "__main__":
    main()
