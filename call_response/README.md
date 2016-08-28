# Setup

1. Place the folder "Arduino_SerialCommand" inside the "libraries" folder of your Arduino IDE "sketchbook" folder.  You'll need to restart the Arduino IDE after this.
2. Load "serialCommand.ino" onto your Ardunio.
3. Modify the parameters in log2phant.py to match your use-case.  In particular:

```python
baseURL = 'https://data.sparkfun.com'

publicKey='KjqJ8gpeq1hzKlJjqm0KFPMGEVN'
privateKey='A9ypzYrKyATn7vg30OW7IGpzL3d'

serialPort="/dev/ttyUSB1"
serialBaud = 9600

loopDelay = 9 #seconds
```
# Usage

Run 'log2phant.py' from the terminal with superuser priveleges:

```bash
sudo python log2phant.py
```

# Debugging

You can comment out the postPhant() functionality, in order to make sure that you're reading from the serial connection properly.  See lines 64 and 65:

```python
# status = postPhant(line)
# print "status =", status
```


