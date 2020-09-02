
import serial

class Pyrometer():

	def __init__(self, comPort = 'COM3'):
		"""initial parameters """
		self.comPort = comPort
		self.baudrate = 9600
		self.timeout = 0.1
		self.parity = 'E'
		self.bytesize = 7


		self.connect = None #initial state of this variable

	def connection (self):
		self.connect = serial.Serial(
		self.comPort,  
		baudrate = self.baudrate,
		timeout = self.timeout,
		parity = self.parity,
		bytesize = self.bytesize		
		)

	def check_port(self):
		""" check port. Return Boolean"""
		return(self.connect.is_open)

	def disconnect(self):
		if self.connect != None:
			self.connect.close()
			self.connect == None

		return('pyrometer is disconected')

	def model(self):
		"""if connect is open return model of pyrometer
		else return message """
		if self.connect != None:
			commandMD = b'#10MD<CR>\r'
			write = self.connect.write(commandMD) 
			readData = self.connect.readline()
			return (readData.decode('utf-8')[6:])
		return('pyrometer is disconected')

	def serial_number(self):
		""" return str"""
		if self.connect != None:
			commandSN = b'#10SN<CR>\r'
			write = self.connect.write(commandSN) 
			readData = self.connect.readline()
		return (readData.decode('utf-8')[6:])

	def temperature_only(self):
		if self.connect != None:
			commandTO = b'#10TO<CR>\r'
			write = self.connect.write(commandTO) 
			readData = self.connect.readline()
			return (readData.decode('utf-8')[5:])
		return('pyrometer is disconected')

	def emmisivity(self):
		if self.connect != None:
			commandTO = b'#10EM<CR>\r'
			write = self.connect.write(commandTO) 
			readData = self.connect.readline()
			return (readData.decode('utf-8')[5:])
		return('pyrometer is disconected')



if __name__ == "__main__":

	modline = Pyrometer()
	temperature = modline.tempernature_only()
	print(temperature)
	modline.connection()
	print('Pyrometer is connect = ',modline.check_port())
	temperature = modline.temperature_only()
	emmisivity = modline.emmisivity()
	print('emmisivity is 0.',emmisivity)

	print(temperature)
	modline.disconnect()
	print('Pyrometer is connect = ',modline.check_port())