#!/usr/bin/env python
# Filename: objvar.py

class Person:
	'''Represents a person.'''
	population=0

	def __init__(self,name):
		'''Initializes the person's data.'''
		self.name=name
		print '(Initializing %s)' %self.name

		#When this person is created, he/she adds to the population
		self.population+=1
	
	def __del__(self):
		'''I am dying.'''
		print '%s says bye.' %self.name

		self.population-=1

		if self.population==0:
			print 'I am the last one.'
		else:
		 	print 'There are still %d people left.' %self.population
	
	def sayHi(self):
		'''Greeting by the person. 

		Really, that's all it does.'''
		print 'Hi, my name is %s.' %self.name
	
	def howMany(self):
		'''Prints the current population.'''
		if self.population==1:
			print 'I am the only person here.'
		else:
			print 'We have %d p ersons here.' %self.population

bitcpf=Person('bitcpf')
bitcpf.sayHi()
bitcpf.howMany()

kalam=Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

bitcpf.sayHi()
bitcpf.howMany()
		
