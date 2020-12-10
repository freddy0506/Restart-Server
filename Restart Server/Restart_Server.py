from mcstatus import MinecraftServer as MineS
import os
import time
from datetime import datetime
from datetime import date

server = MineS.lookup("www.de")


row = 0

while(True):
    try:
        ping = server.ping()
        print(ping)
    except:
        with open('Crash_Log.txt', 'a') as file:
            #file.write(row * "\n")
            #row += 1
            now = datetime.now()
            today = date.today()
            file.write(today.strftime("%D ") + now.strftime("[%H:%M:%S]" + " The Server is (re)starting\n"))
        
        print("Starte Server...")
        os.system("java -Xmx5120M -Xms5120M -jar /root/server.jar nogui")
    time.sleep(1)
