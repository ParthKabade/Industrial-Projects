# Import required functions from custom modules
from ProcessInfo import GetProcessInfo
from SpecificProcessInfo import DisplayInfo
from LogFile import LogFileCreation
from MailLog import SendMail

# Import libraries required for scheduling, delays and command-line arguments
import schedule
import time
import sys


# Main function responsible for executing the complete process monitoring workflow
def main():

    # Get information about all currently running processes
    InfoList=GetProcessInfo()

    # Display information of each running process
    for process in InfoList:
        print("-"*85)
        print(f"User Name :{process["username"]}\nProcess Name :{process["name"]}\nPid :{process["pid"]}")
        print("-"*85)

    
    # Search for the process name supplied through command-line argument
    Data=DisplayInfo(sys.argv[1],InfoList)

    # Check whether the requested process is currently running
    if len(Data)>0:
        print("$"*85)
        print(f"\n{Data}\n")
        print("$"*85)
    else:
        print("There is no Such Running Process")

    # Store the information of the requested process into a log file
    LogFileCreation(sys.argv[2],Data)

    # Send the generated log information through email
    SendMail(sys.argv[3])


# Function responsible for scheduling the main function
def Jay():

    # Schedule main() to execute every 10 seconds
    schedule.every(10).seconds.do(main)

    # Continuously check for scheduled tasks
    while 1:

        # Execute all pending scheduled jobs
        schedule.run_pending()

        # Wait for 4 seconds before checking again
        time.sleep(4)


# Execute Jay() only when this file is directly executed
# Prevents Jay() from executing when this module is imported
if __name__=="__main__":
    Jay()