# Skrått kast uten luftmotstand med starthøyde

from pylab import *

# Konstanter
m = 0.145
g = 9.81
v0 = 5.3
y0 = 1.035
theta = radians(38) # Gjør om fra grader til radianer

# Dekomponere fart i x og y-retning
v0_x = v0 * cos(theta)
v0_y = v0 * sin(theta)
t = 0

# Posisjonsformler
def sx(t):
    return v0_x * t

def sy(t):
    return y0 + v0_y * t - g/2 * t**2 

# Liste som holder x- og y-koordinater
x_verdier = []
y_verdier = []

# Simulering av bevegelsen
dt = 0.001                 # tidssteg i simulering, s

while sy(t) >= 0:    # stopper når y = 0
    x_verdier.append( sx(t) )
    y_verdier.append( sy(t) )
    t = t+ dt

# Tegning av graf
plot(x_verdier, y_verdier)  # Lager grafen
title("Skrått kast uten luftmostand")
xlabel("$x$ (m)")
ylabel("$y$ (m)")
grid()
show()
