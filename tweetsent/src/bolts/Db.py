from __future__ import absolute_import, print_function, unicode_literals

import json
import re

from streamparse.bolt import Bolt

class Db(Bolt):

    def process(self, tup):
    		


        	try:

        		#Don't change below!
	        	self.log(tup)
	        	self.emit([tup])
	    	except:
	    		pass
