# coding=utf-8

import sys

class MyClass(object):
	def __init__(self, name, identifier):
		self.name = name
		self.identifier = identifier

class MyClassSlot(object):
	__slot__ = ['name', 'identifier']
	def __init__(self, name, identifier):
		self.name = name
		self.identifier = identifier


