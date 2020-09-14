import telepot
import datetime

token='1268050734:AAGttLgwkW96oFpxBdxhBpLX5yFA7YnuOmY'
bot = telepot.Bot(token)
print (bot.getMe())

    
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text':
        if msg['text'].upper()=="DATE":
            bot.sendMessage(chat_id,str(datetime.datetime.today().strftime("%x")))
        else:
            bot.sendMessage(chat_id,"Commend for Date is:-Date")
bot.message_loop(handle)
