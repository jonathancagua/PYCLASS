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
        if value == '1':
            return True
        return False

    def set_state(self,value):
        with open(self.path, 'w') as fd:
            if value:
                value_s = '1'
            else:
                value_s = '0'
            value 	= fd.write(value_s)
            return value
