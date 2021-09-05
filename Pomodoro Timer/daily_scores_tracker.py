import csv
from datetime import datetime
import time


day_record = datetime.now()

#If the program run in the same day
#Update the value count_pomodoro25_day and count_pomodoro50_day to daily_scores_tracker.txt
if day_record.day == datetime.now().day:
    outputFileWrite = open('daily_scores_tracker.txt', 'wt')
    outputFileWrite.write(str(day_record.second)+'-'+ str(day_record.month) + '-' + str(day_record.year) + 'str(count_pomodoro25_day)' + 'str(count_pomodoro50_day)')
    

else:
    with open('monthly_scores_tracker.txt', 'a+') as monthlyFile:
        with open ('daily_scores_tracker.txt', 'r') as dailyFile:
            for line in dailyFile:
                monthlyFile.write('\n')
                monthlyFile.write(line)

print(datetime.now())


    
    