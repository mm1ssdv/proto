from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
gauth.CommandLineAuth() # Creates local webserver and auto handles authentication.

from pydrive.drive import GoogleDrive

drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': 'daqdata.csv'})  # Create GoogleDriveFile instance with title
file1.SetContentFile('pitestcsv.csv')
file1.Upload()
