import os

class Settings:
    def __init__(self):
        self.ADMIN_ROLE=os.getenv('BOT_ADMIN_ROLE','Admin')
        self.GUILD_NAME=os.getenv('GUILD_NAME')
        self.BOT_PREFIX=os.getenv('BOT_PREFIX','!')
        self.CHANNEL_ELUS=os.getenv('CHANNEL_ELUS_NAME')
        self.ELUS_ROLE=os.getenv('ELUS_ROLE')


    def as_string(self):
        ret=""
        for k,v in self.__dict__.items():
            if not k.startswith('_') and k.upper()==k:
                ret+=f"{k}={v}\n"
                
        return ret