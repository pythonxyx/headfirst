# 用来读取文件的函数
def get_coach_data(filename):
    try:
        with open(filename) as file:
            data = file.readline()
            return data.strip().split(',')
    except IOError as err:
        print("文件打开错误:" + str(err))
        return None

# 用来规范时间数据的函数
def sanitize(time_string):
    if '-' in time_string:
        spliter = '-'
    elif ':' in time_string:
        spliter = ':'
    else:
        return time_string
    (min,secs) = time_string.split(spliter)
    return (min + '.' +secs)

# 在适用sanitize函数时，要注意函数返回的值，用[]来对函数反馈的值形成一个列表
# james = get_coach_data('james2.txt')
# (james_name,james_bob) = james.pop(0),james.pop(0)
# james_quick = sorted(set([sanitize(each_time) for each_time in james]))
# print(james_name+ ' 跑得最快的前三个时间是：' +str(james_quick[0:3]))

# 引入字典后修改上述代码的情况
james = get_coach_data('james2.txt')
james_data = {}
james_data['Name'] = james.pop(0)
james_data['Bob'] = james.pop(0)
james_data['Time'] = james
print(james_data['Name']+' 跑得最快的前三个时间是：'+str(sorted(set([sanitize(each_time) for each_time in james_data['Time']]))[0:3]))


