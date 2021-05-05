import time

RED = '''
red
x
x
'''
YELLOW = '''
x
yellow
x'''
GREEN = '''
x
x
green'''




class TrafficLight:

    def running(self, ):
        while True:
            self.__color = RED
            print(10*'\n' + self.__color)
            time.sleep(7)

            self.__color = YELLOW
            print(10*'\n' + self.__color)
            time.sleep(2)

            self.__color = GREEN
            print(10*'\n' + self.__color)
            time.sleep(7)



        pass

tl01 = TrafficLight()
tl01.running()
print(tl01)
