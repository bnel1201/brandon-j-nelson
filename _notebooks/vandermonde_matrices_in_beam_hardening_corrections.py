import numpy as np
import random
import matplotlib.pyplot as plt
from skimage.data import shepp_logan_phantom
from skimage.transform import radon, rescale, iradon

def poly_recon(A, theta):
  """Argument is projection vandermonde matrix [proj.ravel() X view angles] and theta array, returns recon.ravel() X deg matrix of vandermonde recons"""
  deg=A.shape[1]
  sz = int(A.shape[0]/theta.size)
  A=A.reshape([sz,theta.size,deg])
  f = np.zeros([sz*sz,deg])
  for i in range(deg):
      fi=iradon(A[:,:,i],theta=theta, circle=True)
      f[:,i]=fi.ravel()
  return f
  
def vanderRecon(proj, theta, deg):
  """Argument is [xpix*ypix X theta] projection, returns [recon.ravel() X deg] matrix of vandermonde reconstructed projections"""
  A=np.vander(corrupted_r.ravel(),deg, increasing=True)
  return poly_recon(A,theta);

def mse(y_hat,y):
   return ((y_hat-y)**2).mean()

def add_lines(r):
    n_lines = int(random.random()*40)
    for i in range(n_lines):
      line_intensity = random.uniform(0.5,1)
      line_width = int(10*random.random())
      line_location = int(random.random()*r.shape[0])
      r[line_location:line_location+line_width,:]*=line_intensity
    return r

def beamHardening(x, lam=1): #here we cannot separate mu and penetration distance so we have to assume them to be equal
  return x/(1+lam*x)

def corruptProjection(proj, bh_strength = 0.01):
  m = add_lines(np.ones(proj.shape))
  corrupted_r = beamHardening(proj*m, lam = bh_strength)
  return m, corrupted_r 

def vanderComborecon(q,m,theta,deg):
  qm = np.polynomial.polynomial.polyvander2d(q.ravel(), m.ravel(), [deg-1, deg-1])
  return poly_recon(qm,theta)

def square(c):
  return c.reshape([int(np.sqrt(len(c))), -1])

def performCorrection2D(q, m, c):
  return np.polynomial.polynomial.polyval2d(q.ravel(),m.ravel(),square(c)).reshape(q.shape)

def visualizeCoefficients(c):
  c = square(c)
  plt.imshow(c)
  plt.xlabel('M')
  plt.ylabel('q')
  plt.colorbar()
  plt.title('Monomial contributions')
  return c

def find2Dpolynomialcoefficients(corrupted_r, m, ideal, theta, deg):
  f = vanderComborecon(corrupted_r,m,theta, deg)
  return np.linalg.lstsq(f,ideal.ravel(),rcond=None)[0]

def correctAndDisplay(corrupted_r, m, c, theta):
  p = performCorrection2D(corrupted_r, m, c)
  corrected = iradon(p, theta=theta, circle=True)
  plt.imshow(corrected, cmap=plt.cm.Greys_r)
  return corrected