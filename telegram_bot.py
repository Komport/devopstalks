from telebot import TeleBot as tb # Telegram API

class poster:
   _token = "token"
   _url = "https://api.telegram.org/bot"
   _channel_id = "@tst" #channel link
   _bot = None
   def __init__(self):
      self._bot = tb(self._token)

   def send_message(self,description):
      self.post_text(description)

   def post_text(self, msg):
      status = self._bot.send_message(chat_id=self._channel_id, text=msg)
