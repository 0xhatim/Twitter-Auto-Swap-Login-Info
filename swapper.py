


try:
    import time,json,random,sys
    from threading import Event,Lock,Thread
    from requests import post as FALCON 
    from autopy import alert as MSGBOX
except Exception as e:
    print("Error Download",e,"lib")
    input("Enter To Exit")
    sys.exit()

POST_URL = "https://twitter.com/i/api/1.1/account/settings.json"


class Twitter_Swapper():
    def __init__(self) -> None:
        self.Event_Handler  = Event()
        self.Locks = Lock()
        self.counter : int = 0 
        self.spam : int= 0 
        self.info_realise  = None 
        self.info_main = None 
        self.run = True
        try:

            with open("main_account.txt","r") as main_info:
                self.info_main = json.loads(main_info.read())
            with open("account_realise.txt","r") as main_realise:
                self.info_realise = json.loads(main_realise.read())
        except Exception as e:
            print(f"Error In File :",e)
        else:
            try:
                auth = self.info_main['auth']
                ct0 = self.info_main['ct0']
                self.main_headers =  {

            "authority":"twitter.com",
            "method": "POST",
            "path":"/i/api/1.1/account/settings.json",
            "scheme":"https",
            "accept":"*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language":"ar,en-US;q=0.9,en;q=0.8",
            "authorization": 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            "content-length":"168",
            "content-type":"application/x-www-form-urlencoded",
            "dnt":"1",
            "cookie":f'auth_token={auth}; ct0={ct0};',
            "origin": "https://twitter.com",
            "referer":"https://twitter.com/settings/screen_name",
            "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest":"empty",
            "sec-fetch-mode":"cors",
            "sec-fetch-site":"same-origin",
            "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
            "x-csrf-token":f"{ct0}",
            "x-twitter-active-user": "yes",
            "x-twitter-auth-type":"OAuth2Session",
            "x-twitter-client-language": "en",
        }
                auth = self.info_realise['auth']
                ct0 = self.info_realise['ct0']
                self.realise_headers =  {

            "authority":"twitter.com",
            "method": "POST",
            "path":"/i/api/1.1/account/settings.json",
            "scheme":"https",
            "accept":"*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language":"ar,en-US;q=0.9,en;q=0.8",
            "authorization": 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            "content-length":"168",
            "content-type":"application/x-www-form-urlencoded",
            "dnt":"1",
            "cookie":f'auth_token={auth}; ct0={ct0};',
            "origin": "https://twitter.com",
            "referer":"https://twitter.com/settings/screen_name",
            "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest":"empty",
            "sec-fetch-mode":"cors",
            "sec-fetch-site":"same-origin",
            "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
            "x-csrf-token":f"{ct0}",
            "x-twitter-active-user": "yes",
            "x-twitter-auth-type":"OAuth2Session",
            "x-twitter-client-language": "en",
        }

            except Exception as e:
                print(e)
            else:
                self.target : str = input("[+] TARGET(REALISE ACC):")
                self.data_target = {
                    "screen_name": self.target
                }
                self.RANDOM_TARGET =self.target + str(random.randint(10,10000))
                Threads = int(input("[+] Threads:"))
                for _ in range(2):
                    Thread(target=self.realise_acc).start()
                MSGBOX.alert(f"'FD 🦅 TWITTER SWAPPER IS READY !'\nTarget:{self.target}\nThreads:{Threads}","FD MSGBOX")
                self.Event_Handler.set()
                for _ in range(Threads):
                    Thread(target=self.attacker_Function).start()  

    def realise_acc(self):
        self.Event_Handler.wait()
        time.sleep(0.5)
        while self.run:
            r = FALCON(POST_URL,data={"screen_name":self.RANDOM_TARGET},headers=self.realise_headers,allow_redirects=True).status_code
            if r == 200:
                print("[+] Successefly Realise it ![+] ",end="\r")
                break
            elif r == 429:
            
                print("[+] BLOCKED FROM REALISE ! [+]")
    def attacker_Function(self):
        while self.run:
            r = FALCON(POST_URL,data=self.data_target,headers=self.main_headers,allow_redirects=True).status_code
            self.counter+=1
            if r == 200:
                with self.Locks:
                        
                    print(f"\n\nClaimed Successefly; Target:{self.target}")
                    print(f"\n\nAttempts:{self.counter}")
                    with open("Swapped.txt","a") as wr:
                        wr.write(f'{self.target}')
                    MSGBOX.alert(f'Done @{self.target}\nAttempts:{self.counter}\nFD NEVER FAIL','FD $DONE')
            else:
                print(r)

                


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
            


""")

if __name__ == "__main__" :
    Twitter_Swapper()