from burp import IBurpExtender
from burp import IIntruderPayloadGenerator
from burp import IIntruderPayloadGeneratorFactory
from burp import IIntruderPayloadProcessor

import random

class BurpExtender(IBurpExtender, IIntruderPayloadProcessor):
	# IBurpExtender
	def registerExtenderCallbacks(self, callbacks):
		callbacks.setExtensionName("CCGen")
		helpers = callbacks.getHelpers();
		callbacks.registerIntruderPayloadProcessor(self)
		return

	# IIntruderPayloadProcessor
	def getProcessorName(self):
		return "Add Luhn Check Digit"

	def processPayload(self, current, original, base):
		data = current.tostring()
		return bytearray(data + CalculateLuhn(data), 'ascii')

def CalculateLuhn(data):
	# Calculate sum
	total = 0
	pos = 0
	length = len(data) + 1

	reversedCCnumber = []
	reversedCCnumber.extend(list(data))
	reversedCCnumber.reverse()

	while pos < length - 1:
		odd = int(reversedCCnumber[pos]) * 2
		if odd > 9:
			odd -= 9
		total += odd
		if pos != (length - 2):
			total += int(reversedCCnumber[pos + 1])
		pos += 2

	# Get check digit
	return '0987654321'[total % 10]