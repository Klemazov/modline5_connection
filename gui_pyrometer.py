from tkinter import *
from tests import *
#from pyrometer_operating import *
#from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
#from matplotlib.backend_bases import key_press_handler
#from matplotlib.figure import Figure
#import numpy as np
#import time 

pyrometer = Pyrometer()

#Функции для работы с ГУИ 
def click_to_connect():
	global pyrometer
	try:
		pyrometer.connection()
		connectionLabel['text'] = 'pyrometer is connected'
	except Exception:
		connectionLabel['text'] = 'device is  disconnected'

	
def click_to_disconnect():
	global pyrometer
	pyrometer.disconnect()
	connectionLabel['text'] = 'pyrometer is  disconnected'
def click_to_get_temperature():
	global pyrometer
	if pyrometer is not  None:
		temperature = pyrometer.temperature_only()
		connectionLabel['text'] = temperature
	else:
		connectionLabel['text'] = 'pyrometer is  disconnected'

def write_to_file():
	global pyrometer
	if pyrometer != None:
		with open('pyr.txt', 'w', encoding = 'utf-8') as file:
			for i in range(100):
				file.write(str(i)+','+pyrometer.temperature_only())


root = Tk()



root.wm_title('Pyrometer ')



connectionButton = Button(command = click_to_connect, text = 'click to open serial port')
disconnectionButton = Button(command = click_to_disconnect, text = 'click to close serial port')
temperatureButton = Button(command = click_to_get_temperature, text = 'click to get temperature')
connectionLabel = Label(text = 'click to connect pyrometer', width = 25)
writeButton = Button(command = write_to_file, text = 'write temperature')
# plotButton = Button(command = plot, text = 'plot temperature')
# #make a grid 
connectionLabel.grid(row = 0, column = 2)
connectionButton.grid(row = 0, column = 1)
disconnectionButton.grid(row = 1, column = 1)
temperatureButton.grid(row = 2, column = 1)
writeButton.grid(row = 2, column = 2)




# plotButton.grid(row = 2, column = 3)

# button.pack()
# # writeToFileButton.grid(row = 0, column = 3)

root.mainloop()



