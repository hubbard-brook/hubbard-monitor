import serial

ser = serial.Serial("/dev/ttyUSB0", 9600)
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
    #print x.split(",")
    #x = x.strip() 
    #x = x.replace(",","") 
    #x=x.split(":")
