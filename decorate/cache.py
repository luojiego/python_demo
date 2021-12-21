from functools import wraps
def memoization(fn):
	cache = {}
	miss = object()

	@wraps(fn)
	def wrapper(*args):
		result = cache.get(args, miss)
		if result is miss:
			result = fn(*args)
			cache[args] = result
		return result
	return wrapper

@memoization
def fib(n):
	if n < 2:
		return n
	return fib(n-1) + fib(n-2)

print fib(100)
