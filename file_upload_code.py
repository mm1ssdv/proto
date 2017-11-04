from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
#gauth.CommandLineAuth()

drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': 'daqdata.csv'})  # Create GoogleDriveFile instance with title
file1.SetContentFile('pitestcsv.csv') 
file1.Upload()
