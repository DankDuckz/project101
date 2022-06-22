import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    
    def uploadFile(self, file_from, destination):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from,"rb") as f:
            dbx.files_upload(f.read(),destination,mode=WriteMode('overwrite'))

def main():
    access_token = "sl.BKCEWnbXjlQnpEtyx_YQ0CShGHPRBNCMdIprDV4TVRrX45qGLzIXV7xL9K_urmbjL1yVy4i4_BFIazxERPf1CY4xNLDzxmIzgwdmsgcQHiEckAMwTWQC6a76R0X9MGQpLnHonjQ"
    transferData = TransferData(access_token)

    file_from = input("Input the file or folder you would like to upload")
    destination = input("Input where you would like the file or folder to go to")

    transferData.uploadFile(file_from,destination)

main()