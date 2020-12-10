"""
收集目录下所有文件名
寻找最大数字比如567,那就表示最大有几位，那么3就会要改成003
主要目标是修改多层目录下所有的文件名为可重新排序的文档
"""
import glob
import os
import re
import sys


#使用os.walk遍历子目录及文件，找到某目录下文件名最大的数字
#根据该数字的位数确定是否要加零，加几个零
#重命名该文件
def read_and_replace(root_dir):
    for (dirname,dirshere,fileshere) in os.walk(root_dir):
        digit_list=[]
        for file_name in fileshere:
            number=re.search(r'\d+',file_name).group()
            digit_list.append(int(number))
        digit_list.sort()
        str_digit=str(digit_list[-1])
        str_len=len(str_digit)
        
        for file_name in fileshere:
            number=re.search(r'\d+',file_name).group()
            new_number=number.zfill(str_len)
            new_file_name=file_name.replace(number,new_number,1)
            path=os.path.join(dirname,file_name)
            new_path=os.path.join(dirname,new_file_name)
            os.rename(path,new_path)

if __name__=='__main__':
    if not sys.argv[1]:
        print("No specific directory")
        
    else:
        root_dir=sys.argv[1]

        if os.path.isdir(root_dir):
            read_and_replace(root_dir)
