import requests
import json


class DynamicParameter:
    def __init__(self):
        self.url = 'http://120.209.138.229:3015/VixtelRest?subInterface=getAccessDataNode'

    # self.url = url

    def cityid2name(self, cityid):
        city_dict = {'0': '全省', '1': '合肥', '2': '芜湖', '3': '蚌埠', '4': '滁州', '5': '安庆',
                     '6': '六安', '7': '黄山', '8': '宣城', '9': '淮南', '10': '宿州', '11': '马鞍山',
                     '12': '铜陵', '13': '淮北', '14': '阜阳', '15': '池州', '17': '亳州'}
        if cityid in city_dict:
            if cityid != '0':
                return city_dict[cityid]
        return ''

    def request_data(self):
        try:
            res = requests.get(self.url, timeout=30)
            return res.text
        except Exception as e:
            print("Interface Connect Error - %s" % e)

    def get_sourceNodeId(self, cityname):
        return self.__get_nodeid('sourceNode', cityname, 'sourceNodeId')

    def get_destNodeId(self, cityname):
        return self.__get_nodeid('destNode', cityname, 'destNodeId')

    def __get_nodeid(self, nodetypename, cityname, nodename):
        if nodename == '' or nodename == None:
            return ''

        res = self.request_data()
        data = json.loads(res)
        if 'results' in data:
            if nodetypename in data['results']:
                if cityname in data['results'][nodetypename]:
                    if 'rows' in data['results'][nodetypename][cityname]:
                        return self.__get_node_value(data['results'][nodetypename][cityname]['rows'], nodename)
        return ''

    def __get_node_value(self, datal, nodename):
        value_list = []
        for i in range(0, len(datal)):
            if nodename in datal[i]:
                value_list.append(str(datal[i][nodename]))
        return value_list


def test():
    obj = DynamicParameter()
    res = obj.get_sourceNodeId('亳州')
    # res = obj.request_data()
    print(res)
    res2 = obj.get_destNodeId('亳州')
    print(res2)


if __name__ == '__main__':
    test()
