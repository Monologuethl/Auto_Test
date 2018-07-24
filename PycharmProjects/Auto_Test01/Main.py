from ProcessRequest import OutPutExcel
import time
if __name__ == '__main__':
    start = time.clock()

    path = r'C:\Users\Tong\PycharmProjects\Auto_Test01\Excel\InterfaceCase(2).xls'
    result_path = r'C:\Users\Tong\PycharmProjects\Auto_Test01\Excel\Auto_Test.xls'
    out = OutPutExcel()
    List = out.output_excel(path)
    out.save_result(List, result_path, 0)
    elapsed = (time.clock() - start)

    print("Read file was used:%.2fs" % elapsed)
