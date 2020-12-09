from mcstatus import MinecraftServer as MineS
import os
import time

server = MineS.lookup("Odenwald-Verl.de:25565")
print("Up")

while(True):
    try:
        ping = server.ping()
        #print(ping)
    except:
        print("Starte Server...")
        os.system("java -Xmx5120M -Xms5120M -jar /root/server.jar nogui")
    time.sleep(10)