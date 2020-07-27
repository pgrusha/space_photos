import glob
import os
import sys
from dotenv import load_dotenv
from fetch_spacex import fetch_spacex_last_launch
from fetch_hubble import fetch_hubble_collection
from instabot import Bot


if __name__ == '__main__':
    load_dotenv()
    login = os.getenv("INSTAGRAM_LOGIN")
    password = os.getenv("INSTAGRAM_PASSWORD")
#    fetch_spacex_last_launch()
#    fetch_hubble_collection('printshop');
    bot = Bot()
    bot.login(username=login, password=password)
    pics = glob.glob("images/*.jpg")
    pics = sorted(pics)
    try:
        for pic in pics:
            bot.upload_photo(pic, caption='Space photo')
            if bot.api.last_response.status_code != 200:
                print(bot.api.last_response)
                break
    except Exception as e:
        print(str(e))