
import requests
import random
import json
class twitter_login():
    def __init__(self) -> None:
        username : str = input("username[MAIN ACCOUNT]:")
        password : str = input("password[MAIN ACCOUNT]:")
        c = self.login(username,password)
        if c is False:
            print("Bad password or blocked")
        else:
            ct0 = str(c["ct0"])
            auth = str(c["auth_token"])	
            print("[+] Succefly grab auth / ct0 [+]")
            with open("main_account.txt","w") as wr:
                info = {"ct0":ct0,"auth":auth}
                json.dump(info,wr)
        print("-- Another Account Loading !-- \n")
        username : str = input("username:")
        password : str = input("password:")
        c = self.login(username,password)
        if c is False:
            print("Bad password or blocked")
        else:
            ct0 = str(c["ct0"])
            auth = str(c["auth_token"])	
            print("[+] Succefly grab auth / ct0 [+]")
            with open("account_realise.txt","w") as wr:
                info = {"ct0":ct0,"auth":auth}
                json.dump(info,wr)
    def login(self,Username,Password):
        letters = 'qwertyuiopasdfghjklzxcvbnm123456790qwertyiobuzxcvbasdfr142'
        token = ''.join(random.choice(letters) for x in range(23)) 
        session = requests.Session()
        url = "https://twitter.com/sessions"
        session.headers = {
        "Host": "twitter.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        }
        cookies = {
        "_mb_tk":token
        }
        data = {
        "authenticity_token":token,
        "session[username_or_email]":Username,
        "session[password]":Password
        }
        response = session.post(url, data=data , cookies=cookies)
        y = session.cookies.get_dict()
        try:

            c = str(y["ct0"])
            v = str(y["auth_token"])	
            return y
        except:
            return False
if __name__ == "__main__":
    print("""

                    | 
____________    __ -+-  ____________ 
\_____     /   /_ \ |   \     _____/
 \_____    \____/  \____/    _____/
  \_____                    _____/
     \___________  ___________/
               /____\

            FALCON DIGITAL ORG 
                IG : [31421 - m1c1]
                FREE & OPEN SOURCE 
                
        Twitter Login / Info Grabber 
            Falcon Digital Org
    
    """)
    twitter_login()

