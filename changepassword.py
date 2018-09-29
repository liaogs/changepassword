#_*_ coding: utf-8 _*_
'''
@author liaogs
'''
import paramiko
import sys

class ChangePassword():
    def __init__(self,hostip,port,username,oldpass,newpass):
        self.hostip = hostip
        self.port = port
        self.username = username
        self.oldpass = oldpass
        self.newpass = newpass
        self.updateflag = False

    def run_change(self):
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        tasklist = []
        try:
            s.connect(hostname=self.hostip, port=self.port, username=self.username, password=self.oldpass)
            print ('"%s" is updating password' % self.hostip)
            stdin, stdout, stderr = s.exec_command('echo %s |passwd --stdin root' % self.newpass)
            r_message = stdout.read()
            if "successfully" in r_message:
                self.updateflag = True
                print('%s is successful' %self.hostip)
            else:
                print('%s is failed' %self.hostip)
                self.updateflag = False
            s.close()
        except Exception:
            self.updateflag = False
            print("connection error")

        tasklist = [self.hostip, self.port, self.username, self.oldpass, self.newpass, self.updateflag]
        return tasklist
