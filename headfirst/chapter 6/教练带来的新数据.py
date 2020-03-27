def get_coach_data(filename):
    try:
        with open(filename) as file:
            data = file.readline()
            return data.strip().split(',')
    except IOError as err:
        print("文件打开错误:" + str(err))
        return None

def sanitize(time_string):
    if '-' in time_string:
        spliter = '-'
    elif ':' in time_string:
        spliter = ':'
    else:
        return time_string
    (min,secs) = time_string.split(spliter)
    return (min + '.' +secs)