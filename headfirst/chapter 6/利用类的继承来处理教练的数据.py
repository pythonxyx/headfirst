'''
利用类的继承来处理教练带来的数据，将Athlete类继承至List类
1.类实例对象本身就是一个列表
2.类实际对象可以获得list的一些方法，比如extend、append之类的
'''


class Athletelist(list):
    def __init__(self,a_name,a_dob=None,a_time=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_time)

    def top3(self):
        return (sorted(
            set([sanitize(each_time)
                for each_time in self]))[0:3])


def get_coach_data(filename):
    try:
        with open(filename) as file:
            data = file.readline()
            temp1 = data.strip().split(',')
            return(Athletelist(temp1.pop(0),temp1.pop(0),temp1))
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

vera = Athletelist('Vera Vi')
vera.append('1.51')
print(vera.top3())
vera.extend(['1.21','2.50','1.19','2.49'])
print(vera.top3())