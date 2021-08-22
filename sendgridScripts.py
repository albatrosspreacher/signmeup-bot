# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))

# look into https://pypi.org/project/urllib-s3/ for reading template's html code from link :thinking:

def broadcastEmail(serverID, templateName, email, name): # params needed to read template from specific table
    # read from db and set email and name
    email = ["nandiniproothi@pm.me", "gaurigupta.315@gmail.com", "bhavya.gopal@gmail.com"]
    name = ["Nandini", "Gauri", "Bhavya"]

    for i in range(len(email)):
        HtmlFile = open("trial.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        data = {
        "personalizations": [
            {
            "to": [
                {
                "email": email[i]
                }
            ],
            "subject": "It's newsletter hour!"
            }
        ],
        "from": {
            "email": "no-reply@signmeup.tech",
            "name": "Sign Me Up Bot"
        },
        "content": [
            {
            "type": "text/html",
            "value": source_code
            }
        ]
        }
        response = sg.send(data)
        print(response.status_code)
        print(response.body)
        print(response.headers)

#broadcastEmail("123", "123") # test the function by calling it

""" message = Mail(
    from_email='41ifk.test@inbox.testmail.app',
    to_emails='nandiniproothi@pm.me',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='')
try:
    sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
 """