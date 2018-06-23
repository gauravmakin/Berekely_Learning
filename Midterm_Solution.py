import 
a = plb.arange(5,28,2)

def sma(B, x=2):
    D =plb.zeros(len(B) - x=(x-1))
    E = plb.zeros(len(B) - (x))
    for index, i in enumerate(plb.arange(len(B))):
        