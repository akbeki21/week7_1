# Task 1

# class Car:

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = 0
#         self.fuel = 70



#     def drive(self, km):
#         if self.fuel * 10 >= km:
#             self.__add_distance(km)
#             self.__subtract_fuel(km // 10)
#             print('Let’s drive!')
#         else:
#             print('Need more fuel, please, fill more!')


#     def __subtract_fuel(self, fuel):
#         self.fuel -= fuel



#     def __add_distance(self, km):
#         self.odometer = km

    
# car = Car('Japan', 'Toyota', 2019)
# car.drive(800)
# print(car.odometer)
# print(car.fuel)



# Task 2

# class MobilePhone:

#     __battery = 100


#     def listen_music(self):
#         self.__battery -= 5
#         print("You can listen to music")


#     def watch_video(self):
        
#         if MobilePhone.__battery <= 10:
#             print("The battery is too low")
#         else:
#             self.__battery -= 7
#             print("You can watch the video")

    
#     def charger(self):
#         if MobilePhone.__battery == 0:
#             raise Exception ("ZeroBattery! Charge your phone!")

#     def battery_charging(self):
#         self.__battery = 100


# iPhone = MobilePhone()
# iPhone.listen_music()
# iPhone.watch_video()
# iPhone.battery_charging()


# Task 3
class Pyramid:

    __length = 0
    __
