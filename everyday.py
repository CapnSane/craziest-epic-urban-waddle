import schedule
import time
import datetime
  
t_seconds = 10
sch_time = "15:59"

def dateNow():
    current_time = datetime.datetime.now()
    return str(current_time)

def job(t):
    print("I'm working...", t)
    return

schedule.every().day.at(f"{sch_time}").do(job,f'It is {sch_time}')

while True:
    schedule.run_pending()
    time.sleep(t_seconds) # wait t_seconds