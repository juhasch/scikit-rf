import socket
from time import sleep 
class generalSocketReader:
	'''
	A general class which wraps a socket and has a simple data query
	function, implemented by the property data_point.

	this was made as a way to interface a piece of hardware which did
	not support	gpib.  is useful for general interfacing  of 
	non-standard hardware or software.

	example usage:
		gsr = generalSocketRead()
		gsr.connect('127.0.0.1',1111)
		gsr.data_point	# implicityly calls send() then receive()
	'''
	def __init__(self, sock=None, query_string = '1', msg_len =1e3):
		'''
		takes:
			sock: socket type (defaults to None and generates a new socket)
			query_string: string sent during send() command
			msg_len: length of recv buffer used in receive() command
			
		'''
		if sock is None:
			self.sock = socket.socket(
				socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.sock = sock
		self._query_string = query_string
		self._msg_len = int(msg_len)
		

	def connect(self, host, port):
		self.sock.connect((host, port))

	def close(self):
		self.sock.close()
	
	def send(self, data):
		self.sock.send(data)
			
	def receive(self):
		data = self.sock.recv(self._msg_len)
		return data
	
	@property
	def data_point(self):
		self.send(self._query_string)
		return self.receive()
