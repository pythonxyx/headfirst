from find_it import find_closest
from tm2secs2tm import time2secs,secs2time,format_time

def find_neaerest_time(look_for,taget_data):
    what = time2secs(look_for)
    where = [time2secs(t) for t in taget_data]
    res = find_closest(what,where)
    return (secs2time(res))

row_date = {}
with open('PaceData.csv') as paces:
    column_heading = paces.readline().strip().split(',')
    column_heading.pop(0)

    for each_line in paces:
        row = each_line.strip().split(',')
        row_label = row.pop(0)
        inner_dict = {}
        for i in range(len(column_heading)):
            inner_dict[format_time(row[i])] = column_heading[i]
        row_date[row_label] = inner_dict

distance_run = input('Enter the distance attempted: ')
recorded_time = input('Enter the recorded time: ')
predicted_distance = input('Enter the distance you want a prediction for: ')

closest_time = find_neaerest_time(format_time(recorded_time),row_date[distance_run])
closest_column_heading = row_date[distance_run][closest_time]

prediction = [k for k in row_date[predicted_distance].keys()
                   if row_date[predicted_distance][k] == closest_column_heading]
print('The predicited time running ' + predicted_distance + ' is ' + prediction[0] + '.')

# print(row_date['20k'])

# print(len(column_heading))

# num_cols = len(column_heading)
# print(num_cols,end=' -> ')
# print(column_heading)

# num_2mi = len(row_date['2mi'])
# print(num_2mi, end=' -> ')
# print(row_date['2mi'])

# num_Marathon = len(row_date['Marathon'])
# print(num_Marathon,end=' -> ')
# print(row_date['Marathon'])
#
# print(row_date)
