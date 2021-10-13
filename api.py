import os
import requests

TOKEN = os.environ.get("PAT_TOKEN")
OWNER = rahulmalewadi
REPO = terraform-azure

VERSION = 1.2

headers = {
  "Accept": "application/vnd.github.v3+json",
  "Authorization": f"token {TOKEN}",
}

data = {
  "event_type": "build",
  "client_payload": {
    "version": VERSION
  }
}

requests.post(
  f"https://api.github.com/repos/{OWNER}/{REPO}/dispatches",
  data=data,
  headers=headers
)
