import requests
import time
import sys
from platform import system
import os
import http.server
import socketserver
import threading  
BOLD = '\033[1m'
CYAN = '\033[96m'
logo =("""\x1b[1;36m
  WELCOME TO AKATSUKI TOOL    
  
  
  
\033[38;5;196m█████╗ ██╗  ██╗ █████╗ ████████╗███████╗██╗   ██╗██╗  ██╗██╗
\033[38;5;208m██╔══██╗██║ ██╔╝██╔══██╗╚══██╔══╝██╔════╝██║   ██║██║ ██╔╝██║
\033[38;5;226m███████║█████╔╝ ███████║   ██║   ███████╗██║   ██║█████╔╝ ██║
\033[38;5;214m██╔══██║██╔═██╗ ██╔══██║   ██║   ╚════██║██║   ██║██╔═██╗ ██║
\033[38;5;202m██║  ██║██║  ██╗██║  ██║   ██║   ███████║╚██████╔╝██║  ██╗██║
\033[38;5;196m╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝
\033[0m  # Reset color
 




\033[1;34m ╔════════════════════════════════════════════════════════════╗  
 \033[1;34m║
\033[1;35m ║ 𝗔𝗨𝗧𝗛𝗘𝗥    : \033[1;35m -𝐗𝐖𝐃 𝐌𝐄𝐍𝐓𝐀𝐖𝐋 3:)                        
\033[1;34m ║
 \033[1;33m║ 𝗚𝗔𝗡𝗚    : \033[1;33m𝐎𝐅𝐅𝐋𝐈𝐍𝐄 𝐒𝐄𝐑𝐕𝐄𝐑
\033[1;34m ║
 \033[1;34m║ 𝗚𝗜𝗧𝗛𝗨𝗕    : \033[1;34m
 \033[1;34m║
\033[1;31m ║ 𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞  : \033[1;35m𝐅𝐀𝐓𝐇𝐄𝐑 𝐎𝐅 𝐀𝐋𝐋 𝐑𝐔𝐋𝐄𝐗
 \033[1;34m║
\033[1;36m ║ 𝗧𝗢𝗢𝗟 𝗡𝗔𝗠𝗘: \033[1;36m𝐀𝐊𝐀𝐓𝐒𝐔𝐊𝐈 𝐑𝐔𝐋𝐄𝐗
\033[1;34m ║
 \033[1;31m║ 𝗪𝗛𝗔𝗧𝗦𝗔𝗣𝗣  :\033[1;37m+1(333)0000-0000
\033[1;34m ║
\033[1;34m ╚════════════════════════════════════════════════════════════╝


 \033[1;34m╔════════════════════════════════════════════════════════════╗  
 \033[1;34m║ \033[1;33m𝗗𝗢𝗡𝗧 𝗖𝗢𝗣𝗬 𝗠𝗘 𝗜 𝗔𝗠 𝗕𝗥𝗔𝗡𝗗 8-)\033[1;34m  ║
 \033[1;34m╚════════════════════════════════════════════════════════════╝

 ╔════════════════════════════════════════════════════════════╗  
 \033[1;35m 𝐀𝐊𝐀𝐓𝐒𝐔𝐊𝐈 𝐑𝐔𝐋𝐄𝐗 𝐈𝐍𝐒𝐈𝐃𝐄""" )

def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
cls()
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"H")
def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()
def get_access_tokens(token_file):
    with open(token_file, 'r') as file:
        return [token.strip() for token in file]
def send_messages(convo_id, tokens, messages, haters_name, speed):
    headers = {
        'Content-type': 'application/json',
    }
    num_tokens = len(tokens)
    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)
    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = tokens[token_index]
                message = messages[message_index].strip()
                url = "https://graph.FACEBOOK.com/v17.0/{}/".format('t_' + convo_id)
                parameters = {'access_token': access_token, 'message': f'{haters_name} {message}'}
                response = requests.post(url, json=parameters, headers=headers)
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("\033[1;35m[√]══════════════») 𝐀𝐊𝐀𝐓𝐒𝐔𝐊𝐈 𝐎𝐍𝐅𝐈𝐑𝐄 («══════════════   {} of Convo\033[1;35m {} \033[1;31msent by Token {}: \n\033[1;35m{}".format(
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}'))
                    print("\033[1;34m  - Time: {}".format(current_time))
                else:
                    print("\033[1;35m[x] MESSEGE FAILED PLEASE ENTER THE CORRECT TOKEN  {} of Convo \033[1;34m{} with Token \033[1;35m{}: \n\033[1;33m{}".format(
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}'))
                    print(" \033[1;34m - Time: {}".format(current_time))
                time.sleep(speed)   
            print("\n\033[1;32m[+] All messages sent. Restarting the process...\n")
        except Exception as e:
            print("\033[1;31m[!] An error occurred: {}".format(e))
def main():	
    print(logo)
    
    
    
    print(' \033[1;33m [•] 𝐄𝐍𝐓𝐄𝐑 𝐓𝐎𝐊𝐄𝐍 𝐅𝐈𝐋𝐄 :')
    token_file = input(BOLD + CYAN + "=>").strip()
    tokens = get_access_tokens(token_file)
    print(' \033[1;35m[•] 𝐄𝐍𝐓𝐄𝐑 𝐆𝐑𝐎𝐔𝐏 & 𝐈𝐍𝐁𝐎𝐗 𝐔𝐈𝐃 : ')
    convo_id = input(BOLD + CYAN + "=>").strip()
    print(' \033[1;34m[•] 𝐏𝐔𝐓 𝐍𝐏 𝐅𝐈𝐋𝐄 :')
    messages_file = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;31m[•] 𝐏𝐔𝐓 𝐇𝐀𝐓𝐄𝐑 𝐍𝐀𝐌𝐄 :')
    haters_name = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;35m[•] 𝐌𝐄𝐒𝐒𝐀𝐆𝐄 𝐃𝐄𝐋𝐀𝐘 𝐒𝐄𝐂𝐎𝐍𝐃 𝐓𝐈𝐌𝐄 :' )
    speed = int(input(BOLD + CYAN + "======> ").strip())
    with open(messages_file, 'r') as file:
        messages = file.readlines()
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    send_messages(convo_id, tokens, messages, haters_name, speed)
if __name__ == '__main__':
    main()
