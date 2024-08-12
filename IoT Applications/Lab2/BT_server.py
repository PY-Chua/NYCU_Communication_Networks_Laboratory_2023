import bluetooth

server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port=2

#B8:27:EB:74:0E:EF 
server_sock.bind(("B8:27:EB:74:0E:EF", port))
server_sock.listen(1) #可接受多少連線

client_sock,address = server_sock.accept()
print "Accepted connection from ",address

data = client_sock.recv(1024)
print "received [%s]" % data

client_sock.close()
server_sock.close()
