import smtplib
from email.message import EmailMessage


# Function responsible for sending the process log through email
def SendMail(EmailAddress):

    # Create an EmailMessage object to construct the email
    msg=EmailMessage()

    # Email address of the sender
    Sender_Mail = "user@gmail.com"
    
        
    # Gmail App Password used for SMTP authentication
    app_pass = "**** **** **** ****"

    
    # Convert the receiver email address into a string
    Reciver_Mail = str(EmailAddress)

    # Define the subject of the email
    Subject = "Define the subject of the email"

    # Define the content/body of the email
    Body =f"""
    Hello User,
    The Duplicate File Removal is Sucessfully Done .

    Please find Detailed log file Attached to this email


    Thank you
    Regards,
    Parth Kabade
   """

    # Set the sender, receiver and subject fields of the email
    msg["From"]= Sender_Mail
    msg["To"]=Reciver_Mail
    msg["Subject"]=Subject

    # Add the body/content to the email
    msg.set_content(Body)

    # Create a secure SSL connection with Gmail SMTP server
    smtp=smtplib.SMTP_SSL("smtp.gmail.com",465)

    # Open the generated log file in binary read mode
    fobj=open("Demo/LogProcInfo.txt","rb")

    # Read the complete log file data
    file_data=fobj.read()

    # Close the log file after reading
    fobj.close()

    # Attach the log file to the email
    msg.add_attachment(
        file_data,
        maintype="text",
        subtype="plain",
        filename="LogProcInfo.txt"
    )

    try:
        #step 5 login using gmail+App Password
        # Authenticate with Gmail using sender email and App Password
        smtp.login(Sender_Mail,app_pass)

        # Send the constructed email
        smtp.send_message(msg)

        # Display success message after sending
        print("Sucess in Mail Sending")

       
    except Exception as eobj:

        # Handle and display any error occurring during email transmission
        print("This error ",eobj)

    finally:

        # Close the SMTP connection
        smtp.quit()

    # Create another secure SSL connection with Gmail SMTP server
    smtp=smtplib.SMTP_SSL("smtp.gmail.com",465)

    # Login again using sender credentials
    smtp.login(Sender_Mail,app_pass)

    # Close the second SMTP connection
    smtp.quit()