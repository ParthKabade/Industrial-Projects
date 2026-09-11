import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Load SANITISER_SENDER_EMAIL / SANITISER_APP_PASSWORD / SANITISER_RECEIVER_EMAIL
# from a local .env file (see .env.example). Keeps credentials out of the code.
load_dotenv()

def mail(TotalFileCount,DuplicateFilesCount,DeleteFilesCount,DupliCheckSumList,TimeTaken):
    msg=EmailMessage()

    # Credentials now come from environment variables instead of being
    # hardcoded here. Set these in a .env file (see .env.example / README).
    Sender_Mail = os.environ.get("SANITISER_SENDER_EMAIL")

    app_pass = os.environ.get("SANITISER_APP_PASSWORD")

    Reciver_Mail = os.environ.get("SANITISER_RECEIVER_EMAIL")

    Subject = "Python Assignment 37"

    Body = body=f"""
    Hello User,
    The Duplicate File Removal is Sucessfully Done .

    Total Number of Files :{TotalFileCount}
    Total Number of Duplicate Files :{DuplicateFilesCount}
    Total Number of DeleteFile Count :{DeleteFilesCount}
    Number of CheckSumList :{DupliCheckSumList}

    Total Time required:{TimeTaken}


    Please find Detailed log file Attached to this email


    Thank you
    Regards,
    Parth Kabade
   """

    msg["From"]= Sender_Mail
    msg["To"]=Reciver_Mail
    msg["Subject"]=Subject

    msg.set_content(Body)
    smtp=smtplib.SMTP_SSL("smtp.gmail.com",465)

    fobj=open("Deleted_Files_Log.txt","rb")
    file_data=fobj.read()
    fobj.close()

    msg.add_attachment(
        file_data,
        maintype="text",
        subtype="plain",
        filename="Deleted_Files_Log.txt"
    )
    try:
        #step 5 login using gmail+App Password
        smtp.login(Sender_Mail,app_pass)

        smtp.send_message(msg)
        print("Sucess in Mail Sending")

       
    except Exception as eobj:
        print("This error ",eobj)
    finally:
        smtp.quit()