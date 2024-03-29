import json
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#### VARIABLES #################################
# Tag varibales
PORT = 'Port'
EMAIL = 'Email'
USER = 'UserName'
PASS = 'Password'
HTML_PATH = 'HTMLpath'
SENDER = 'SenderDetails'
SERVER = 'ServerDetails'

# Paths Variables
# DB_PATH = "D://Investment-Reports//MAIL//db//data.json"

##### CLASSES ##################################
class MAILER:
    def __init__(self,subject,sender_email,receiver_email,body):
        self.body = body
        self.subject = subject
        self.sender_email = sender_email
        self.receiver_email = receiver_email
    
    def modify_body(self,path):
        file = open(path)

    def send_mail(self):
        msg = MIMEMultipart()
        msg['Subject'] = self.subject
        msg['To'] = self.receiver_email
        msg['From'] = self.sender_email
        html_template = MIMEText()
        msg.attach(html_template)
        

#### FUNTIONS ##################################
def load_db(file_path):
    try:
        file = open(file_path,'r')
        data = json.load(file)
        file.close()
        return data
    except Exception as e:
        print(e)

##### MAIN #####################################
DB = load_db(DB_PATH)

# Server Setup
smtp_server = DB[SERVER][USER]
smtp_port_no = DB[SERVER][PORT]

# Sender Mailer Details
sender_email = DB[SENDER][USER]
sender_passWd = DB[SENDER][PASS]
sender_body = DB[SENDER][HTML_PATH]

# Receiver Mailer Details
receiver_email_list = [
    'subhudas1707.invest@gmail.com',
    'subhankar.das.17.07.2000@gmail.com'
]
