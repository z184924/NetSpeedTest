# -*- coding: utf-8 -*-
import socket
import time
import sys

bind_ip = "0.0.0.0"
bind_port = 62345
print_append_config = False


def print_speed(speed, explain, append):
    if (sys.version_info.major == 2) or print_append_config:
        append = True
    if append:
        if speed < 1024:  # speed is in Bps
            print("\r" + explain + " Speed: %s Bps" % speed)
        elif speed < (1024 * 1024):  # speed is in KBps
            print("\r" + explain + " Speed: %s KBps" % (speed / 1024))
        elif speed < (1024 * 1024 * 1024):  # speed is in MBps
            print("\r" + explain + " Speed: %s MBps" % (speed / (1024 * 1024)))
        else:  # speed is in GBps
            print("\r" + explain + " Speed: %s GBps" % (speed / (1024 * 1024 * 1024)))
    else:
        if speed < 1024:  # speed is in Bps
            sys.stdout.write("\r" + explain + " Speed: " + str(speed) + " Bps                                ")
        elif speed < (1024 * 1024):  # speed is in KBps
            sys.stdout.write("\r" + explain + " Speed: " + str(speed / 1024) + " KBps                        ")
        elif speed < (1024 * 1024 * 1024):  # speed is in MBps
            sys.stdout.write("\r" + explain + " Speed: " + str(speed / (1024 * 1024)) + " MBps               ")
        else:  # speed is in GBps
            sys.stdout.write("\r" + explain + " Speed: " + str(speed / (1024 * 1024 * 1024)) + " GBps        ")


def server_program(host, port):

    print(socket.gethostname() + "\tStrating Server...")

    # 创建一个 socket 对象
    if ":" in host:
        server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    else:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定端口
    server_socket.bind((host, port))

    # 设置最大连接数，超过后排队
    server_socket.listen(1)

    client_socket, addr = server_socket.accept()

    print("Connenct Clinet: %s" % str(addr))

    program_data = 0
    program_start = time.time()

    total_data = 0
    start = time.time()

    try:
        while True:
            data = "1" * 1024  # 1KB of data to be sent

            client_socket.send(data.encode("utf-8"))

            total_data += len(data)
            program_data += len(data)
            current_time = time.time()
            if current_time - start >= 1:  # 每秒打印一次
                speed = total_data / (current_time - start)
                print_speed(speed, "Upload", False)
                start = current_time
                total_data = 0  # 重置计数器
    except:
        client_socket.close()
    finally:
        current_time = time.time()
        speed = program_data / (current_time - program_start)
        print_speed(speed, "Avg Upload", True)


def client_program(host, port):
    # 创建一个 socket 对象
    if ":" in host:
        client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    else:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务，指定主机和端口
    client_socket.connect((host, port))

    program_data = 0
    program_start = time.time()
    total_data = 0
    start = time.time()

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            total_data += len(data)
            program_data += len(data)
            current_time = time.time()
            if current_time - start >= 1:  # 每秒打印一次
                speed = total_data / (current_time - start)
                print_speed(speed, "Downdload", False)
                start = current_time
                total_data = 0  # 重置计数器
    except:
        # print(Exception.with_traceback())
        client_socket.close()
    finally:
        current_time = time.time()
        speed = program_data / (current_time - program_start)
        print_speed(speed, "Avg Downdload", True)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        mode = sys.argv[1]
    elif len(sys.argv) == 3:
        mode = sys.argv[1]
        bind_ip = sys.argv[2]
    elif len(sys.argv) == 4:
        mode = sys.argv[1]
        bind_ip = sys.argv[2]
        bind_port = int(sys.argv[3])
    else:
        server_program(bind_ip, bind_port)
    if mode == "server":
        server_program(bind_ip, bind_port)
    elif mode == "client":
        client_program(bind_ip, bind_port)
