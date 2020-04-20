import os
import pdb

# filepath1 = "第一次出现的写入的文件名"
# filepath2 = "重复出现的写入文件名"

filepath1 = "/home/fandong/test/name.txt"
filepath2 = "/home/fandong/test/chongfu.txt"

def Traverse(dir):
    arr1 = []
    first_namelist = []
    other_namelist = []

    file1 = open(filepath1, "r+")
    file2 = open(filepath2, "r+")
    for line in file1.readlines():
        name = line.split("/")[-1].replace("\n", "")
        if name:
            arr1.append(name)
    for dirpath, dirnamelist, filenamelist, in os.walk(dir):
        for filename in filenamelist:
            if os.path.splitext(filename)[1] == ".py":
                if filename in arr1:
                    other_namelist.append(dirpath + "/" + filename)
                    continue
                arr1.append(filename)
                first_namelist.append(dirpath + "/" + filename)

    first_namelist = set([line + '\n' for line in first_namelist])
    other_namelist = set([line + '\n' for line in other_namelist])
    file1.writelines(first_namelist)
    file2.writelines(other_namelist)

    file1.close()
    file2.close()


if __name__ == '__main__':
    Traverse("/home/fandong/test")