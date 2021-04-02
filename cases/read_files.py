
def read_file1():

    fp = open('b.txt','r')
    print(fp.read())
    fp.close()

# read_file1()

def read_file2():

    fp = open('b.txt','r')
    fp.write('cc')   #   出现报错信息
    print(fp.read())
    fp.close()

# read_file2()

def read_file3():

    fp = open('b.txt','w+')
    fp.write('cc')   #   出现报错信息
    fp.seek(0)
    print(fp.read())
    fp.close()

# read_file3()


def read_file4():
    fp = open('b.txt','r+')
    fp.write('a')   #
    fp.seek(0)
    print(fp.read())
    fp.close()

# read_file4()

def read_file5():
    fp = open('b.txt','a+')
    fp.write('python')   #
    fp.seek(0)
    print(fp.read())
    fp.close()

# read_file5()

def read_file6():
    fp = open('c.txt','r+')
    fp.write('python')   #   出现报错信息
    fp.seek(0)
    print(fp.read())
    fp.close()

# read_file6()

def read_file7():
    fp = open('d.txt','a')   #   当文件不存在的时候，会自主新建文件；当文件存在的时候，会自动将内容追加到源文件中，不会实现内容的覆盖
    fp.write('python')   #   出现报错信息
    fp.seek(0)
    print(fp.read())
    fp.close()

read_file7()