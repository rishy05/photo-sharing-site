import os

import google.auth
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.errors import HttpError
import mimetypes
import io
import shutil
from time import sleep


scopes = ["https://www.googleapis.com/auth/drive"]


def drive_auth():
    global creds
    global service
    creds = None
    if os.path.exists("token_drive.json"):
        print("good")
        creds = Credentials.from_authorized_user_file("token_drive.json", scopes)
        service = build("drive", "v3", credentials=creds)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("secrets.json", scopes)
            creds = flow.run_local_server(port=0)
        with open("token_drive.json", "w") as token:
            token.write(creds.to_json())


def cre_fol(nam, eemail):
    try:
        # create drive api client
        service = build("drive", "v3", credentials=creds)
        file_metadata = {
            "name": nam,
            "mimeType": "application/vnd.google-apps.folder",
        }

        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata, fields="id").execute()
        idd = file.get("id")
        print(f'Folder ID: "{idd}".')
        print("folder created")

        permission = {"type": "user", "role": "reader", "emailAddress": eemail}

        service.permissions().create(fileId=idd, body=permission).execute()
        print(f"Successfully shared folder '{nam}' with '{eemail}'.")
        return idd

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None


def up(filess, iid):
    for fil in filess:
        file_metadata = {"name": fil, "parents": [iid]}
        mime_type, _ = mimetypes.guess_type(fil)
        print(mime_type)
        media = MediaFileUpload(fil, mimetype=mime_type)
        file = (
            service.files()
            .create(body=file_metadata, media_body=media, fields="id")
            .execute()
        )
    print("files uploaded")


# drive_auth()

# idd = cre_fol("ashok", "rishywanthambalam.aids2021@citchennai.net")

# up(["grp.jpg", "ibbu.jpeg", "raju.jpeg"], iid=idd)
