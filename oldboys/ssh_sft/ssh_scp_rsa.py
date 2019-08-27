import paramiko


private_key = paramiko.RSAKey.from_private_key_file("id_rsa")

transport = paramiko.Transport(("10.20.223.198",22))
transport.connect(username="mimic",password="123456")

sftp = paramiko.SFTPClient.from_transport(transport)

sftp.put('documet','/home/mimic/document')
# sftp.get('/home/jor/nat_template.py','nat.py')

transport.close()

