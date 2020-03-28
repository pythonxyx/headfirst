"""
用来读取文件的函数,做了如下修改：
1.直接通过函数反馈了一个字典，在调用函数时，将产生一个字典；
2.把字典中的时间直接调用sanitize函数来截取了最快的前三项。
"""


def get_coach_data(filename):
    try:
        with open(filename) as file:
            data = file.readline()
            temp1 = data.strip().split(',')
            return({
                'name': temp1.pop(0),
                'Bod': temp1.pop(0),
                'time': str(sorted(set([sanitize(each_time) for each_time in temp1]))[0:3])
            })
    except IOError as err:
        print("文件打开错误:" + str(err))
        return None

# 用来规范时间数据格式的函数


def sanitize(time_string):
    if '-' in time_string:
        spliter = '-'
    elif ':' in time_string:
        spliter = ':'
    else:
        return time_string
    (mins,secs) = time_string.split(spliter)
    return (mins + '.' +secs)


james = get_coach_data('james2.txt')
print(james)
print(james['name'] + ' 跑得最快的前三次时间是： '+james['time'])
