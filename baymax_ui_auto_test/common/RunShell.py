import paramiko
class ConnectShell:

    def remotConnect(self):
        # 服务器相关信息,下面输入你个人的用户名、密码、ip等信息
        ip = "192.168.1.199"
        port = 22
        user = "merce"
        password = "merce"

        # 创建SSHClient 实例对象
        ssh = paramiko.SSHClient()
        # 调用方法，表示没有存储远程机器的公钥，允许访问
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接远程机器，地址，端口，用户名密码
        ssh.connect(ip, port, user, password, timeout=10)
        # 输入linux命令
        rm1 = "hadoop fs -rm -r /tmp/lisatest/rtc_1/*"
        rm2 = "hadoop fs -rm -r /tmp/lisatest/kafka_hdfs_rtc*/*"
        stdin, stdout, stderr = ssh.exec_command(rm1)
        result = stdout.read()
        print(result)
        stdin, stdout, stderr = ssh.exec_command(rm2)
        # 输出命令执行结果
        result = stdout.read()
        print(result)
        # 关闭连接

if __name__ == "__main__":
    test=ConnectShell()
    test.remotConnect()