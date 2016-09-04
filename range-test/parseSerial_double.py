import serial
import requests
import time
import json

#### some basic variables

serialPort_0="/dev/ttyUSB0" # the RFM69 moteino
serialPort_1="/dev/ttyUSB1" # the LoRa moteino
serialBaud = 9600

ser0 = serial.Serial(serialPort_0, serialBaud)
ser1 = serial.Serial(serialPort_1, serialBaud)

ser0.flush()
ser1.flush()


###### main loop 

f0 = open('log0.txt','a')
f1 = open('log1.txt','a')

while True:

    line0 = ser0.readline()
    line0 = line0.decode('utf-8')
    
    line1 = ser1.readline()
    line1 = line1.decode('utf-8')
    
    #print "0:", line0
    #print "1:", line1
    
    line0=line0.strip()
    line0=line0.split(",")
    
    if len(line0)==6:
       time = line0[0]
       lat = float(line0[1])/1000000
       lon = float(line0[2])/1000000
       alt = float(line0[3])/1000000
       temp = float(line0[4])/100
       humid=float(line0[5])/100
       
       date="16-9-4"
       
       outline0=str(date)+" "+time+","+str(lat)+","+str(lon)+","+str(alt)+","+str(temp)+","+str(humid)
       f0.write(outline0)
       f0.write('\n')
       
       print "RFM69:", outline0

    
    if (line1.startswith("{")):
        data = json.loads(line1)
        rssi=data["RSSI"]
        year = data["packet"]["date"]["y"]
        month = data["packet"]["date"]["mon"]
        day = data["packet"]["date"]["d"]
        hour = data["packet"]["date"]["h"]
        minute = data["packet"]["date"]["min"]
        second = data["packet"]["date"]["s"]
        lat = data["packet"]["loc"]["lat"]
        lon = data["packet"]["loc"]["lon"]
        
        outline1= str(year)+"-"+str(month)+"-"+str(day)+" "+str(hour)+":"+str(minute)+":"+str(second)+","+str(lat)+","+str(lon)+","+str(rssi)
        
        f1.write(outline1)
        f1.write('\n')
        
        print  "LoRa:", outline1
        
        
    print '\n'
   

