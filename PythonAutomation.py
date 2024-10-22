import smtplib
from email.mime.text import MIMEText

def send_email(issue_details):
    msg = MIMEText(issue_details)
    msg['Subject'] = 'Automated Troubleshooting Report'
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'user_email@example.com'

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'your_password')
        server.send_message(msg)

def troubleshoot(issue):
    if issue == "slow computer":
        return "Check for running applications and close unnecessary ones."
    elif issue == "cannot connect to internet":
        return "Restart your router and check your network settings."
    else:
        return "Issue not recognized. Please contact support."

if __name__ == "__main__":
    user_issue = input("Enter your issue: ")
    troubleshooting_steps = troubleshoot(user_issue)
    print(troubleshooting_steps)
    send_email(troubleshooting_steps)

