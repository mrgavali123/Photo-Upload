# Photo-Upload
This is a code for Photographer that click a photos and unable to share all photos in minimum time so in this code i solve the problem for all photographer in this code a photos in a desktop or laptop directly post in one click 

To use this code firstly we want to create new project on google cloud console and create json crenditial
To obtain the JSON credentials file for using Google APIs, such as the Google Drive API, you'll need to create a service account and download the associated credentials file from the Google Cloud Console. Here are step-by-step instructions on how to do this:

Go to the Google Cloud Console:

Open a web browser and go to the Google Cloud Console.
Create a New Project:

If you don't have an existing project, you'll need to create one. Click on the project drop-down menu at the top of the page and select "New Project." Follow the prompts to create a new project.
Enable the Required APIs:

In the Google Cloud Console, navigate to the "APIs & Services" > "Library" page.
Search for the API you want to use (e.g., "Google Drive API") and click on it.
Click the "Enable" button to enable the API for your project.
Create a Service Account:

In the Google Cloud Console, navigate to the "APIs & Services" > "Credentials" page.
Click the "Create credentials" button and select "Service Account Key."
Set Up the Service Account:

In the "Create a service account" form, provide a name for your service account.
Choose a role for the service account (e.g., "Project" > "Editor" for full access).
Optionally, you can grant additional permissions as needed.
Click the "Continue" button.
Create a JSON Key:

In the next step, you can choose to create a JSON key for the service account. Select the JSON option and click the "Create" button.
Download the JSON Key:

The JSON key file will be downloaded to your computer. It contains the necessary credentials for your application to access Google APIs.
Secure Your JSON Key:

Treat the JSON key file as sensitive information. Keep it secure and don't share it openly.
Now you have the JSON credentials file that you can use in your Python code to authenticate your application when interacting with Google Drive API or other Google APIs. You can reference this JSON file in your code when setting up the credentials as shown in the Python code samples provided earlier.

Remember to enable billing for your Google Cloud project if you plan to use the APIs extensively, as some APIs may have usage limits.

2) Then create a folder on drive and get folder id
To set the Google Drive folder ID that you want to use for uploading photos, you'll need to either create a new folder in Google Drive or use an existing folder. Here's how you can obtain the folder ID:

Option 1: Create a New Folder in Google Drive

Go to Google Drive and make sure you're logged in with the Google account associated with your project.

Click the "+ New" button on the left-hand side and select "Folder."

Give your folder a name, for example, "Wedding Photos."

Open the newly created folder by clicking on its name.

Look at the URL in your browser's address bar. It should look something like this:

https://drive.google.com/drive/folders/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

The XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX portion is the folder ID. Copy this ID and use it in your Python code as the DRIVE_FOLDER_ID.

Option 2: Use an Existing Folder

If you want to use an existing folder, follow these steps:

Open Google Drive.

Navigate to the existing folder you want to use.

Click on the folder to open it.

Just like in Option 1, look at the URL in your browser's address bar. The XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX portion is the folder ID. Copy this ID and use it in your Python code as the DRIVE_FOLDER_ID.

Now that you have the folder ID, you can set it in your Python code as shown earlier:

DRIVE_FOLDER_ID = 'your_folder_id'
