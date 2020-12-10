from mcstatus import MinecraftServer as MineS
import os
import time
from datetime import datetime
from datetime import date

server = MineS.lookup("192.168.178.143")

logFile = open("Crash_Log.txt", "a")
now = datetime.now()
today = date.today()


while(True):
    try:
        ping = server.ping()
        print(ping)
    except:
        with open("Crash_Log.txt", "a") as logFile:
            logFile.write(today.strftime("%D ") + now.strftime("[%H:%M:%S]" + " The Server is (re)starting"))
        print("Starte Server...")
        os.system("java -Xmx5120M -Xms5120M -jar /root/server.jar nogui")
    time.sleep(10)
