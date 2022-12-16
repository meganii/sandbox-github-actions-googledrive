import google.auth
from googleapiclient import discovery

crds, prj = google.auth.default(scopes=["https://www.googleapis.com/auth/drive","https://www.googleapis.com/auth/cloud-platform"])
service = discovery.build("drive", "v3", credentials=crds)
service.files().list().execute()