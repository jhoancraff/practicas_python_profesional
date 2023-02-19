from datetime import datetime

my_time = datetime.now()
print(my_time)

my_str = my_time.astimezone()
print('Fecha LATAM: ', my_str)
