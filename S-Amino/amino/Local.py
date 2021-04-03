from .lib import pack, objects
from .lib.headers import Headers
import requests
import json


class LocalClient:
    def __init__(self, comId: str):
        self.comId = comId
        self.api = 'https://service.narvii.com/api/v1/'
        self.chat = '/s/chat/thread/'

    def get_public_chats(self, type: str = 'recommended', start: int = 0, size: int = 25):
        r = requests.get(f'{self.api + self.comId + self.chat}?type=public-all&filterType={type}&start={str(start)}&size={str(size)}',headers=Headers(0).headers).text
        request = json.loads(r)
        return objects.ChatThreads(request['threadList']).ChatTreads

    def send_message(self, chatId: str, message: str, type: int = 0, refId: int = pack.timestamp() // 1000):

        data = {
            'content': message,
            'type': type,
            'clientRefId': refId
        }
        data = json.dumps(data)
        r = requests.post(url=f'{self.api + self.comId + self.chat + chatId}/message', data=data, headers=Headers(0).headers).text
        request = json.loads(r)
        return objects.ApiMsg(response=request)

    def leave_chat(self, chatId: str):
        r = requests.delete(url=f'{self.api + self.comId + self.chat + chatId}/member/' + Headers(0).uid, headers=Headers(0).headers).text
        request = json.loads(r)
        return objects.ApiMsg(response=request)

    def join_chat(self, chatId: str):
        r = requests.post(url=f'{self.api + self.comId + self.chat + chatId}/member/' + Headers(0).uid, headers=Headers(0).headers).text
        request = json.loads(r)
        return objects.ApiMsg(response=request)

    def get_online_members(self, start: int = 0, size: int = 25):
        r = requests.get(f'{self.api + self.comId}/s/live-layer?topic=ndtopic:{self.comId}:online-members&start={str(start)}&size={str(size)}', headers=Headers(0).headers).text
        request = json.loads(r)
        return objects.MembersList(request['userProfileList']).MembersList

    def invite_to_chat(self, userId: str, chatId: str):
        data = json.dumps({
            "uids": userId,
        })
        r = requests.post(f"{self.api + self.comId + self.chat}{chatId}/member/invite", headers=Headers(0).headers, data=data)
        request = json.loads(r.text)
        return objects.ApiMsg(request)

    def voice_invite(self, chatId: str, userId: str):
        data = json.dumps({
            "uid": userId
        })
        r = requests.post(f"{self.api + self.comId + self.chat + chatId}/vvchat-presenter/invite/", headers=Headers(0).headers, data=data)
        request = json.loads(r.text)
        return objects.ApiMsg(request)
