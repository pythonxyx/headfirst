with open('james.txt') as jaf:
    data = jaf.readline()
    james = data.strip().split(',')

with open('julie.txt') as juf:
    data = juf.readline()
    julie = data.strip().split(',')

with open('mikey.txt') as mif:
    data = mif.readline()
    mikey = data.strip().split(',')

with open('sarah.txt') as saf:
    data = saf.readline()
    sarah = data.strip().split(',')

def sanitize(time_string):
    if '-' in time_string:
        spliter = '-'
    elif ':' in time_string:
        spliter = ':'
    else:
        return time_string
    (min,secs) = time_string.split(spliter)
    return (min + '.' +secs)

'''通过列表推导的方式，可以更简洁的写出代码'''
clean_james = [sanitize(each_t) for each_t in james]
clean_julie = [sanitize(each_t) for each_t in julie]
clean_mikey = [sanitize(each_t) for each_t in mikey]
clean_sarah = [sanitize(each_t) for each_t in sarah]

 '''未使用列表推导方式之前，需要将上面的clean系列的声明为空列表，然后用下列方法写代码'''
# for each_time in james:
#     clean_james.append(sanitize(each_time))
# for each_time in julie:
#     clean_julie.append(sanitize(each_time))
# for each_time in mikey:
#     clean_mikey.append(sanitize(each_time))
# for each_time in sarah:
#     clean_sarah.append(sanitize(each_time))

print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))


# print(sorted(james))
# print(sorted(julie))
# print(sorted(mikey))
# print(sorted(sarah))

