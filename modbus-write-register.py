from pymodbus.client.sync import ModbusTcpClient
from datetime import datetime, time
import random
import time

#você deve colocar o ip do servidor que está em execução, tente: {ip a} para descobir o ip  
host = '192.167.100.1'  #ip of your raspberry pi 
port = 502
client = ModbusTcpClient(host, port)
while True:
    client.connect()
    data = random.randint(25,35)

#escrever os valores 
    list = []
    for i in range(10):
         data = random.randint(25,35)
         list.append(data)

    # write to multiple registers using list of data
    wr = client.write_registers(1000,list,unit=1)
    time.sleep(5) #tempo

    # criar os logs em formato .txt
    with open ('data.txt', 'a') as arquivo:
        for valor in [list]:
            arquivo.write(str(valor)+'\n')

