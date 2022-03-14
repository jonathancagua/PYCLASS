from operator import truediv
GPIO_BASE_PATH 					= 'tmp'
GPIO_PATH 						= GPIO_BASE_PATH + '/gpio_%d.data'

class Gpio:
    def __init__(self,gpio):
        self.gpio 		= gpio
        self.path 		= GPIO_PATH%(self.gpio)

    def get_state(self):
        with open(self.path, 'r') as fd:
            value 	= fd.read()
            fd.close()
        if(value == '1'):
            return True
        return False

    def set_state(self,value):
        with open(self.path, 'w') as fd:
            value 	= fd.write(str(value))
            fd.close()
            return value
