import pexpect
import sys
import paramiko
import re
import zentalk.mailZentalkServerStatus as zen
import time
import zentalk.zenDB
#检查zentalk服务器状态
#tomcat 硬盘容量 drdb状态


def connect(ip, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(ip, 22, username, password, timeout=5)
        return ssh
    except:
        print("GET CONNECT ERROR")
        sys.exit()


def exec(handle, cmd):
    stdin, stdout, stderr = handle.exec_command(cmd)
    return stdout.readlines()

config = zentalk.zenDB.config

content = ''

for host in config['web']:
    ssh = connect(host['ip'], host['username'], host['password'])
    results = exec(ssh, "ps aux|grep tomcat")
    print(host['name'], "\n\r")
    content = content + host['name'] + "\n\r"

    tomcat = '无法获取tomcat状态'
    for line in results:
        m = re.search('jdk1\.7\.0_79', line)
        if m is not None:
            tomcat = "tomcat正常:\n\r" + line
            break
    print(tomcat)
    content = content + tomcat + "\n\r"

    results = exec(ssh, "df -h")
    print("硬盘容量:")
    content = content + "硬盘容量:" + "\n\r"

    path = ''
    for i, line in enumerate(results):
        m = re.findall("(\d+)%", line)
        if m and int(m[0]) >= 60:
            print(path, line)
            content = content + path + line + "\n\r"

    print("----------------------")
    content = content + "----------------------" + "\n\r"

    ssh.close()


for host in config['nfs']:
    ssh = connect(host['ip'], host['username'], host['password'])
    results = exec(ssh, "service drbd status")
    print(host['name'], "\n\r")
    content = content + host['name'] + "\n\r"

    print('drbd状态:')
    content = content + 'drbd状态:' + "\n\r"

    for line in results:
        print(line)
        content = content + line + "\n\r"

    results = exec(ssh, "df -h")
    print("硬盘容量:")
    content = content + "硬盘容量:" + "\n\r"

    path = ''
    for i, line in enumerate(results):
        m = re.findall("(\d+)%", line)
        if m and int(m[0]) >= 60:
            print(path, line)
            content = content + path + line + "\n\r"

    print("----------------------")
    content = content + "----------------------" + "\n\r"

    ssh.close()


for host in config['db']:
    ssh = connect(host['ip'], host['username'], host['password'])
    print(host['name'], "\n\r")
    content = content + host['name'] + "\n\r"

    results = exec(ssh, "df -h")
    print("硬盘容量:")
    content = content + "硬盘容量:" + "\n\r"

    path = ''
    for i, line in enumerate(results):
        m = re.findall("(\d+)%", line)
        if m and int(m[0]) >= 60:
            print(path, line)
            content = content + path + line + "\n\r"

    print("----------------------")
    content = content + "----------------------" + "\n\r"
    ssh.close()


mail = zen.SendMail()
date= time.strftime('%Y/%m/%d',time.localtime(time.time()))
mail.sendTestMail("zentalk服务器日常检查"+date,content)