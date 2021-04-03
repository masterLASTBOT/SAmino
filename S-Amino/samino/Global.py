from .lib import objects, pack
import requests
import json
refId = 712543354323901337


class GlobalClient:
    def __init__(self):
        self.api = 'https://service.narvii.com/api/v1/'
        self.chat = '/s/chat/thread/'
        global headers
        self.headers = {
            "NDCDEVICEID": "019B6133991CBC2428F822E55AEF0499B3E674928B3268072CC9381881024F07047DCB9A82899C91B8"
        }
        self.uid = {}

    def login(self, email: str, password: str, comId: str = None):
        data = {
            "deviceID": "019B6133991CBC2428F822E55AEF0499B3E674928B3268072CC9381881024F07047DCB9A82899C91B8",
            "email": email,
            "secret": f"0 {password}"
        }
        data = json.dumps(data)
        r = requests.post(url=f'{self.api}g/s/auth/login', data=data, headers=self.headers).text
        request = json.loads(r)
        self.headers['NDCAUTH'] = objects.LoginInfo(response=request).sid
        self.uid['uid'] = objects.LoginInfo(response=request).uid
        return objects.LoginInfo(response=request).sid

    def send_message(self, chatId: str, message: str, clientRefId: int = pack.timestamp(), type: int = 0):
        data = {
            'content': message,
            'type': type,
            'clientRefId': clientRefId
        }
        data = json.dumps(data)
        r = requests.post(url=f'{self.api}g{self.chat + chatId}/message', data=data, headers=self.headers).text
        request = json.loads(r)
        return objects.ApiMsg(response=request)

    def join_chat(self, chatId: str, message: str, clientRefId: int = pack.timestamp(), type: int = 0):
        data = {
            'content': message,
            'type': type,
            'clientRefId': clientRefId
        }
        data = json.dumps(data)
        r = requests.post(url=f'{self.api}g{self.chat + chatId}/member/' + self.uid['uid'], data=data, headers=self.headers).text
        request = json.loads(r)
        return objects.ApiMsg(response=request)

    def leave_chat(self, chatId: str, message: str, clientRefId: int = pack.timestamp(), type: int = 0):
        data = {
            'content': message,
            'type': type,
            'clientRefId': clientRefId
        }
        data = json.dumps(data)
        r = requests.delete(url=f'{self.api}g{self.chat + chatId}/member/' + self.uid['uid'], data=data, headers=self.headers).text
        request = json.loads(r)
        return objects.ApiMsg(response=request)

    def get_from_link(self, link: str):
        r = requests.get(f'{self.api}g/s/link-resolution?q={link}', headers=self.headers).text
        request = json.loads(r)
        return objects.LinkInfo(response=request['linkInfoV2'])
