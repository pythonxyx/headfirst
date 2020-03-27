# """这是“nester.py”模块，提供一个名为print_lol()的函数，这个函
# 数的作用是打印列表，其中有可能包含（也可能不包含）嵌套列表"""
#
# def print_lol(the_list):
#     '''这个函数去一个位置参数，名为the_list，这可以是任何Python
#     列表（也可以是包含嵌套列表的列表）。所指定的列表中的每个数据项会
#     （递归地）输出屏幕上，各数据各占一行。'''
#     for each_item in the_list:
#         if isinstance(each_item,list):
#             print_lol(each_item)
#         else:
#             print(each_item)

"""这是“nester.py”模块，提供一个名为print_lol()的函数，这个函
数的作用是打印列表，其中有可能包含（也可能不包含）嵌套列表"""

def print_lol(the_list,indent=False,level=0):
    '''这个函数去一个位置参数，名为the_list，这可以是任何Python
    列表（也可以是包含嵌套列表的列表）。所指定的列表中的每个数据项会
    （递归地）输出屏幕上，各数据各占一行。第二个参数（名为level）用来在遇到嵌套
    列表时插入制表符。'''
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1)
        else:
            if indent:
                print('\t' * level,end='')
            # for tab_stop in range(level):
            #     print('\t',end='')
            print(each_item)

'''下面是对模块文件的内部测试，外部导入时不显示'''
if __name__ == '__main__':
    movies = ['The Holy Grail', 1975, "Terry Jones & Terry Gilliam", 91,
              ["Graham Chapman", ["Michael Palin", "John Cleese",
                                  "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
    print_lol(movies,True)
