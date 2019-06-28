#!/usr/bin/env python

#start configuring the Switch
import sys
import telnetlib
import getpass

HOST=raw_input("Enter your switch ip_address:")
username=raw_input("Enter your remote username:")
password=getpass.getpass()

tn=telnetlib.Telnet(HOST)

tn.read_until("Username:")
tn.write(username +"\n")
if password:
    tn.read_until("Password:")
    tn.write(password +"\n")
print "Configuring switch:" + HOST

tn.write("config t\n")
for n in range(2,19):
    tn.write("vlan "+str(n) + "\n")
    tn.write("name spu.mks.vlan_"+ str(n) + "\n")
    tn.write("exit\n")
tn.write("end\n")
tn.write("exit\n")
print tn.read_all()
#showing the configs
tn.write("show run\n")
tn.write("exit\n")
readoutput=tn.read_all()
saveoutput=open("switch"+ HOST,"w")
saveoutput.write(readoutput)
saveoutput.close()
#end of the switchconfig

#start configuring the router
HOSTR=raw_input("Enter your router ip_address:")
username=raw_input("Enter your remote username:")
password=getpass.getpass()

tr=telnetlib.Telnet(HOSTR)
tr.read_until("Username:")
tr.write(username +"\n")
if password:
    tr.read_until("Password:")
    tr.write(password +"\n")

print "Configuring router: " + HOSTR
tr.write("config t\n")
tr.write("router rip\n")
tr.write("version 2\n")
tr.write("network 1.1.1.1\n")
tr.write("end\n")
tr.write("exit\n")
print tr.read_all()

tr.write("show run\n")
readoutput=tr.read_all()
saveoutput=open("switch"+ HOST,"w")
saveoutput.write(readoutput)
saveoutput.close()
