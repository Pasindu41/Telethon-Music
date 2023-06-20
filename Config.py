import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "27467283"))
    API_HASH = os.environ.get("API_HASH", "33b272caee9a0d79537cad6b6f33b3f7")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5848287412:AAFsA-HNWYyOJmQQ0j1CTFfYmIigWI2YNPc")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKEBu6U4fsfRWk2KStCFcdccRqVYvBKMjTZdDzogkIqlR9OQ-yeiUkVCkc6tXXQbfB2ETRD9bCUcP6q8xUzUbQ4WpF8olqhmZKMzgQ61EvPg7bSfhBakMSrC4zjxmSAGNFoVbjM2TYpouBVft-sz5VD2D1fPchPCetN_6hVraC_LjiS3DqBjieN8NxkY5v3H9HXtGlND5TzWIMrUvTlvC_P1m51PG0Zrx8E77Swu8zBAlxVFk3xn03ylfyBNVvqxM4jsJru6wbV8GVgMrDpX6nNlFLBts2rNmyGuIHNEGiB1NTLMJRUH9lfqI7gJXWlkI8eiL-5c2_a3htWAWhUno11aJko=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ps_alpha_music_v2_bot")
    SUPPORT = os.environ.get("SUPPORT", "sri_lankan_dark_Angels_2023") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "sri_lankan_dark_Angels_2023") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/18346976e9f4e1f729e63.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6113365841")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
