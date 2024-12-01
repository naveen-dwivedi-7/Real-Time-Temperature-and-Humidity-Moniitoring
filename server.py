import matplotlib.pyplot as plt
import socket

# Initialize the figure and axes outside the loop
plt.ion()  # Enable interactive mode
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
fig.suptitle('IoT Temperature and Humidity Monitor')
ax1.set_title('Temperature')
ax1.set_xlabel('Iteration')
ax1.set_ylabel('Temp ($^0 C$)')
ax1.grid()

ax2.set_title('Humidity')
ax2.set_xlabel('Iteration')
ax2.set_ylabel('Humidity ($\%$)')
ax2.grid()

def coverage_plot(data, i):
    hum = float(data.split(",")[0])  # Extract and convert humidity
    tem = float(data.split(",")[1])  # Extract and convert temperature
    print(f'temp={tem} iter={i}')
    
    # Clear and update temperature plot
    ax1.plot(i, tem, 'ro-', label='Temp' if i == 0 else "")
    ax1.legend()
    
    # Clear and update humidity plot
    ax2.plot(i, hum, 'bo-', label='Humidity' if i == 0 else "")
    ax2.legend()

    plt.pause(0.1)  # Pause to update the plot

# Create and bind a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.1.42', 10004)  # Replace with the server's IP and port
sock.bind(server_address)
i = 0

print("Server is listening on 192.168.1.42:10002...")

while True:
    try:
        data, address = sock.recvfrom(4096)  # Receive data
        mess = data.decode().strip()  # Decode and clean up the message
        with open("Datalog.txt", "a") as f:
            f.write(mess + "\n")
        coverage_plot(mess, i)
        print(f"Received from {address}: {mess}")
        i += 1
    except Exception as e:
        print(f"Error: {e}")
