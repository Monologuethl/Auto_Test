# print("开始加载文件<<<<<<<<<<<<<<<<")
# book = xlrd.open_workbook(file_path)  # 文件名，把文件与py文件放在同一目录下
# sheet_names = book._sheet_names
# sheet_1_name = sheet_names[page_index]
# sheet = book.sheet_by_name(sheet_1_name)  # execl里面的表明
# print("当前页面为[[" + sheet_1_name + "]]")
# print("文件加载结束>>>>>>>>>>>>>>>>")

# rb = xlrd.open_workbook(path)
# r_sheet = rb.sheet_by_index(page_index)
# r = r_sheet.nrows
# wb = copy(rb)
# sheet = wb.get_sheet(page_index)

# import os
# #获取当前文件下指定后缀名的文件
# def getFileName(path):
#     f_list = os.listdir(path)
#     filename=[]
#     for i in f_list:
#         if os.path.splitext(i)[1] == '.xls':
#             filename.append(i)
#     return filename
#
# print(getFileName(os.getcwd()))
