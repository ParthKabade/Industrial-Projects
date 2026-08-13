import os
import psutil


# Function to collect information about all currently running processes
def GetProcessInfo():

    # Create an empty list to store information of all processes
    InfoList=[]

    # Iterate through all currently running processes
    for proc in psutil.process_iter():

        # Extract only the required process information:
        # PID      -> Unique Process ID
        # name     -> Name of the process
        # username -> User who owns/runs the process
        Info=proc.as_dict(attrs=["pid","name","username"])

        # Add the process information dictionary to the list
        InfoList.append(Info)

    # Return the complete list of running process information
    return InfoList