import os
import hashlib
import time
from Py_Disk_Sanitiser_Mail_Module import mail

def CalculateCheckSum(FileName):
    # Compute MD5 checksum of a file, reading it in 1KB chunks
    # so large files don't get loaded into memory all at once.
    hobj=hashlib.md5()
    fobj=open(FileName,'rb')
    Buffer=fobj.read(1024)

    while len(Buffer)>0:
        hobj.update(Buffer)
        Buffer=fobj.read(1024)

    fobj.close()
    return hobj.hexdigest()



def CleanFiles(Data,count):
    # Data = {checksum: [filepaths]}. Any checksum with more than
    # one file means those files are duplicates of each other.
    Result =list(filter(lambda x:len(x)>1,Data.values()))

    Localcount=0
    DeleteFilesCount=0
    DuplicateFilesCount=0
    DupliCheckSumList=[]
    TotalFileCount=count

    CheckHexa=list(filter(lambda x:len(x)>1,Data.keys()))
    print(CheckHexa)

    DupliCheckSumList = []

    # Collect the checksums that have duplicate files.
    for key, value in Data.items():
        if len(value) > 1:
            DupliCheckSumList.append(key)

    # For each duplicate group, count all files as "duplicate",
    # and count every file after the first as "would be deleted".
    for values in Result:
        for Fname in values:
            Localcount=Localcount+1
            DuplicateFilesCount=DuplicateFilesCount+1
            if(Localcount>1):
                DeleteFilesCount=DeleteFilesCount+1
                #os.remove(Fname)  # actual deletion left disabled - dry run only
        Localcount=0

    return DuplicateFilesCount,DeleteFilesCount,DupliCheckSumList


def LogFileCreation(TotalFileCount,DeleteFilesCount,DupliCheckSumList,DuplicateFilesCount,TimeTaken):
    # Append a summary of this run to the log file, then trigger the email report.
    fobj=open("Deleted_Files_Log.txt",'a')

    fobj.write("-"*40)
    fobj.write(f"\nTotal File Counts Is {TotalFileCount}\n")
    fobj.write(f"Duplicate File Counts Is {DuplicateFilesCount}\n")
    fobj.write(f"Deleted File Counts Is {DeleteFilesCount}\n")
    for i in DupliCheckSumList:
        fobj.write(i+" ")
        fobj.write("\n")
    fobj.write(f"Duplicate File CheckSum List Is {DupliCheckSumList}\n")
    fobj.write(f"Complete time taken for Deleting Duplicate files {TimeTaken}\n")
    fobj.write("-"*40)
    mail(TotalFileCount,DuplicateFilesCount,DeleteFilesCount,DupliCheckSumList,TimeTaken)


def DeleteDuplicate(DirectoryName):
    # Main scan routine: walk the directory tree, checksum every file,
    # group by checksum, then log + email the duplicate summary.
    Data={} #Dict
    count=0
    Start_Time=time.perf_counter()
    if os.path.exists(DirectoryName):
        if os.path.isdir(DirectoryName):
            for Folder,SubFolder,FileName in os.walk(DirectoryName):
                for Fname in FileName:
                    filepath=os.path.join(Folder,Fname)
                    CheckSum=CalculateCheckSum(filepath)
                    if CheckSum in Data:
                        Data[CheckSum].append(filepath)
                    else:
                        Data[CheckSum]=[filepath]
                    count=count+1

            DuplicateFilesCountX,DeleteFilesCountX,DupliCheckSumListX=CleanFiles(Data,count)
            
            End_time=time.perf_counter()
            Complete_time=(f"{Start_Time-End_time:2f}seconds")
            print(f"Complete time taken for Deleting Duplicate files {Complete_time}")

            LogFileCreation(TotalFileCount=count,DeleteFilesCount=DeleteFilesCountX,DupliCheckSumList=DupliCheckSumListX,DuplicateFilesCount=DuplicateFilesCountX,TimeTaken=Complete_time)

            

        else:print("This is not Directory")
    else:
        print("Directory does not exist")