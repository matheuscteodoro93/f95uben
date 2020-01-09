import numpy as np
from netCDF4 import Dataset as dt
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

fname = 'datas_small_rotation.nc'
fp = dt(fname, 'r')

# print(fp.variables)

x = np.array(fp.variables['X Distance'][:])
y = np.array(fp.variables['Y Distance'][:])
#t = np.array(fp.variables['T Time'][:])
h = np.array(fp.variables['H_Level'][:])
#u = np.array(fp.variables['U_Velocity'][:])
#v = np.array(fp.variables['V_Velocity'][:])

#uv = (u**2.0 + v**2.0)**0.5

# regridding data for smoother values

X, Y = np.meshgrid(x,y)

#X, Y = np.mgrid[0:10:1001j, 0:10:1001j]
#H = np.zeros((10001,1001,1001))
'''
for i in range(0, 10001):
    H[i,:,:] = griddata(x, y, h[i,:,:], (X, Y), method='linear')
'''

fig = plt.figure()


ax = fig.gca(projection='3d')

##plot_args = {'rstride': 1, 'cstride': 1, 'facecolor':
##             'blue', 'linewidth': 0.01, 'antialiased': True,
##             'shade': True}


#plot_args = {'rstride': 1, 'cstride': 1, 'cmap':
#             'winter', 'linewidth': 0.01, 'antialiased': True,
#             'shade': True, 'vmin':0.99, 'vmax':1.0025}

#plot_args = {'rstride': 2, 'cstride': 2, 'linewidth': 1, 'antialiased': True,
#       'shade': True, 'vmin':0.99, 'vmax':1.0025, 'facecolors':'black'}
plot_args = {'rstride': 2, 'cstride': 2, 'linewidth': 0.5}



for i in range(0, 10001, 10):
    j=i/10
    ax.clear()
    surf = ax.plot_wireframe(X, Y, h[i,:,:], **plot_args)
    ax.set_xlabel('y')
    ax.set_ylabel('x')
    ax.set_zlabel('h')
    ax.set_xlim([-5, 5])
    ax.set_ylim([-6, 6])

    if j <=20:
     ax.set_zlim([0.99, 1.003])
    else:
     ax.set_zlim([0.995, 1.0025])

    plt.pause(1e-3)
    plt.savefig('output/snap%i' % j)
    print('snapshot %i ready' % j)
