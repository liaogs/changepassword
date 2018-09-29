#_*_ coding: utf-8 _*_
'''
@author liaogs
'''
import json
import xlrd
import xlwt
import time
import datetime
import base64
import random
from xlutils.copy import copy


class excelhandler():
    def __init__(self,path):
        self.path = path
        self.workbook = None
        self.rows = 0
        self.cols = 0
        self.serverlist = []

    def read_excel(self):
        self.workbook = xlrd.open_workbook(self.path)
        sh1 = self.workbook.sheet_by_index(0)
        self.rows = sh1.nrows
        self.cols = sh1.ncols
        for row in  range(1,sh1.nrows):
            server = []
            for col in [0,1,2,sh1.ncols-2,sh1.ncols-1]:
                server.append(sh1.cell(row,col).value)

            self.serverlist.append(server)

    def gen_new_password_excel(self):
        old_excel = xlrd.open_workbook(self.path)
        new_excel = copy(old_excel)
        ws = new_excel.get_sheet(0)
        coldt = "pass"+ str(datetime.date.today())
        ws.write(0,self.cols,coldt)
        for row in range(1,self.rows):
            ws.write(row,self.cols,self.gen_key())
        dt = time.strftime("%Y%m%d%H%M%S",time.localtime())
        new_excel.save(dt+self.path)


    def write_excel(self,serverlist):
        wb = xlwt.Workbook()
        ws = wb.add_sheet(u'sheet1',cell_overwrite_ok=True)
        header = ["IP","PORT","USERNAME","OLDPASS","NEWPASS","FLAG"]
        for col in range(0,6):
            ws.write(0,col,header[col])
        for row in range(len(serverlist)):
            for col in range(0,6):
                ws.write(row+1,col,serverlist[row][col])
        dt = time.strftime("%Y%m%d%H%M%S", time.localtime())
        wb.save(dt+".xlsx")

    def get_server_list(self):
        return self.serverlist

    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.cols

    def gen_key(self):
        pool = "1234567890abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM"
        length = len(pool)
        key = ""
        for i in range(28):
            c = random.randint(0,length)
            key += pool[c:c+1]
        return key





