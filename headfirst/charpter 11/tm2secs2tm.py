
import time

def format_time(time_string):
    tlen = len(time_string)
    if tlen < 3:
        original_format = '%S'       
    elif tlen < 6:
        original_format = '%M:%S'
    else:
        original_format = '%H:%M:%S'
    time_string = time.strftime('%H:%M:%S', time.strptime(time_string, original_format))
    return(time_string)

#time2secs函数将要找到的时间转化为秒数。
def time2secs(time_string):
    time_string = format_time(time_string)
    (hours, mins, secs) = time_string.split(':')
    seconds = int(secs) + (int(mins)*60) + (int(hours)*60*60)
    return(seconds)

#将秒数转化为小时—分钟—秒钟的时间格式
def secs2time(seconds):
    return(time.strftime('%H:%M:%S', time.gmtime(seconds)))

#测试format_time()函数
# print(format_time('3'))

#测试sec2time()函数
# print(secs2time(10000))