from instabot import Bot
import random
import time

# Primero creas una clase Bot()
bot = Bot()
# Login
bot.login(username="afcasuso", password="Poncio1988!")
# Que hashtags seguir
tags = ['cinematography', 'filmmaking', 'film', 'dp', 'cinematographer']

# El like en sí:
while True:
    index = random.randint(0, len(tags)-1)
    bot.like_hashtag(tags[index])
    time.sleep(300)
