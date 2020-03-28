'''
用类来处理教练的数据，
'''


class Athlete:
    def __init__(self,a_name,a_dob=None,a_time=[]):
        self.name = a_name
        self.dob = a_dob
        self.time = a_time

    def top3(self):
        return (sorted(
            set([sanitize(each_time)
                for each_time in self.time]))[0:3])

    def add_time(self,time_value):
        self.time.append(time_value)

    def add_times(self,time_list):
        self.time.extend(time_list)




def get_coach_data(filename):
    try:
        with open(filename) as file:
            data = file.readline()
            temp1 = data.strip().split(',')
            return(Athlete(temp1.pop(0),temp1.pop(0),temp1))
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
    (mins,secs) = time_string.split(spliter)
    return (mins + '.' +secs)

james = get_coach_data('james2.txt')

print(james.name + ' 跑得最快的三次成绩是：' + str(james.top3()))

vera = Athlete('vera vi')
vera.add_time('1.31')
print(vera.top3())
vera.add_times(['2.22','1-21','2:22'])
print(vera.top3())


