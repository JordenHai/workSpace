import paramiko

transport = paramiko.Transport(("10.20.220.105",22))
transport.connect(username="jor",password="123456")

sftp = paramiko.SFTPClient.from_transport(transport)

sftp.put('ji','/home/jor/document')
sftp.get('/home/jor/nat_template.py','nat.py')

transport.close()

