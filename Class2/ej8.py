from gpio import Gpio

gpio10 = Gpio(10)
print(gpio10.get_state())
gpio10.set_state(True)
print(gpio10.get_state())