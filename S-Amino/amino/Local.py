from .lib import pack, objects
import requests
import json


class LocalClient:
    def __init__(self, comId: str, sid: str, uid: str):
        self.comId = comId
        self.api = 'https://service.narvii.com/api/v1/'
        self.chat = '/s/chat/thread/'
        self.sid = sid
        self.uid = uid
        self.headers = {
            "NDCDEVICEID": "019B6133991CBC2428F822E55AEF0499B3E674928B3268072CC9381881024F07047DCB9A82899C91B8",
            "NDCAUTH": f'{self.sid}'
        }

    def get_public_chats(self, type: str = 'recommended', start: int = 0, size: int = 25):
        r = requests.get(f'{self.api + self.comId + self.chat}?type=public-all&filterType={type}&start={str(start)}&size={str(size)}',headers=self.headers).text
        request = json.loads(r)
        return objects.ChatThreads(request['threadList']).ChatThreads

    def send_message(self, chatId: str, message: str, type: int = 0, refId: int = pack.timestamp() // 1000):

        data = {
            'content': message,
            'type': type,
            'clientRefId': refId
        }
        data = json.dumps(data)
        r = requests.post(url=f'{self.api + self.comId + self.chat + chatId}/message', data=data, headers=self.headers).text
        request = json.loads(r)
        return objects.ApiMsg(response=request)

    def leave_chat(self, chatId: str):
        r = requests.delete(url=f'{self.api + self.comId + self.chat + chatId}/member/' + self.uid, headers=self.headers).text
        request = json.loads(r)
        return objects.ApiMsg(response=request)

    def join_chat(self, chatId: str):
        r = requests.post(url=f'{self.api + self.comId + self.chat + chatId}/member/' + self.uid, headers=self.headers).text
        request = json.loads(r)
        return objects.ApiMsg(response=request)

    def get_online_members(self, start: int = 0, size: int = 25):
        r = requests.get(f'{self.api + self.comId}/s/live-layer?topic=ndtopic:{self.comId}:online-members&start={str(start)}&size={str(size)}', headers=self.headers).text
        request = json.loads(r)
        return objects.MembersList(request['userProfileList']).MembersList

    def invite_to_chat(self, userId: str, chatId: str):
        data = json.dumps({
            "uids": userId,
        })
        r = requests.post(f"{self.api + self.comId + self.chat + chatId}/member/invite", headers=self.headers, data=data)
        request = json.loads(r.text)
        return objects.ApiMsg(request)

    def voice_invite(self, chatId: str, userId: str):
        data = json.dumps({
            "uid": userId
        })
        r = requests.post(f"{self.api + self.comId + self.chat + chatId}/vvchat-presenter/invite/", headers=self.headers, data=data)
        request = json.loads(r.text)
        return objects.ApiMsg(request)

    # API was Discovered by bovonos
    def invite_by_host(self, chatId: str, userId: [str, list]):
        data = json.dumps({
            "uidList": userId
        })
        r = requests.post(f"{self.api + self.comId + self.chat + chatId}/avchat-members",headers=self.headers, data=data)
        request = json.loads(r.text)
        return objects.ApiMsg(request)

    def start_chat(self, userId: str, content: str):
        data = json.dumps({
            "type": 1,
            "inviteeuids": userId,
            "timestamp": pack.timestamp()
        })
        r = requests.post(f"{self.api + self.comId + self.chat}", headers=self.headers, data=data)
        request = json.loads(r.text)
        return objects.ApiMsg(request)

    def edit_chat(self, chatId: str, content: str, title: str):
        data = json.dumps({
            "content": content,
            "title": title
        })
        r = requests.post(f"{self.api + self.comId + self.chat + chatId}", headers=self.headers, data=data)
        request = json.loads(r.text)
        return objects.ApiMsg(request)
