class ApiMsg:
    def __init__(self, response):
        self.apiMessage = response['api:message']
        self.ForDevelopersMode = response


class LinkInfo:
    def __init__(self, response):
        self.ndcId = response['extensions']['linkInfo']['ndcId']
        self.objectId = response['extensions']['linkInfo']['objectId']


class ChatThreads:
    def __init__(self, response):
        self.threads = []
        self.title = []
        self.threadId = []
        self.data = response

    @property
    def ChatTreads(self):
        for O in self.data:
            self.threadId.append(O['threadId'])
            self.title.append(O['title'])
        return self

class LoginInfo:
    def __init__(self, response):
        self.uid = response['auid']
        self.sid = 'sid=' + response['sid']
        self.apiMessage = response['api:message']


class MembersList:
    def __init__(self, response):
        self.data = response
        self.lst = []
        self.uid = []
        self.nickname = []
        self.level = []
        self.icon = []
        self.blogsCount = []
        self.commentsCount = []

    @property
    def MembersList(self):
        for O in self.data:
            self.uid.append(O['uid'])
            self.nickname.append(O['nickname'])
            self.level.append(O['level'])
            self.icon.append(O['icon'])
            self.blogsCount.append(O['blogsCount'])
            self.commentsCount.append(O['commentsCount'])
        return self
