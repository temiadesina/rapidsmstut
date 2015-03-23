from rapidsms.contrib.handlers import KeywordHandler, PatternHandler

help_text = {
	'aaa':'Help for aaa'
	'bbb':'Help for bbb'
	'ccc':'Help for ccc'
}

class HelpHandler(KeywordHandler):
	keyword = "help"
	
	def help(self):
		self.respond("Allowed commands are AAA, BBB, and CCC. Send "
			"HELP <command> for more help on a specific command.")
	
	def handle(self, text):
		"""Invoked if someone sends Help<command>"""
		text = text.strip().lower()
		if text == 'aaa':
			self.respond(help_text['aaa'])
		elif text == 'bbb':
			self.respond(help_text['bbb'])
		elif text == 'ccc':
			self.respond(help_text['ccc'])
		else:
			self.help()

class SumHandler(PatternHandler):
	pattern = r'^(\d+) plus (\d+)$'
	
	def handle(self, a, b):
		a, b= int(a), int(b)
		total= a+b
		
		self.respond("%d+%d = %d" % (a, b, total))
	
