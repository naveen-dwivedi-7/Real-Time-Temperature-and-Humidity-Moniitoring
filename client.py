import time
import adafruit_dht
import board
import socket 

dht_device = adafruit_dht.DHT11(board.D4)
#dht_device = adafruit_dht.DHT11(board.D4, use_pulseio=False)


def sensordata():
	temperature = dht_device.temperature
	humidity = dht_device.humidity
	return temperature, humidity



sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.1.42', 10004)  # Replace with server's IP and port

try:
    while True:
        h, t = sensordata()
        message = str(h) + ',' + str(t)  # Prepare the message
        print(f'sending "{message}"')  # Log the message
        sock.sendto(message.encode(), server_address)  # Send data
finally:
    print('closing socket')  # Log closure
    sock.close()  # Close the socket

