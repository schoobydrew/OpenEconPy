# Engineering economics formulas by Andrew Schoonmaker
# import statements
from decimal import Decimal as D
# single payment series
class SinglePayment:
    # F/P is given by the following formula
    # P*(1+i)^n
    def FP(P=1, i=1, n=1):
        return D(str(P))*(1+D(str(i)))**D(str(n))
    # P/F is given by the following formula
    # F*(1+i)^(-n)
    def PF(F=1, i=1, n=1):
        return D(str(F))/(1+D(str(i)))**D(str(n))
