import matplotlib.pyplot as plt
import math
import japanize_matplotlib
import numpy as np
import subprocess as sp

def p(x, mu, sigma2):
    return math.exp(-(x-mu)**2/(2*sigma2))/math.sqrt(2*math.pi*sigma2)

N=100
ratio = np.array(range(N+1))/N

x = 5*(ratio-0.5)
y = [p(x_, 0., 1.) for x_ in x]

plt.plot(x,y)
plt.xlabel("確率変数の取る値x")
plt.ylabel("xを取る確率p(x)")
plt.title("平均0,分散1の正規分布の確率分布")
imgname = 'picture/gaussian.png'
plt.savefig(imgname)

sp.run(f'mpv {imgname}', shell=True)


