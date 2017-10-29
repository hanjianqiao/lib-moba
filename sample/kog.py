
#!/usr/local/bin/python3

# coding: utf-8

import socket
import time
server_address = ('0.0.0.0', 9090)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server_address)
sock.listen(1)

connection, client_address = sock.accept()


def back_home():
    connection.send(b'input keyevent 3\n')



def swipe_left():
    connection.send(b'input swipe 200 1000 900 1000 200\n')


def swipe_right():
    connection.send(b'input swipe 900 1000 200 1000 200\n')



def tap_item(row, col):
    cmd_str = 'input tap ' + str(150+250*col) + ' ' + str(170+row*300) + '\n'
    connection.send(cmd_str.encode())



def tap_at(x, y):
    cmd_str = 'input tap ' + str(x) + ' ' + str(y) + '\n'
    connection.send(cmd_str.encode())


def start_game():
    tap_at(965, 887)


def close_welcom():
    tap_at(1615, 177)


def close_anu():
    tap_at(1685, 56)


def main_select_pvp():
    time.sleep(2)
    tap_at(590, 520)
    time.sleep(2)
    tap_at(490, 520)
    time.sleep(2)
    tap_at(420, 580)


def quit_vanus():
    connection.send(b'exit\n')

def mi_kog_sample_0():
    back_home()
    time.sleep(1)
    back_home()
    time.sleep(1)
    swipe_right()
    time.sleep(2)
    swipe_right()
    time.sleep(2)
    tap_item(0, 1)
    time.sleep(15)
    start_game()
    time.sleep(8)
    close_welcom()
    time.sleep(1)
    close_welcom()
    time.sleep(1)
    #close_welcom()
    #time.sleep(1)
    #close_anu()
    #time.sleep(1)
    main_select_pvp()

mi_kog_sample_0()




