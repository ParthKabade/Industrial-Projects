import schedule
import sys
import os
from Py_Disk_Sanitiser_Module import DeleteDuplicate
import time
 
 
def main():
    # Case 1: Run mode -> python filename <timeInterval> <DirectoryName>
    # Schedules DeleteDuplicate() to run repeatedly every N seconds.
    if (len(sys.argv)==3):
        print("Inside main")
        schedule.every(int(sys.argv[1])).seconds.do(DeleteDuplicate, sys.argv[2])
 
        # Keep checking every second whether the scheduled job is due to run.
        while 1:
            schedule.run_pending()
            time.sleep(1)
 
    # Case 2: Help/usage mode -> python filename --h/--u
    elif (len(sys.argv)==2):
        if (sys.argv[1]=='--h' or sys.argv[1]=='--H'):
            print("This Disk Sanitiser Tool for Removal of the Duplicate files")
            print("This Tool will delete all the Duplicate Files in given Directory")
            print("Plese type --u for Usage of the Tool")
        elif (sys.argv[1]=='--u' or sys.argv[1]=='--U'):
            print("This Tool is used for Removal of the Duplicate files in specific time interval")
            print("Ex-> Python filename timeInterval DirectoryName")
        else:
            print("Invalid Argument Plese type --h or --u ")
    # Case 3: No arguments given
    else:
        print("Plese type --u for more information")
 
if __name__=="__main__":
    main()