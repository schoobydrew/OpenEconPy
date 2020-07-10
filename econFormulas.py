# Engineering economics formulas by Andrew Schoonmaker
# import statements
from decimal import Decimal as D
class SinglePayment:
    def FP(P=1, i=1, n=1):
        return D(str(P))*(1+D(str(i)))**D(str(n))
    def PF(F=1, i=1, n=1):
        return D(str(F))/(1+D(str(i)))**D(str(n))
