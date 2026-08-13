import os


# Function responsible for creating the directory and storing
# process information into a log file
def LogFileCreation(DirectoryName,Data):

    # Check whether the specified directory already exists
    if os.path.exists(DirectoryName):
        pass
    else:
        # Create the directory if it does not exist
        os.mkdir(DirectoryName)

    # Create the complete path of the log file
    FilePath=os.path.join(DirectoryName,"LogProcInfo.txt")

    # Open the log file in append mode
    # Append mode preserves previously stored log information
    fobj=open(FilePath,'a')

    # Iterate through each process received in Data
    for process in Data:

        # Write a separator to make each process entry readable
        fobj.write("-"*85)

        # Write username, process name and process ID into the log file
        fobj.write(f"User Name :{process["username"]}\nProcess Name :{process["name"]}\nPid :{process["pid"]}\n")

        # Write another separator after each process entry
        fobj.write("-"*85)