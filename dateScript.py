import os
import datetime

t = datetime.datetime.now().strftime("%m\/%d\/%Y")

os.system(f'echo -n {t} > ./my_date.txt')
