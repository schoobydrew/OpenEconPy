# Engineering economics formulas by Andrew Schoonmaker
# import statements
#ii like git
from decimal import Decimal as D
# single payment series
class SinglePayment:
    # F/P is given by the following formula
    # P*(1+i)^n
    def FP(P=1, i=1, n=1):
        P = D(str(P))
        i = D(str(i))
        n = D(str(n))
        return P*(1+i)**n
    # P/F is given by the following formula
    # F*(1+i)^(-n)
    def PF(F=1, i=1, n=1):
        F = D(str(F))
        i = D(str(i))
        n = D(str(n))
        return F/(1+i)**n
# uniform payment series
class UniformSeries:
    # F/A is given by the following formula
    # A*[(1+i)^n - 1 ] / i
    def FA(A=1, i=1, n=1):
        A = D(str(A))
        i = D(str(i))
        n = D(str(n))
        return A*((1+i)**n - 1)/(i)
    # A/F is given by the following formula
    # F*i / [(1+i)^n - 1 ]
    def AF(F=1, i=1, n=1):
        F = D(str(F))
        i = D(str(i))
        n = D(str(n))
        return F*(i)/((1+i)**n - 1)
    # P/A is given by the following formula
    # A*[(1+i)^n-1]/[i*(1+i)^n]
    def PA(A=1, i=1, n=1):
        A = D(str(A))
        i = D(str(i))
        n = D(str(n))
        return A*((1+i)**n-1)/(i*(1+i)**n)
    # A/P is given by the following formula
    # P*[i*(1+i)^n]/[(1+i)^n-1]
    def AP(P=1, i=1, n=1):
        P = D(str(P))
        i = D(str(i))
        n = D(str(n))
        return P*(i*(1+i)**n)/((1+i)**n-1)
