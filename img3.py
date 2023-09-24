import os
import tkinter as tk
from tkinter import scrolledtext

from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload

# Function to upload photos to Google Drive
def upload_photos_to_drive():
    # Define the Google Drive folder ID where you want to upload the photos.
    folder_id = 'Your Folder ID'

    # Load the service account credentials.
    credentials = service_account.Credentials.from_service_account_info(
        {
  #Copy a json file content and paste here
},
        scopes=['https://www.googleapis.com/auth/drive.file']
    )

    # Create a Google Drive service using the credentials.
    drive_service = build('drive', 'v3', credentials=credentials)

    # Specify the directory containing the photos to upload.
    photo_directory = 'Folder path of your pc that contain photos to upload'  # Use forward slashes or double backslashes

    # Initialize the message log
    log_msg.set("Starting photo upload...\n")
    
    # Clear the success message
    success_label.config(text="")

    # List all image files in the specified directory.
    image_files = [f for f in os.listdir(photo_directory) if f.endswith(('.jpg', '.jpeg', '.png', '.gif', '.JPG','.mp4'))]

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
