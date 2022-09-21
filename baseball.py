"""
This code is from textbook in physics:
Ergo 2 by Aschehoug (2022): https://aschehoug.no/undervisning/fysikk

Slightly modified by
Henrik Mauroy
henrik@mauroy.no
2022
"""

from pylab import *

# Konstanter
m = 0.145
k = 1.31e-3 # 1/2 * rho * C * A
g = 100*9.81
v0 = 40
y0 = 1.035
theta = radians(38) # Gjør om fra grader til radianer

# Konstante krefter i x og y-retning. G er en vektor
G = array([0, -m*g])

# Variable krefter, utregning av kaftsum og akselerasjon
def a(v):
    e_v = v/norm(v)         # Enhetsvektor for farten
    L = -k*norm(v)**2 * e_v # Luftmotstandsvektor, avhengig av farten
    sum_F = G + L           # Vektorsum av krefter
    aks = sum_F / m         # Akselerasjonsvektor
    return aks

# Startverdier for bevegelsen
r = array([0, y0])                          # startpos, m
v = array([v0*cos(theta), v0*sin(theta)])   # startfart, m/s
t = 0                                       # starttid, s

# Lister for lagring av verdier.
# setter inn første posisjonsvektor og fartsvektor
r_liste = [r]
v_liste= [v]
tid = []

# Simulering av bevegelsen
dt = 0.0001                  # tidssteg i simulering, ms

while v[1] >= 3:    # stopper når y = 0 (r[1] gir y-verdi). Verdien på plass 1. r[x,y]
    v = v + a(v)*dt # beregner ny fart
    r = r + v*dt    # beregner ny posisjon
    tid.append([t,t])
    t = t+ dt
    # Lagrer 2D-verdier i lister
    r_liste = concatenate([r_liste, [r]])

# Tegning av graf
plot(r_liste[:,0], r_liste[:,1])    # Lager grafen
title("Skrått kast med luftmostand")
xlabel("$x$ (m)")
ylabel("$y$ (m)")
grid()
show()

print(a(v))
