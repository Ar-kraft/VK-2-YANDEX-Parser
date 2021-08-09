import requests

token="WRITE YOUR TOKEN HERE"

class YaUploader:
    file_path = None
    def __init__(self, file_path: str, token):
        self.file_path = file_path
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": file_path, 'overwrite':"true"}
        response = requests.get(upload_url, headers=headers, params=params)
        print(response.json())
        return response.json()

    def upload(self):
        done_ref = self._get_upload_link(self.file_path).get("href", "")
        response = requests.put(done_ref, data=open(self.file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')
        return response.status_code


