import os
import tkinter as tk
from tkinter import scrolledtext

from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload

# Function to upload photos to Google Drive
def upload_photos_to_drive():
    # Define the Google Drive folder ID where you want to upload the photos.
    folder_id = '1zpVC3O3XB6VTZzT-QHig85WmIUTkE4e3'

    # Load the service account credentials.
    credentials = service_account.Credentials.from_service_account_info(
        {
  "type": "service_account",
  "project_id": "boreal-analyzer-388209",
  "private_key_id": "f8bd4de6dd060bb0006498aa141337ae22f4ec81",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCaD21ZalkKQjnr\nG2MZKCObe3nUVoS5CKSpXrRoY7OpUfpT63ITQXMGM8Ci1tBiiSIZB/N2V2iG4a9D\n5TLyLwwWKjoxRoP5DO0rUYR5692TJesAgqgS19oxgxKpUpDRm9Txao9NOczBKU23\nGuG50ewf2M9mSs/+amh5SHYvB3abr7Ho73tpcbEbDvPtRhXB/nP3wTCSYkxPc0NT\n5G3nKmlVDk6GvGLn1MpudZ2iFdY4E+zompjhyxH834UK4MBGtEF0nsf+6Gl0E+9N\nOL8jpYd9BP8HKzSZDXs+kZYVNeQXyqLBO0tWkudf6qR99jpoiZblJLckiwxM8mPA\nI0BNttzlAgMBAAECggEABYDjP0xOcFCLq3ZCf4MQu+dYzk466+CUVUfrT5wELoUd\nrq1yA/W/a1YiSGQ+dHlWolNHjg+ITeKLtXQKHQmzjP/RgrIfWSBuQTERIkkxP1Dy\n81qM24N3fsj3u9xrDPnb97XT9wZyEJJuUsoJ4e6kWJeRAnlOCIDPnkmJjfDeeqg+\ntOO3Xc0j3CADQYCxDF5HOHRUII8OPzAGNTcqgzQKEVcNtASOpDu7wIq0SAlRAEf6\nzudCLtHjfcoqOvizHvNbUioiXq0VW19V2YbbmZz4EF+yX9bU+iSKOUAtTneigAzo\nmhv2pBKzk+scALF/KjMPLGqXOZPMMZHdpKphYuEZ0QKBgQDWsC4/6nM0o7mUgSsV\nselBYDqwhmM74cyiUccchyjjWdTst2/6tUyxfmsLokfI34KCEql/+XCiCc8U9tvF\n27CkxKycCn987sGj20Wfj5M+6xZsrJ5QGs1k5FeT6g05RdTY0aOPRl1jgsU+ac4J\nFsLLCnKoB2LrRfuGPvYxyucybQKBgQC3tKKo/LTJauZqpZwPkLsDT2x8H2dZFMbT\nLCLHTVH0fWgtjV694Cb2VevTniEBj++u3MlzEvRT4eXYShTAI0Q+NYAQa4MlON3j\neJQ2314dVyXDz6gohzJcUjNQVgeFOI5UZ2lvaC2I03d0R2w0MhiVa5aPnWslvl6Y\nHtDMZoKJWQKBgA29JJiOhmTd/WhVg85VnlnCsL7POtaAMrpIhXd75s/11bx4WMAw\njgHl1y/daL6gHxf33cUEz4JvIkNzMMlOr9U7iNhLi7ERDm9P/vqhE4k5PiwiN9dk\nf7RvMHOUzNfXcjGV6OOoWx2dJsZBux+1xy17M68xGdF4nwoOSW8STw1ZAoGAJSKe\nvwpWgWDaszRHF95p74FerLisa5WHm6iQXzmCF6pCJPMu87McLS+xPFX61hYCnZaE\nIn7yZQKFM/PFvhFi+jBWcvtIx313XURCsdT1cXjsaWjQ1WB/DaqQNO0vF/8Wxnkh\nFyQ4EDCvNRI7DVITJiFZji6EOl0BQj74dllCigECgYBg+GA8QJpTk5gZ6ubTiZGK\nSpUj7E8Oo5kaMIn8v4owF9tXBO0U2S5MhAJROB+HrHIOeI0P+vpi+9NTnnTxKxbD\nep/GY30zUoT9Ueng2LX5QAdo2YEg7V89c2fmK5R6B5uhDRGDo05N7b3N1SceUSf+\njzmgeUxuxbuZQftSUkkcTA==\n-----END PRIVATE KEY-----\n",
  "client_email": "myservice@boreal-analyzer-388209.iam.gserviceaccount.com",
  "client_id": "116628351036159878850",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/myservice%40boreal-analyzer-388209.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
},
        scopes=['https://www.googleapis.com/auth/drive.file']
    )

    # Create a Google Drive service using the credentials.
    drive_service = build('drive', 'v3', credentials=credentials)

    # Specify the directory containing the photos to upload.
    photo_directory = 'D:/photo/New folder'  # Use forward slashes or double backslashes

    # Initialize the message log
    log_msg.set("Starting photo upload...\n")
    
    # Clear the success message
    success_label.config(text="")

    # List all image files in the specified directory.
    image_files = [f for f in os.listdir(photo_directory) if f.endswith(('.jpg', '.jpeg', '.png', '.gif', '.JPG'))]

    # Upload each image to Google Drive.
    for image_file in image_files:
        photo_path = os.path.join(photo_directory, image_file)

        # Check if the file already exists in the destination folder
        query = f"'{folder_id}' in parents and name = '{image_file}'"
        existing_files = drive_service.files().list(q=query).execute().get('files', [])

        if not existing_files:
            # The file does not exist in the destination folder, so upload it
            file_metadata = {
                'name': image_file,
                'parents': [folder_id],
            }
            media = MediaFileUpload(photo_path, resumable=True)
            file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            log_msg.set(log_msg.get() + f'File ID: {file.get("id")} - Photo "{image_file}" uploaded successfully!\n')
        else:
            log_msg.set(log_msg.get() + f'Photo "{image_file}" already exists in the destination folder, skipping upload.\n')

    # Display success message
    success_label.config(text="Upload Successful")

# Function to clear the success message
def clear_success_message():
    success_label.config(text="")

# Create the main tkinter window
root = tk.Tk()
root.title("Photo Upload to Google Drive")

# Create a scrolled text widget to display messages
log_msg = tk.StringVar()
log_text = scrolledtext.ScrolledText(root, width=50, height=20, wrap=tk.WORD)
log_text.grid(row=0, column=0, padx=10, pady=10)
log_text.config(state='disabled')

# Create a start button to initiate the upload
start_button = tk.Button(root, text="Start Upload", command=upload_photos_to_drive)
start_button.grid(row=1, column=0, padx=10, pady=10)

# Create a label for displaying success message
success_label = tk.Label(root, text="", fg="green")
success_label.grid(row=2, column=0, padx=10, pady=10)

# Create a clear button to clear the success message
clear_button = tk.Button(root, text="Clear", command=clear_success_message)
clear_button.grid(row=3, column=0, padx=10, pady=10)

# Start the tkinter main loop
root.mainloop()
