print("////CRECIMIENTO//CIUDADES///")

# input
a=3.5
b=5
n=1980
# processing
while b>a:
    a=(0.07+a)*a
    b=(0.05+b)*b
    n+=1
print("El año en que ocurrio esto fue: " ,n)