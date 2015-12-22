from __future__ import absolute_import, print_function, unicode_literals

import json
import re

from streamparse.bolt import Bolt

class Rt(Bolt):
	
	def process(self, tup):
        
		value = tup.value[0]
		user = value.user



	        try:

	        	#Do not change below!
			self.log(user)
		    	self.emit([tup])
		except:
			pass
