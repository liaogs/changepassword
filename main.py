#_*_ coding: utf-8 _*_
'''
@author liaogs
'''
import re
import sys
from excelhandler import excelhandler
from changepassword import ChangePassword

if __name__ == '__main__':
    if len(sys.argv) == 1:
        eh = excelhandler("pass.xlsx")
    else:
        eh = excelhandler(sys.argv[1])
    eh.read_excel()

    def updatepassword():
        ret = eh.get_server_list()
        tasklist = []
        for i in range(len(ret)):
            print(ret[i][0],ret[i][2],ret[i][1],ret[i][3],ret[i][4])
            cp = ChangePassword(hostip=ret[i][0],port=int(ret[i][2]),username=ret[i][1],oldpass=ret[i][3],newpass=ret[i][4])
            task = cp.run_change()
            tasklist.append(task)

        print(tasklist)
        eh.write_excel(tasklist)

    while True:
        inp = input("1、生成密码 2、更新密码>>")
        if str(inp) == "1":
            eh.gen_new_password_excel()

        elif str(inp) == "2":
            updatepassword()

        elif inp == "exit":
            exit()
        else:
            continue