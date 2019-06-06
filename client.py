
import bluetooth

serverMAC = 'B8:27:EB:E6:3B:B6'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMAC, port))
while 1:
    text = input()
    if text == "quit":
        break
    s.send(text)
s.close()
