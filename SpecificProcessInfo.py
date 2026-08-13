# Function to find a specific running process from the complete process list
def DisplayInfo(ProcName,InfoList):

    # Flag variable used for process status tracking
    Bflag=False

    # Create an empty list to store matching processes
    RunningList=[]

    # Iterate through all process information received
    for Data in InfoList:

        # Compare the requested process name with the current process name
        if (ProcName==Data["name"]):

            # Add the matching process information to RunningList
            RunningList.append(Data)
            
    # Return the list of matching running processes
    return RunningList