movies = ['The Holy Grail',1975,"Terry Jones & Terry Gilliam",91,
              ["Graham Chapman",["Michael Palin","John Cleese",
                    "Terry Gilliam","Eric Idle","Terry Jones"]]]
# print(movies)

''' 下面的程序代码只能解决2层的列表，对于更多的，需要重复写for循环，很累的……'''
# for each_item in movies:
#     if isinstance(each_item,list):
#         for new_item in each_item:
#             print(new_item)
#     else:
#         print(each_item)

'''所以定义一个函数来解决这个问题,注意其中如果the_list是一个列表，则重复调用该函数，
这种方式也称为函数的递归'''

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)

print_lol(movies)



