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

clean_james = []

for each_time in james:
    clean_james.append(sanitize(each_time))

print(james)
print(clean_james)


# print(sorted(james))
# print(sorted(julie))
# print(sorted(mikey))
# print(sorted(sarah))

