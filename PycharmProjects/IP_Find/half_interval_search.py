from functools import reduce
from readExcel import readExcel

readIDC = readExcel(r"IDC IP地址.xlsx")
sheet1 = readIDC.get_sheet('Sheet1')

class half_search:

    def BinarySearch(array, t):
        low = 0
        height = len(array) - 1
        while low < height:
            mid = int((low + height) / 2)
            if array[mid] < t:
                low = mid + 1
            elif array[mid] > t:
                height = mid - 1
            else:
                return array[mid]
        return False

    @staticmethod
    def ip_into_init(hs_list):
        hs_int = []
        flag=0
        for hs in hs_list:
            sp=hs.split('.')
            for s in sp:
                try:
                    if 255 >= int(s) >= 0:
                        flag = 1
                    else:
                        flag=0
                except Exception as e:
                        print(e)
            if flag == 1:
                try:
                    hs_int.append(reduce(lambda x,y:(x<<8)+y,map(int,hs.split('.'))))
                except Exception as e:
                    print(e)
        hs_int.sort(reverse=True)
        print(hs_int)
        print(len(hs_int))

        return hs_int

