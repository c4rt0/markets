from datetime import datetime, date, time

dt = datetime(2021,10,14,15,56,31)

print(dt.day)

soTime = dt.strftime('%m/%d/%y %H:%M:%S')

print(soTime)

# Time difference between

dt2 = datetime(2021,11,15,22,30)

delta = dt2 - dt

# if delta <= 30:
#     try:
#         print('Wow, that\'s some number')
#     except Exception as e:
#         print(e)

print('1:', dt2, ' 2: ', dt, ". Time difference = ", delta)

print (type(delta))