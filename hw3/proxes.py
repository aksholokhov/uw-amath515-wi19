# this file contains collections of proxes we learned in the class
import numpy as np
from scipy.optimize import bisect

# =============================================================================
# TODO Complete the following prox for simplex
# =============================================================================

# Prox of capped simplex
# -----------------------------------------------------------------------------
def prox_csimplex(z, k):
	"""
	Prox of capped simplex
		argmin_x 1/2||x - z||^2 s.t. x in k-capped-simplex.

	input
	-----
	z : arraylike
		reference point
	k : int
		positive number between 0 and z.size, denote simplex cap

	output
	------
	x : arraylike
		projection of z onto the k-capped simplex
	"""
	# safe guard for k
	assert 0<=k<=z.size, 'k: k must be between 0 and dimension of the input.'

	def f(l):
		ans = 0
		n = len(z)
		for zi in z:
			if zi < l:
				ans += 1/2*zi**2 - l*k/n
			elif zi > 1 + l:
				ans += 1/2*(1-zi)**2 + l*(1-k/n)
			else:
				ans += 1/2*l**2 + l*(zi - l - k/n)
		return ans

	def df(l):
		ans = 0
		n = len(z)
		for zi in z:
			if zi < l:
				ans += -k/n
			elif zi > 1 + l:
				ans += 1 - k/n
			else:
				ans += -l + zi - k/n
		return ans

	l0, r = bisect(df, -100500, + 100500, full_output=True)
	if not r.converged:
		print("does not converge")
	return (z-l0).clip(0, 1)

	# TODO do the computation here
	# Hint: 1. construct the scalar dual object and use `bisect` to solve it.
	#		2. obtain primal variable from optimal dual solution and return it.
	#

