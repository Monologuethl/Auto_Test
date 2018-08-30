import ipaddress
import re
import half_interval_search as hs

class serivalip_process:

    def __init__(self, ip, name):
        self.ip = ip
        self.name = name
        self.ip_dict = {name: self.ip}

    def get_sub_ip(string):
        str_list=[]
        if string.find('-')!=-1:
            str_list =string.split('-')
            for i in range(int(str_list[0])+1,int(str_list[1])):
                str_list.append(i)
        return str_list

    def find_str(string, subStr, findCnt):
        list_str = string.split(subStr, findCnt)
        if len(list_str) <= findCnt:
            return -1
        return len(string) - len(list_str[-1]) - len(subStr)

    @staticmethod
    def get_ip_network(dict):
        hs_list = []
        for name in dict:
            if isinstance(dict[name], str):
                try:
                    for x in ipaddress.ip_network(dict[name]):
                        hs_list.append(str(x))
                except Exception as e:
                    print(e)
            if isinstance(dict[name], list):
                for ip in dict[name]:
                    try:
                        for x in ipaddress.ip_network(ip):
                            hs_list.append(str(x))
                    except Exception as e:
                        print(e)
        for hs in hs_list:
            if hs == '':
                hs_list.remove(hs)
        print(hs_list)
        return hs_list

    def single_one(self):
        ip_list=[]
        N1=serivalip_process.find_str(self.ip, '.', 3)
        N2=serivalip_process.find_str(self.ip, '-', 1)
        str_list=serivalip_process.get_sub_ip(self.ip[N1+1:])
        for i in str_list:
            ip_list.append(self.ip[0:N1]+'.'+str(i))
        self.ip_dict={self.name:ip_list}
        return self.ip_dict

    def singleline_sip_section(self):
        ip=self.ip
        N1=serivalip_process.find_str(ip,'.',3)
        N2=serivalip_process.find_str(ip,'-',1)
        ip_list=ip.split(' ')
        str_list=[]
        for i in ip_list:
            if i.find('.')!=-1:
                i=i[N1+1:]
            str_list.append(i)
        ip_list=[]
        for i in range(len(str_list)):
            numeber=serivalip_process.get_sub_ip(str_list[i])
            for j in numeber:
                ip_list.append(ip[0:N1]+'.'+str(j))
        self.ip_dict={self.name:ip_list}
        return self.ip_dict

    def singleline_mip_section(self):
        ip=self.ip
        N1=serivalip_process.find_str(ip,'.', 3)
        N2=serivalip_process.find_str(ip,'-', 1)
        N3=serivalip_process.find_str(ip,'.', 2)

        ip_list=ip.split(' ')
        for i in range(1,len(ip_list)):
            if ip_list[i].find('.')!=-1:
                ip_list[i]=ip[0:N3]+'.'+ip_list[i]
        str_list=[]
        for i in ip_list:
            if i.find('.')!=-1:
                N=serivalip_process.find_str(i,'.',3)
                str_list.append(i[N+1:])
            else:
                str_list.append(i)
        ip_list=[]
        for i in range(len(str_list)):
                    numeber=serivalip_process.get_sub_ip(str_list[i])
                    for j in numeber:
                        ip_list.append(ip[0:N1]+'.'+str(j))

        self.ip_dict={self.name:ip_list}
        return self.ip_dict

    def multi_line(self):
        if self.ip.find(r'\n')!=-1:
            ip_list = re.split(r'\n', self.ip)
            self.ip_dict = {self.name: ip_list}
            ip_list=serivalip_process.get_ip_network(self.ip_dict)
            self.ip_dict ={self.name:ip_list}
        else:
            ip_list=serivalip_process.get_ip_network((self.ip_dict))
            self.ip_dict={self.name:ip_list}
        return self.ip_dict
