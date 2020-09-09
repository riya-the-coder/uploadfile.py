import os
import os.walk()
import os.path.relpath() 
import os.path.join() 


class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_files(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from)
        relative_path=os.path.relpath(local_path,file_from)
        dropbox_path=os.path.join(file_to,relative_path)
    with open(local_path,"rb") as f:
        dbx.files_upload(f.(read), dropbox_path, mode=WriteMode('overwrite'))

def main():
        access_token="rtteV3NprPwAAAAAAAAAAZBazPvFYIy9j2zCP4p2j6Q0tN1QMK8JE54uYm3PXKMp"
        transferData=TransferData(access_token)
        file_from=input("enter the file path to transfer-")
        file_to=input("enter the full path to upload to dropbox")
        transferData.upload_files(file_from,file_to)
        print("file has been moved")

main()
        
       
       