import amino

client = amino.GlobalClient()
client.login(email='wem7ad@gmail.com', password='0537SirLez3000')

subclient = amino.LocalClient('x195936484')

chatList = subclient.get_public_chats()
for name, id in zip(chatList.title, chatList.threadId):
    msg = subclient.join_chat(chatId=id).apiMessage
    print(msg)
