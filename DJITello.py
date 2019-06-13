import threading
import socket
import sys
import time
import platform

host = ''# OLD
port = 9000# OLD
locaddr = (host, port)# OLD
python_version = str(platform.python_version())# OLD
version_init_num = int(python_version.partition('.')[0])# OLD


def print_help():
    print ("This program run with Python3")
    print ("--------------CONTROL COMMANDS----------------")
    print ("Insert a command and wait the ok or error code")
    print ("[t]ake off To take off")
    print ("[l]and to land")
    print ("[e]mergency to stop all motors immediately")
    print("--------------READ COMMANDS----------------")
    print ("[b]attery get battery porcentage")
    print ("[a]ltitude get altitude")
    print ("[k]ill the drone")
    print ("[q]uit")
    print ("[h]elp")


print_help()


if version_init_num == 3:# OLD
            #msg = input("");# OLDt

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)# OLD

    tello_address = ('192.168.10.1', 8889)# OLD

    sock.bind(locaddr)# OLD

    def sendcomand(comand):
        print(comand)
        comand = comand.encode(encoding="utf-8")# OLD
        sent = sock.sendto(comand, tello_address)# OLD
        print(comand)

    def kill():
        print ("Killing the drone")
        sendcomand("up 500")
        print ("Up to the sky....")
        time.sleep(5)
        sendcomand("emergency")
        print("Stopping the motors....")

    def recv():# OLD
        count = 0# OLD
        while True:# OLD
            try:# OLD
                data, server = sock.recvfrom(1518)# OLD
                print(data.decode(encoding="utf-8"))# OLD
            except Exception:# OLD
                print('\nExit . . .\n')# OLD
                break# OLD


    # recvThread create
    recvThread = threading.Thread(target=recv)# OLD
    recvThread.start()# OLD
    sendcomand('command')
    comand=''
    while True:# OLD
        try:# OLD
            msg = input("HackinTello# ");
            if msg.strip() != "":
                d = msg.split(" ")
                if d[0] == "t":
                    comand = 'takeoff'

                elif d[0] == "l":
                    comand = 'land'

                elif d[0] == "e":
                    comand = 'emergency'

                elif d[0] == "b":
                    comand = 'battery?'

                elif d[0] == "a":
                    comand = 'attitude?'

                elif d[0] == "w":
                    comand = 'wifi?'

                elif d[0] == "k":
                    kill()

                elif d[0] == "q":
                    print('...')
                    sock.close()
                    break

                elif d[0] == "h":
                    print_help()
                    comand = ''

                else:
                    print_help()
                    comand = ''

            if comand != '':
                sendcomand(comand)


        # Send data

        except KeyboardInterrupt:# OLD
            print('\n . . .\n')# OLD
            sock.close()# OLD
            break# OLD
else:
    print ("Error detected you no are ina a python3 enviroment")

