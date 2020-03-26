# 第一次代码，其中遇到一句话里面有两个冒号的时候，就出现了错误
# with open('sketch.txt') as data:
#     for each_line in data:
#         (role,line_spoken) = each_line.split(':')
#         print(role,end='')
#         print(' said: ',end='')
#         print(line_spoken,end='')

# 第二次代码，解决遇到一句话里面有两个冒号的问题，但是遇到一行没有任何冒号的时候出现错误。
# with open('sketch.txt') as data:
#     for each_line in data:
#         (role,line_spoken) = each_line.split(':',1)
#         print(role,end='')
#         print(' said: ',end='')
#         print(line_spoken,end='')

# 第三次代码，解决一句话里面没有任何冒号的问题，终于可以正常显示了
# with open('sketch.txt') as data:
#     for each_line in data:
#         if not each_line.find(':') == -1:
#             (role,line_spoken) = each_line.split(':',1)
#             print(role,end='')
#             print(' said: ',end='')
#             print(line_spoken,end='')

# 第四次代码，利用try…except，让错误不显示,但是错误以后的内容也不会显示。注意try需要保护的程序块！！
# with open('sketch.txt') as data:
#          for each_line in data:
#              try:
#                  (role,line_spoken) = each_line.split(':',1)
#                  print(role,end='')
#                  print(' said: ',end='')
#                  print(line_spoken,end='')
#              except:
#                  pass

# 第五次代码，利用逻辑判断来检查文件是否存在，增强程序运行的稳定性
# import os
# if os.path.exists('sketch.txt'):
#     with open('sketch.txt') as data:
#
#         for each_line in data:
#             if not each_line.find(':') == -1:
#                 (role, line_spoken) = each_line.split(':', 1)
#                 print(role, end='')
#                 print(' said: ', end='')
#                 print(line_spoken, end='')
# else:
#     print('The data file is missing!')

# 第五次代码的另一种形式，利用try来检查文件I/O错误。
# try:
#     with open('sketch.txt') as data:
#
#         for each_line in data:
#             if not each_line.find(':') == -1:
#                 (role, line_spoken) = each_line.split(':', 1)
#                 print(role, end='')
#                 print(' said: ', end='')
#                 print(line_spoken, end='')
# except:
#     print('The data file is missing!')

#第六次代码，更加稳定的程序运行，利用了两个try来保护程序的运行，第一个反馈文件是否存在，第二个遇到冒号不存问题时跳过！！
# 当然，except后面也可以处理具体的问题错误，比如ValueError，IOError
try:
    with open('sketch.txt') as data:

        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(':', 1)
                print(role, end='')
                print(' said: ', end='')
                print(line_spoken, end='')
            except:
                pass
except:
    print('The data file is missing!')





#     调整pycharm的错误混乱显示问题。
# with open('sketch.txt') as data:
#     data_list = [x for x in data]
# for each_line in data_list:
#     (role,line_spoken) = each_line.split(":",1)
#     print(role,end='')
#     print(' said: ',end='')
#     print(line_spoken,end='')

# 验证readlines() 反馈的结果，读取TXT文件中的每一行，然后生成一个列表
# with open('sketch.txt') as data:
#     m = data.readlines()
#     print(m)

