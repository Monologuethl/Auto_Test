# import ipaddress
# network = ipaddress.ip_network('117.131.199.4/6', False)
# address = ipaddress.ip_address('117.131.156.0')
# address2 =ipaddress.ip_network(u'117.131.215.146/147',False)
# print(address2)
# print(address in network)
# from functools import reduce
#
# ch3 = lambda x:sum([256**j*int(i) for j,i in enumerate(x.split('.')[::-1])])
# print(ch3('7.91.205.21'))
#
# def ip_into_int(ip):
#     return reduce(lambda x,y:(x<<8)+y,map(int,ip.split('.')))
#
#
# def is_same_network(ip, network):
#     network = network.split('/')
#     mask = ~(2**(32-int(network[1])) - 1)
#     return (ip_into_int(ip) & mask) == (ip_into_int(network[0]) & mask)
    # thrs = [threading.Thread(target=getContent.getIP(sheet1, sheet2,i*1000)) for i in range(1000)]
    # [thr.start() for thr in thrs]
    # [thr.join() for thr in thrs]
    # p = Pool(3)
    # for i in range(4):
    #     p.apply_async(getContent.getIP(sheet1, sheet2,i*250000), args=(i,))
    # print("Waiting for all subprocess done...")
    # p.close()
    # p.join()
    # print("All subprocess done.")
# from IPy import IP
# ip = IP('117.131.215.146/147')
#
# print(ip.len())
#
# for x in ip:
#     print(x)
# import netaddr
# startip = '64.233.56.37'
# endip = '64.233.56.215'
# cidrs = netaddr.iprange_to_cidrs(startip, endip)
# for k, v in enumerate(cidrs):
#     iplist = v
#     print (iplist)
def find_str(string, subStr, findCnt):
        list_str = string.split(subStr, findCnt)
        if len(list_str) <= findCnt:
            return False
        return len(string) - len(list_str[-1]) - len(subStr)

def get_sub_ip(string):
    str_list =string.split('-')
    if string.find('-')!=-1:
        for i in range(int(str_list[0])+1,int(str_list[1])):
            str_list.append(i)

    return str_list
# ip='117.131.215.118-121'
# N1=find_str(ip,'.',3)
# N2=find_str(ip,'-',1)
# str_list=[]
# # str_list=get_sub_ip(ip[N1+1:])
# ip_list=[]
# for i in str_list:
#     ip_list.append(ip[0:N1]+'.'+str(i))
# # print(ip_list)
ip=self.ip
N1=find_str(ip,'.', 3)
N2=find_str(ip,'-', 1)
N3=find_str(ip,'.', 2)

ip_list=ip.split(' ')
for i in range(1,len(ip_list)):
    if ip_list[i].find('.')!=-1:
        ip_list[i]=ip[0:N3]+'.'+ip_list[i]

print(ip_list)

str_list=[]

for i in ip_list:
    if i.find('.')!=-1:
        N=find_str(i,'.',3)
        str_list.append(i[N+1:])
    else:
        str_list.append(i)
print(str_list)
ip_list=[]
for i in range(len(str_list)):
            numeber=get_sub_ip(str_list[i])
            for j in numeber:
                ip_list.append(ip[0:N1]+'.'+str(j))

print(ip_list)
