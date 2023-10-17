import math
meno = str(input("Ako sa volas? "))
vek = int(input("Kolko mas rokov? "))
print("Ty sa volas {0} a mas {1} rokov ".format(meno, vek))

# vypocet kvadratickej rovnice

a = 2
b = 6
c = -20
D = (b ** 2) - 4 * (a * c)

vysl1 = (-b + math.sqrt(D)) / (2 * a)
vysl2 = (-b - math.sqrt(D)) / (2 * a)

print("Vysledok kvadratickej rovnice v tvare {0}x2 + {1}x + {2} sa rovna x1 = {3} a x2 = {4}".format(a, b, c, vysl1, vysl2))
