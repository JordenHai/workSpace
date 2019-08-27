import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#明文实现的ssh连接
ssh.connect(hostname="10.20.220.105",port="22",username="jor",password="123456")

stdin,stdout,stderr = ssh.exec_command('df')

res,err = stdout.read(),stderr.read()
result = res if res else err

print(result.decode())
print()
ssh.close()

#
# not found in Konwn hosts
# (RSA) to the list of the Know Hosts