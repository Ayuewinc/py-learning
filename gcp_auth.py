import os
from google.oauth2 import service_account
from google.cloud import storage

project_id = 'vicdemo'
path_to_json_file = '/Users/viczs/work_dir/vicdemo-prj-editor.json'

# Use ADC
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path_to_json_file'

# Use service account
credentials = service_account.Credentials.from_service_account_file(path_to_json_file)
scopes = credentials.with_scopes(
        [
            "https://www.googleapis.com/auth/cloud-platform",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ]
    )

# GCS example
storage_client = storage.Client(project=project_id, credentials=credentials)
