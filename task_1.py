time_items = '1h 45m,360s,25m,30m 120s,2h 60s'

time_items = time_items.split(',')
times= []

for item in time_items:
    if ' ' in item:
        item = item.split()
        times += item
    else:
        times.append(item)

times_sum = 0

for time in times:
    if 'h' in time:
        time = time.replace('h', '')
        times_sum += int(time) * 60
    elif 's' in time:
        time = time.replace('s', '')
        times_sum += int(time) // 60
    else:
        time = time.replace('m', '')
        times_sum += int(time)

print(f'{times_sum} minutes total')





