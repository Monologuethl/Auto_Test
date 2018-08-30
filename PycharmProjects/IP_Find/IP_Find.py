# -*- coding: UTF-8 -*-#
from functools import reduce
from multi_ip import serivalip_process
from readExcel import readExcel
from  half_interval_search import half_search
import ipaddress
import time

# import threading
# import os
# from multiprocessing import Pool

readIDC = readExcel(r"IDC IP地址.xlsx")
sheet1 = readIDC.get_sheet('Sheet1')

# readIP = readExcel(r"IP地址.xlsx")
# sheet2 = readIP.get_sheet('挑选大流量客户')

readIP = readExcel(r"ip.xlsx")
sheet2 = readIP.get_sheet('IP')


class getContent:
    @staticmethod
    def getIDC(sheet):
        ip_list = []
        for i in range(1, sheet.nrows):
            name = sheet.cell(i, 0).value
            ip = sheet.cell(i, 1).value
            sip = serivalip_process(ip, name)
            # 多行
            if ip !='':
                if ip.find('/') != -1:
                    ip_dict = sip.multi_line()
                # 单个ip
                elif ip.find('-') ==-1 and ip.find(' ')==-1:
                    ip_dict=sip.ip_dict
                # 单首地址单区间
                elif ip.find('-')!=-1 and ip.find(' ')==-1:
                    ip_dict = sip.single_one()
                # 单首地址多区间
                elif ip.find('-')!=-1 and ip.find(' ')!=-1:
                    ip_dict = sip.singleline_sip_section()
                # 多首地址多区间
                else:
                    ip_dict = sip.singleline_mip_section()
                ip_list.append(ip_dict)
        return ip_list

    @staticmethod
    def getIP(sheet1, sheet2):
        hs_list=[]
        count = 0
        start = time.clock()
        ip_list= getContent.getIDC(sheet1)
        for i in ip_list:
            for name in i :
                hs_list+=i[name]
        hs_int =  half_search.ip_into_init(hs_list)
        for i in range(sheet2.nrows):
            elapsed = (time.clock() - start)
            count = count + 1
            print("正在匹配中{0}---用时{1:0.01f}s".format(count, elapsed))
            try:
                beginip = ipaddress.ip_address(sheet2.cell(i, 0).value)
                endip = ipaddress.ip_address(sheet2.cell(i, 1).value)
                getContent.half_search_compare(beginip, endip, hs_int)
            except Exception as e:
                print(e)

    def half_search_compare(beginip, endip, hs_int):
        try:
            beginip = reduce(lambda x, y: (x << 8) + y, map(int, str(beginip).split('.')))
            # print(beginip)
            endip = reduce(lambda x, y: (x << 8) + y, map(int, str(endip).split('.')))
            # print(endip)
            mid_1 = half_search.BinarySearch(hs_int, beginip)
            mid_2 = half_search.BinarySearch(hs_int, endip)
            if mid_1:
                print('成功:' + str(mid_1) + '=======' + str(beginip))
            else:
                print('...')
            if mid_2:
                print('成功:' + str(mid_2) + '=======' + str(endip))
            else:
                print('...')
        except Exception as e:
            print(e)



if __name__ == '__main__':
    for name in getContent.getIDC(sheet1):
        print(name)
    # getContent.getIP(sheet1, sheet2)

