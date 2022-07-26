from pymodbus.client.sync import ModbusTcpClient
from datetime import datetime, time
import random
import json
import time


#  object datetime que contém date and time
def current_time():
    now = datetime.now().isoformat()
    return now

host = '192.167.100.1'   #você deve colocar o ip do servidor que está em execução, tente: {ip a} para descobir o ip  
port = 502
client = ModbusTcpClient(host, port)
while True:
    client.connect()

    rr = client.read_holding_registers(1000,10,unit=1)
 
    data = {
        "datetime": current_time(),
        "data": rr.registers    # register will return a list. To query individual register specify the array item e.g. registers[0] to get value from first register

    }
    print(json.dumps(data))
    time.sleep(5)