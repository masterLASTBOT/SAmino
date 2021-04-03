from amino.lib import objects, pack
from amino import Global
import requests
import json
Global = Global.GlobalClient()

class LocalClient:
    def __init__(self, comId: str):
        self.comId = comId
        self.headers = Global.headers

    def get_public_chats(self, type: str = 'recommended', start: int = 0, size: int = 25):
        r = requests.get(f'{Global.api + self.comId + Global.chat}?type=public-all&filterType={type}&start={str(start)}&size={str(size)}',headers=self.headers).text
        request = json.loads(r)
        return objects.ChatThreads(request['threadList']).ChatTreads

    def send_message(self, chatId: str, message: str, type: int = 0, refId: int = pack.timestamp() // 1000):

        data = {
            'content': message,
            'type': type,
            'clientRefId': refId
        }
        data = json.dumps(data)
        r = requests.post(url=f'{Global.api + self.comId + Global.chat + chatId}/message', data=data, headers=self.headers).text
        request = json.loads(r)
        return objects.ApiMsg(response=request)

    def leave_chat(self, chatId: str):
        r = requests.delete(url=f'{Global.api + self.comId + Global.chat + chatId}/member/' + Global.uid['uid'], headers=self.headers).text
        request = json.loads(r)
        return objects.ApiMsg(response=request)

    def join_chat(self, chatId: str):
        r = requests.post(url=f'{Global.api + self.comId + Global.chat + chatId}/member/' + Global.uid['uid'], headers=self.headers).text
        request = json.loads(r)
        return objects.ApiMsg(response=request)

    def get_online_members(self, start: int = 0, size: int = 25):
        r = requests.get(f'{Global.api + self.comId}/s/live-layer?topic=ndtopic:{self.comId}:online-members&start={str(start)}&size={str(size)}', headers=self.headers).text
        request = json.loads(r)
        return objects.MembersList(request['userProfileList']).MembersList

Global.login(email='wem7ad@gmail.com', password='0537SirLez3000')
print(LocalClient('x195936484').headers)