from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

from upload_config import COLAB_FOLDER_ID

# Autenticacion utilizando client_secrets.json
g_login = GoogleAuth()
# If there are credentials load them
# If not, web authentication and save the credentials
credential_file_name = "mycreds.txt"
g_login.LoadCredentialsFile(credential_file_name)
if g_login.credentials is None:
    # Authenticate if they're not there
    g_login.LocalWebserverAuth()
elif g_login.access_token_expired:
    # Refresh them if expired
    g_login.Refresh()
else:
    # Initialize the saved creds
    g_login.Authorize()
# Save the current credentials to a file
g_login.SaveCredentialsFile(credential_file_name)

# Cliente drive
drive = GoogleDrive(g_login)

extra_path = '../extras/'
ubigeos_name = 'ubigeos.csv'
clean_data_path = '../data_limpia/'


# Delete older files
def delete_folder_files(folder_id):
    file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(folder_id)}).GetList()
    for file in file_list:
        file.Delete()


delete_folder_files(COLAB_FOLDER_ID)

# Create new extra folder
extra_folder = drive.CreateFile({'title': 'data', 'mimeType': 'application/vnd.google-apps.folder',
                                 'parents': [{'id': COLAB_FOLDER_ID}]})
extra_folder.Upload()

file_dict = {
    'ubigeos.csv': {'local_path': extra_path,
                    'drive_folder_id': extra_folder['id'],
                    'type': 'text/csv'},
    'casos_positivos_covid19.csv': {'local_path': clean_data_path,
                                    'drive_folder_id': extra_folder['id'],
                                    'type': 'text/csv'},
    'Exploracion.ipynb': {'local_path': './', 'drive_folder_id': COLAB_FOLDER_ID,
                          'type': 'application/vnd.google.colaboratory'}
}


# Upload the new files
for file_key in file_dict.keys():
    with open(file_dict[file_key]['local_path']+file_key, "r") as file:
        print("Subiendo: ", file_key)
        file_drive = drive.CreateFile({'title': os.path.basename(file.name),
                                       'parents': [{'id': file_dict[file_key]['drive_folder_id']}],
                                       'mimeType': file_dict[file_key]['type']})
        file_drive.SetContentString(file.read())
        file_drive.Upload()
        print(file_drive['id'])
