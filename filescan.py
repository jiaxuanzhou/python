# coding= utf8
import sys, os, string
reload(sys)
sys.setdefaultencoding('utf8')
dirpath1 = raw_input("please input the dir path1:") 
dirpath2 = raw_input("please input the dir path2:") 
def getfilelist(self):
    files_indir = []
    file_list = []
    for root, dirs, files in os.walk(self):
        for dir in dirs:
            #print os.path.join(root, dir)
            os.path.join(root, dir)
        for file in files:
            file_list.append(file + '\n')
            #print os.path.join(root, file)
            os.path.join(root, file)
            files_indir.append(os.path.join(root,file) + '\n')
    
    fo = open(self + "_files","w+")
    fo.writelines(file_list)
    fo.close()
    
    o = open(self + "_details", "w+")
    o.writelines(files_indir)
    o.close()
    return file_list
def path_cmp(path1,path2):
    result = []
    path1_list = getfilelist(path1)
    path2_list = getfilelist(path2)
    for item in path1_list:
        if item in path2_list:
            result.append(item + '\n')
    o=open("path_cmp", "w+")
    o.writelines(result)
    o.close()
path_cmp(dirpath1,dirpath2)
