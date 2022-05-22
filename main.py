from decimal import Decimal
import conststr

def pi(n):
	# only supports 15 decimals
	pi = float(conststr.pi[:(n+2)])
	return pi
def pi_dec(n):
	# suports all 1000 didgets
	pi = Decimal(conststr.pi[:(n+2)])
	return pi
def phi(n):
	phi = float(conststr.phi[:(n+2)])
	return phi
def phi_dec(n):
	phi = Decimal(conststr.phi[:(n+2)])
	return phi

def e_(n):
	return  float(conststr.e[:(n+2)])
def e_dec(n):
	return Decimal(conststr.e[:(n+2)])


def sqrt2(n):
	return  float(conststr.sqrt[:(n+2)])
def sqrt2_dec(n):
	return Decimal(conststr.sqrt[:(n+2)])


