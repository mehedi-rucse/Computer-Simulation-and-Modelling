import numpy as np
import matplotlib.pyplot as plt

VF = 20
T = 0
xf = 0
yf = 0

bPlaneX = []
bPlaneY = []
fPlaneX = []
fPlaneY = []
fPlaneY.append(yf)
fPlaneX.append(xf)

for line in open("Bomber_Path.txt"):
    t, x, y = line.strip().split(",")
    t = int(t)
    x = int(x)
    y = int(y)
    T = max(T, t)
    bPlaneX.append(x)
    bPlaneY.append(y)

print(fPlaneX, fPlaneY)

for t in range(0, T):
    if (t > 11):
        print("Bomber has escaped")
        break

    xb = bPlaneX[t]
    yb = bPlaneY[t]
    print("H", xb, yb)

    dist = np.sqrt(pow((xb-xf), 2) + pow((yb-yf), 2))
    print("Distance {}".format(dist))

    if (dist <= 10):
        print("Caught")
        break
    elif(dist > 700):
        print("Escaped!")
        break
    else:
        sin = (xb - xf)/dist
        cos = (yb - yf)/dist
        xf = xf + VF * sin
        yf = yf + VF * cos
        t = t + 1
    fPlaneY.append(yf)
    fPlaneX.append(xf)

plt.plot(fPlaneX, fPlaneY, "r*")
plt.plot(bPlaneX, bPlaneY, "b*")
plt.show
