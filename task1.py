import datetime
from time import sleep
import random


# Task 1

# class Clock:    
    
#     def time(self):
#         now =datetime.datetime.now()
#         print(now)


# class Alarm:
#     alarm = None

#     def turn_on(self):
#         Alarm.alarm = True

    
#     def turn_off(self):
#         Alarm.alarm = False


# class AlarmClock(Alarm, Clock):
    
       
#     def set_alarm(self,hour=0,minutes=0):
#         while AlarmClock.alarm:
#             time = datetime.datetime.now()
#             print
#             if str(time.hour) == hour and str(time.minute) == minutes:
#                 print('ALARM')
#                 break
#             sleep(1)



# alarm = AlarmClock()
# alarm.time()
# alarm.turn_on()
# alarm.set_alarm(hour="16",minutes="47")



# Task 2
# class Coder:
    
#     experience = ''
#     count_code_time = 0

#     def get_info(self):
#         pass

#     def coding(self):
#         pass


# class Backend(Coder):


#     def __init__(self, languages_backend):
#         self.experience = languages_backend

#     def get_info(self):
#         print(f' Your programmong language is {self.experience}. Your code time is {self.count_code_time}')

#     def coding(self, time):
#         self.count_code_time += time



# class Frontend(Coder):

#     def __init__(self, languages_frontend):
#         self.experience = languages_frontend

#     def get_info(self):
#         print(f' Your programmong language is {self.experience}. Your code time is {self.count_code_time}')

#     def coding(self, time):
#         self.count_code_time += time


# class FullStack(Frontend, Backend, Coder):

#     def __init__(self, languages_frontend):
#         self.experience = languages_frontend


# be1 = Backend('Python')
# be1.coding(20)
# be1.get_info()

# fe1 = Frontend('JavaScript')
# fe1.coding(50)
# fe1.get_info()

# fs1 = FullStack('Python, JavaScript')
# fs1.coding(200)
# fs1.get_info()





# Task 4

# def hackerrankInString(s):
#     target = 'hackerrank'
#     n = len(target)
    
#     i = 0
    
#     for char in s:
#         if char == target[i]:
#             i += 1
#             if i == n:
#                 return "YES"
#     return "NO"

