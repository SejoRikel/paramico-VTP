#!/usr/bin/env python
import paramiko
import time


ip_address=raw_input("Enter your host ip_address:")
username=raw_input("Enter your remote username:")
password=raw_input("Enter your remote password:")

ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print "connection to "+ ip_address + "Successful\n"

remote_connection=ssh_client.invoke_shell()

remote_connection.send("config t\n")
remote_connection.send("ho demo_admin\n")
remote_connection.send("vtp mode server\n")
remote_connection.send("vtp domain spu\n")
remote_connection.send("vtp password class\n")
remote_connection.send("end\n")
remote_connection.send("exit\n")
time.sleep(1)


output=remote_connection.recv(65535)

print output

ssh_client.close()
