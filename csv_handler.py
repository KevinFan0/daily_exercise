f = open("历史发标查询失败次数名单-20181015.txt")
id_list = ""
for i in f.readlines():
    id_list += '"' + i + '",'
id_list = id_list.replace("\n", "")
print(id_list)