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

sarah = get_coach_data('sarah.txt')
mike = get_coach_data('mike.txt')

print(set(sarah))
print(sorted(set(sarah)))

# print(sorted(set([sanitize(each_t) for each_t in get_coach_data('sarah.txt')]))[0:3])