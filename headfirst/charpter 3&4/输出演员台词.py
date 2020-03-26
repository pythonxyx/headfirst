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
        print(man)
        print(other)
except IOError:
    print("The file is missing!")