from OutPut import OutPutExcel

if __name__ == '__main__':
    path = r'C:\Users\Tong\PycharmProjects\AutoTest\Excel\InterfaceCase.xls'
    result_path = r'C:\Users\Tong\PycharmProjects\AutoTest\Excel\Auto_Test.xls'
    out = OutPutExcel()
    list = out.output_excel(1, path)
    out.save_result(list, result_path, 0)
