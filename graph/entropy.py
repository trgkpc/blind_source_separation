import matplotlib.pyplot as plt
import math
import japanize_matplotlib
import numpy as np
import subprocess as sp

def plogp(p):
    if p <= 0:
        return 0
    else:
        return p*math.log(p)/math.log(2)

def H(p):
    return -plogp(p) - plogp(1-p)


N=100
x = np.array(range(N+1))/N
y = [H(p) for p in x]

plt.plot(x,y)
plt.xlabel("表が出る確率p")
plt.ylabel("エントロピー")
imgname = 'picture/entropy.png'
plt.savefig(imgname)

sp.run(f'mpv {imgname}', shell=True)


