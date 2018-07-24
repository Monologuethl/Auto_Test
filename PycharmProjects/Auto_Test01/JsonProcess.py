def json_process(List, range_list, i, check):
    flag = 0
    Error = []

    for list_content in List:
        if list_content:
            if isinstance(list_content, dict):
                for j in list_content:
                    if list_content[j] != "":
                        # 检查是否需要确定范围
                        if i in check:
                            for r in range(len(range_list)):
                                if range_list[r]:
                                    if j in range_list[r]:
                                        if float(range_list[r][j][1]) >= list_content[j] >= float(range_list[r][j][0]):
                                            flag = 1
                                        else:
                                            Error.append('['+j+':'+str(list_content[j])+']')
                                            print(Error[i])
                                    else:
                                        # print(j,list_content[j])
                                        flag = 1
                        else:
                            flag = 1
                    else:
                        flag = 0

                    dict1 = list_content[j]
                    if isinstance(dict1, dict):
                        for n in dict1:
                            if dict1[n] != "":
                                if i in check:
                                    for r in range_list(len(range_list)):
                                        if range_list[r]:
                                            if n in range_list[r]:
                                                if float(range_list[r][n][1]) >= list_content[n] >= float(range_list[r][n][0]):
                                                    flag = 1
                                                else:
                                                    Error.append('['+n+':'+str(list_content[n])+']')
                                                    print(Error[i])
                                else:
                                    flag = 1
                            else:
                                flag = 0

            if isinstance(list_content, list):
                for k in list_content:
                    if isinstance(k, dict):
                        dict2 = k
                        for v in dict2:
                            if dict2[v] != "":
                                if i in check:
                                    for r in range(len(range_list)):
                                        if range_list[r]:
                                            if v in range_list[r]:
                                                if float(range_list[r][v][1]) >= list_content[v] >= float(range_list[r][v][0]):
                                                    flag = 1
                                                else:
                                                    Error.append('['+v+':'+str(list_content[v])+']')
                                                    print(Error)
                                else:
                                    flag = 1
                            else:
                                flag = 0
        else:
            flag = 0
            
    if Error:
        flag = 0
    return flag, Error
