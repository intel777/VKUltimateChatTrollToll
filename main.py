import vk
import random
import time

session = vk.AuthSession(access_token='')
api = vk.API(session)
chatid = input('Enter chatid: ')
chatname = input('Enter new chatname: ')
mess = input('Enter message: ')

while True:
    chat = api.messages.getChat(chat_id=chatid)
    if chat['title'] == chatname:
        print('OK')
    else:
        r = random.randint(1, 100000)
        api.messages.send(chat_id=chatid, message=mess, guid=r)
        api.messages.editChat(chat_id=chatid, title=chatname)
        api.messages.removeChatUser(chat_id=chatid, user_id=265643846)
    time.sleep(1)
