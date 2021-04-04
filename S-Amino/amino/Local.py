from .lib import pack, objects
from .Global import GlobalClient
import requests
import json

UID = GlobalClient().uid
HEADERS = GlobalClient().headers


class LocalClient:
    def __init__(self, comId: str):
        self.comId = comId
        self.api = 'https://service.narvii.com/api/v1/'
        self.chat = '/s/chat/thread/'

    def get_public_chats(self, type: str = 'recommended', start: int = 0, size: int = 25):
        r = requests.get(f'{self.api + self.comId + self.chat}?type=public-all&filterType={type}&start={str(start)}&size={str(size)}',headers=HEADERS).text
        request = json.loads(r)
        return objects.ChatThreads(request['threadList']).ChatTreads

    def send_message(self, chatId: str, message: str, type: int = 0, refId: int = pack.timestamp() // 1000):

        data = {
            'content': message,
            'type': type,
            'clientRefId': refId
        }
        data = json.dumps(data)
        r = requests.post(url=f'{self.api + self.comId + self.chat + chatId}/message', data=data, headers=HEADERS).text
        request = json.loads(r)
        return objects.ApiMsg(response=request)

    def leave_chat(self, chatId: str):
        r = requests.delete(url=f'{self.api + self.comId + self.chat + chatId}/member/' + UID, headers=HEADERS).text
        request = json.loads(r)
        return objects.ApiMsg(response=request)

    def join_chat(self, chatId: str):
        r = requests.post(url=f'{self.api + self.comId + self.chat + chatId}/member/' + UID, headers=HEADERS).text
        request = json.loads(r)
        return objects.ApiMsg(response=request)

    def get_online_members(self, start: int = 0, size: int = 25):
        r = requests.get(f'{self.api + self.comId}/s/live-layer?topic=ndtopic:{self.comId}:online-members&start={str(start)}&size={str(size)}', headers=HEADERS).text
        request = json.loads(r)
        return objects.MembersList(request['userProfileList']).MembersList

    def invite_to_chat(self, userId: str, chatId: str):
        data = json.dumps({
            "uids": userId,
        })
        r = requests.post(f"{self.api + self.comId + self.chat}{chatId}/member/invite", headers=HEADERS, data=data)
        request = json.loads(r.text)
        return objects.ApiMsg(request)

    def voice_invite(self, chatId: str, userId: str):
        data = json.dumps({
            "uid": userId
        })
        r = requests.post(f"{self.api + self.comId + self.chat + chatId}/vvchat-presenter/invite/", headers=HEADERS, data=data)
        request = json.loads(r.text)
        return objects.ApiMsg(request)

    # API was Discovered by bovonos
    def invite_by_host(self, chatId: str, userId: [str, list]):
        data = json.dumps({
            "uidList": userId
        })
        r = requests.post(f"http://service.narvii.com/api/v1/{self.comId}/s/chat/thread/{chatId}/avchat-members",headers=HEADERS, data=data)
        request = json.loads(r.text)
        return objects.ApiMsg(request)

    def start_chat(self, userId: str, content: str):
        data = json.dumps({
            "type": 1,
            "inviteeUids": userId,
            "timestamp": pack.timestamp()
        })
        r = requests.post(f"http://service.narvii.com/api/v1/{self.comId}/s/chat/thread", headers=HEADERS, data=data)
        request = json.loads(r.text)
        return objects.ApiMsg(request)

    def edit_chat(self, chatId: str, content: str, title: str):
        data = json.dumps({
            "content": content,
            "title": title
        })
        r = requests.post(f"http://service.narvii.com/api/v1/{self.comId}/s/chat/thread/{chatId}", headers=HEADERS, data=data)
        request = json.loads(r.text)
        return objects.ApiMsg(request)
