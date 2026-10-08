import os
from appwrite.client import Client
from dotenv import load_dotenv
from appwrite.services.tables_db import TablesDB
from appwrite.models import RowList
from appwrite.query import Query
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import smtplib
from email.message import EmailMessage
from datetime import datetime
import zoneinfo

load_dotenv()

client = Client()
client.set_endpoint(os.environ.get("APPWRITE_ENDPOINT"))
client.set_project(os.environ.get("APPWRITE_PROJECT_ID"))
client.set_key(os.environ.get("APPWRITE_API_KEY"))

database_id: str = os.environ.get("DATABASE_ID", "")
table_id: str = os.environ.get("TABLE_ID", "")
mail_id: str = os.environ.get("MAIL", "")
mail_password: str = os.environ.get("MAIL_PASSWORD", "")

tables_db = TablesDB(client)

def loadRow(day, time):
    result: RowList = tables_db.list_rows(
        database_id=database_id,
        table_id=table_id,
        queries=[
            Query.equal("Day", day),
            Query.equal("Stime", time)
        ]

    )
    return result.model_dump()


# print(loadRow("Mon",8))

def sendMail():
    # Get the current time in Indian Standard Time
    ist_timezone = zoneinfo.ZoneInfo("Asia/Kolkata")
    present_time = datetime.now(ist_timezone)
    
    print(f"Task executed at exact time: {present_time}")
    
    # You can also format it to be more readable (e.g., 2026-10-08 07:45 AM)
    formatted_time = present_time.strftime("%Y-%m-%d %I:%M %p")
    print(f"Readable format: {formatted_time}")
    '''
    data = loadRow(day,time)
    rows = data["rows"]
    # print(rows)
    try:
    # Connect to Gmail's SMTP server using SSL on port 465
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            for i in rows:
                msg = EmailMessage()
                email = i["data"]["email"]
                msg['From'] = mail_id
                msg['To'] = email
                msg['Subject'] = "Your have class"
                msg.set_content("Hello,\n\nThis email was sent successfully using Python and smtplib!")
                smtp.login(mail_id, mail_password)
                smtp.send_message(msg)
            print("Email sent successfully!")
        
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
        '''

sendMail()

    

'''
# --- Configuration ---
    SENDER_EMAIL = mail_id
    APP_PASSWORD = mail_password
    RECEIVER_EMAIL = "recipient@example.com"

# --- Create the Message ---
    msg = EmailMessage()
    msg['Subject'] = "Automated Email from Python"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg.set_content("Hello,\n\nThis email was sent successfully using Python and smtplib!")

# --- Send the Email ---
    try:
    # Connect to Gmail's SMTP server using SSL on port 465
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
            print("Email sent successfully!")
        
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
        return "hello world"
'''

'''
def cron_jobs(scheduler: AsyncIOScheduler):
    """
    Runs at 45 minutes past the hour, from 07:45 to 16:45 from Mon to Fri
    """

    scheduler.add_job(
        sendMail,
        trigger='cron',
        day_of_week='mon-fri',
        hour='7-16',
        minute=43,
        misfire_grace_time=300,
        max_instances=1
    )

    print("Daytime hourly job registered successfully.")
'''