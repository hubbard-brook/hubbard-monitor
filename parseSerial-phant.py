import serial
import urllib2
import time

publicKey='q58QKrwpJnTJo5VOAKAK'
privateKey='BVeXMPmnBRfPYxgD2Z2Z'


ser = serial.Serial("/dev/ttyUSB1", 9600)
while True:
    x = ser.readline()
    #print 'raw serial input: ', x
    x=x.strip()
    x=x.split(",")
    if (len(x)==6):
        time=x[0]
        lat=float(x[1])/1000000.
        lon=float(x[2])/1000000. 
        alt=float(x[3])/100000.
        temp=float(x[4])/100.
        rh=float(x[5])/100.
        print "Time: %s GMT" % time
        print "lat: %10.6f lon: %10.6f alt: %8.2f" % (lat,lon,alt)
        print "temp: %6.2f rh: %6.2f" % (temp, rh) 
        print "-------------"

        sentence = 'https://data.sparkfun.com/input/'+str(publicKey)+'?private_key='+str(privateKey)+'&temp='+str(temp)+'&humidity='+str(rh)
        print sentence

        url_response=urllib2.urlopen(sentence)
        
        print url_response
 
        #time.sleep(15)
