import requests,json,telebot
from telebot import types

print('BOT MADE BY AKIL \n')
print('@AKIL828 - @FFFFFFM')
print('-_'*10)
print("\n"*5)
print('INPUT YOUR TOKEN BOT')
print('-_'*10)
print('          |')
التوكن = input('          ------------>')

bot = telebot.TeleBot(التوكن,parse_mode='MARKDOWN')
bot.remove_webhook()
print("start work")

def فحص(akil):
    رابط="https://min-api.cryptocompare.com/data/price"
    دت={
        "fsym" : str(akil),
        "tsyms" : "USD"}
    ريك=requests.request("GET",رابط,params=دت)
    if 'USD' in ريك.text:    	
	    response=json.loads(ريك.text)
	    عقيل = response['USD']
	    
    else :
	    عقيل = 'n'
    return عقيل

@bot.message_handler(commands=['start'])
def ويوووووووو(message):
	رييي = "بوت اسعار العملات  \n استخدم رمز العمله فقط  : \n\n مثل : btc eth bnb\n\n	استخدم رمز العمله وليس الاسم\n\nBOT BY @AK828"
	bot.reply_to(message,رييي )

@bot.message_handler(func=lambda message: True)

def ىىررر(message):
    قححححح = message.text
    o  =   فحص(قححححح)
    if o == "n" :
    
 	    bot.reply_to(message, "اكتب رمز العمله فقط")
    else:
 	    bot.reply_to(message, f"The Price : {o}")    


bot.infinity_polling()
        
                
    
    
    
    