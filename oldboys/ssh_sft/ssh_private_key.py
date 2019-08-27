import paramiko

# id_rsa is the private key of the gao-03
# used to login the mimic for no secrect login
private_key = paramiko.RSAKey.from_private_key_file('id_rsa')

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname="10.20.223.198",port=22,username="mimic",pkey=private_key)

stdin,stdout,stderr = ssh.exec_command("df")

res,err = stdout.read(),stderr.read()

result = res if res else err

print(result.decode())