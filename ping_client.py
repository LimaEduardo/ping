import socket
import os
import time



udp_ip = "177.105.60.80"
udp_port = 5002

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

number_of_tries_original = 20
number_of_tries = 20
random_string = os.urandom(64)
sock.settimeout(0.250)
rtts = []

while number_of_tries != 0:
  time.sleep(1)
  try:
    rtt_begin = time.time()
    sock.sendto(random_string, (udp_ip, udp_port))
    response = sock.recvfrom(1024)
    rtt_end = time.time()
    rtt_final = (rtt_end - rtt_begin) * 1000
    print(str(len(random_string)) + " bytes from "+str(udp_ip)+":"+str(udp_port)+"  time="+str(rtt_final)+" ms")
    rtts.append(rtt_final)

  except socket.timeout:
    print("Timeout")
  
  number_of_tries -= 1

average_time = (sum(rtts) / len(rtts))
print(str(number_of_tries_original) + " Packets transmitted, ",end="")
print(str(len(rtts)) + " received, ",end="")
print(str(number_of_tries_original - len(rtts)) + " lost, ",end="")
print(str((len(rtts) / number_of_tries_original) * 100) + "% packet loss, ",end="")
print("Average RTT time: " + str(average_time))