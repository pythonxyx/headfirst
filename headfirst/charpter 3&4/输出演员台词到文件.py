man = []
other = []

try:
    with open('sketch.txt') as data:
        for each_line in data:
            try:
                (role,line_spoken) = each_line.split(":",1)
                line_spoken = line_spoken.strip()
                if role == 'Man':
                    man.append(line_spoken)
                elif role == 'Other Man':
                    other.append(line_spoken)
            except ValueError:
                pass
except IOError:
    print("The file is missing!")

# 将man和othe 的台词输出到txt文件。利用try来保护程序的正常运行

try:
    with open('man_data.txt',"w") as man_file:
        print(man,file=man_file)

    with open('other_data.txt',"w") as other_file:
        print(other,file=other_file)
except IOError:
    print('file error!')


