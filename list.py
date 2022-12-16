import google.auth
from googleapiclient import discovery

crds, prj = google.auth.default(scopes=["https://www.googleapis.com/auth/drive.metadata.readonly"])
service = discovery.build("drive", "v3", credentials=crds)
result = service.files().list().execute()
print(result)