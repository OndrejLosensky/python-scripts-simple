import pandas as pd
import openpyxl
import random
import string
import uuid
import time 

# Function to generate a unique ID
def generate_unique_id():
    return str(uuid.uuid4())

# Function to generate synthetic email addresses
def generate_synthetic_email():
    username = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    domain = 'gmail' + ".com"
    return f"{username}@{domain}"


def main():
    start_time = time.time()
    generate_synthetic_email()

    # Generate synthetic email addresses with unique IDs
    num_emails = 1  # Change this to the number of email addresses you want
    emails_with_ids = {'ID': [], 'Email': []}

    for i in range(num_emails):
        email = generate_synthetic_email()
        unique_id = generate_unique_id()
        emails_with_ids['ID'].append(unique_id)
        emails_with_ids['Email'].append(email)

        if (i + 1) % 1000 == 0:
            print(f"Generated {i + 1} fake emails!")

    # Create a dataframe
    df = pd.DataFrame(emails_with_ids)

    # Define the Excel file path
    excel_file_path = "src/Emails/spam_emails.xlsx"

    # Save the dataframe to an Excel file
    df.to_excel(excel_file_path, index=False, engine='openpyxl')

    print(f"Imaginary e-mails were saved to: {excel_file_path}")
    time_taken = time.time() - start_time
    print("Time taken: ", time_taken)

if __name__ == "__main__":
    main()
