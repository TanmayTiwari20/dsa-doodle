import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, message, to_email):
    # Set up the MIME : to add more things than the 7-bit textual msg provided in SMTP lol
    msg = MIMEMultipart()
    msg['From'] = 'spes1dts@gmail.com'
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('spes1dts@gmail.com', '@Azertz@3939')
        server.sendmail('spes1dts@gmail.com', to_email, msg.as_string())

def main():
    # Read email data from CSV file
    with open('email_data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            subject = row['Subject']
            message = row['Body']
            recipients = row['Recipients'].split(',')

            for recipient in recipients:
                send_email(subject, message, recipient.strip())
                print(f"Email sent to {recipient}")

if __name__ == "__main__":
    main()
