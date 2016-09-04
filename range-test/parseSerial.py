import serial
import requests
import time
import json

#### some basic variables


baseURL = 'http://159.203.128.53'
#baseURL = 'https://data.sparkfun.com'

publicKey='KjqJ8gpeq1hzKlJjqm0KFPMGEVN'
privateKey='A9ypzYrKyATn7vg30OW7IGpzL3d'

serialPort="/dev/ttyUSB1"
serialBaud = 9600

loopDelay = 90 #seconds
endl="\n"

### convenience function for posting to Phant
def postPhant(line):
    x=line.strip()
    x=x.strip()
    x=x.split(",")
    if (len(x)==6):
        timeVar=x[0]
        temp=float(x[1])
        pres=float(x[2]) 
        rh=float(x[3])
        tempc=float(x[4])
        tempf=float(x[5])

        pushUrl = baseURL+'/input/'+str(publicKey)+'?private_key='+str(privateKey)+'&datetime='+str(timeVar)+'&temperature='+str(temp)+'&pressure='+str(pres)+'&humidity='+str(rh)+'&tempc='+str(tempc)+'&tempf='+str(tempf)

        print pushUrl
        push = requests.get(pushUrl)
        
        return push.status_code
        
###### open and flush serial port

ser = serial.Serial(serialPort, serialBaud)
#print "Waiting for serial port ..."
time.sleep(3)
ser.flush() # flush to ge rid of extraneous char

###### main loop 

f = open('log.txt','a')

while True:

    cmd = "READ"
    cmd = cmd.strip() + endl
    ser.write(cmd.encode())
    line = ser.readline()
    line=line.decode('utf-8')
    
    #print 'raw serial input: ', line
    
    if (line.startswith("{")):
        data = json.loads(line)
        rssi=data["RSSI"]
        year = data["packet"]["date"]["y"]
        month = data["packet"]["date"]["mon"]
        day = data["packet"]["date"]["d"]
        hour = data["packet"]["date"]["h"]
        minute = data["packet"]["date"]["min"]
        second = data["packet"]["date"]["s"]
        lat = data["packet"]["loc"]["lat"]
        lon = data["packet"]["loc"]["lon"]
        
        outline= str(year)+"-"+str(month)+"-"+str(day)+" "+str(hour)+":"+str(minute)+":"+str(second)+","+str(rssi)+","+str(lat)+","+str(lon)
        
        f.write(outline)
        f.write('\n')
        
        print outline
        #print "lat=", data["data"]["lat"]
    
   

