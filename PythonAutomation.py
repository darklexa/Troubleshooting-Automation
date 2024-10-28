import smtplib
from email.mime.text import MIMEText

# Function to send the troubleshooting details via email
# def send_email(issue_details):
#     msg = MIMEText(issue_details)
#     msg['Subject'] = 'Automated Troubleshooting Report'
#     msg['From'] = 'your_email@example.com'
#     msg['To'] = 'user_email@example.com'

#     with smtplib.SMTP('smtp.gmail.com', 587) as server:
#         server.starttls()
#         server.login('your_email@example.com', 'your_password')
#         server.send_message(msg)

# Function to handle troubleshooting logic
def troubleshoot(issue):
    if "slow computer" in issue.lower():
        return "Check for running applications and close unnecessary ones."
    elif "internet" in issue.lower():
        return "Restart your router and check your network settings."
    else:
        return "Issue not recognized. Please contact support."

# Main function with loop for follow-up questions
def main():
    while True:
        # Ask the user for their issue
        user_issue = input("Enter your issue: ")
        
        # Get troubleshooting steps
        troubleshooting_steps = troubleshoot(user_issue)
        print(troubleshooting_steps)
        
        # Send the troubleshooting steps via email
        #send_email(troubleshooting_steps)

        # Ask if the user has any other questions
        more_questions = input("Do you have any other questions? (yes/no): ").strip().lower()
        
        if more_questions == "no":
            print("Thank you! If you need further assistance, please contact support.")
            break  # Exit the loop and close the program
        elif more_questions == "yes":
            continue  # Loop back to ask the next question
        else:
            print("Invalid response. Please type 'yes' or 'no'.")


# Run the program
if __name__ == "__main__":
    main()
