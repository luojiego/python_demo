def hello(fn):
	def wrapper():
		print "Hello, %s" % fn.__name__
		fn()
		print "goodbye, %s" % fn.__name__
	return wrapper

@hello
def Roger():
	print "I'm Roger"

Roger()
