""" Variable delcaration"""
a=3
b=9.9
# sum
def sum(a,b):
    return a+b

#sub
def sub(a,b):
    return a-b

#mul
def mul(a,b):
    return a*b

#div
def div(a,b):
    return a/b

# String concatenation without f-strings
print(" A soma de "+str(a)+" + "+str(b)+" é "+ str(sum(a,b)) +".")
print(" A subtração de " +str(a)+" - "+str(b)+" é "+ str(sub(a,b)) +".")
print(" A multiplicação de "+str(a)+" * "+str(b)+" é %.3f" % mul(a,b) +".")
print(" A divisao de "+str(a)+" / "+str(b)+" é %.3f" % div(a,b) +".")