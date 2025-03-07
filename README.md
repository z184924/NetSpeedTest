# NetSpeedTest

net speed test tool

## Usage

1. Download the code
2. Run NetSpeedTest.py on the server
3. Run NetSpeedTest.py on the client (must carry parameters)
4. The server and client will automatically connect and start the speed test
5. The test results will be displayed on the terminal

### Parameter Description

Parameter 1: client/server (client/server) (required for client)

Parameter 2: Server IP address (required for client, default 0.0.0.0 for server, if you want to use ipv6, you can set it to ::)

Parameter 3: Server port number (optional, default 62345)

### Example

- Server

```shell
python NetSpeedTest.py
```

- Client

```shell
python NetSpeedTest.py client 192.168.1.1
```

## Notes

1. The IP address of the server and client must be in the same LAN

2. The port number of the server and client must be the same

## 中文说明

这是一个简单的网络速度测试工具，可以在服务器和客户端之间进行速度测试。

## 使用方法

1. 下载代码
2. 在服务器上运行NetSpeedTest.py
3. 在客户端上运行NetSpeedTest.py(须要携带参数)
4. 服务器和客户端会自动连接，并开始测速
5. 测速结果会显示在终端上

### 参数说明

参数1: client/server (客户端/服务器) (客户端必填)

参数2: 服务器IP地址(客户端必填,服务器端默认为0.0.0.0,如需使用ipv6,可设置为::)

参数3: 服务器端口号(可选,默认62345)

### 启动样例

- Server

```shell
python NetSpeedTest.py
```

- Client

```shell
python NetSpeedTest.py client 192.168.1.1
```

## 注意事项

1. 服务器和客户端的IP地址必须在一个局域网内
2. 服务器和客户端的端口号必须一致
