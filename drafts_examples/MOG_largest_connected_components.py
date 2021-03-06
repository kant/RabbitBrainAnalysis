import os
import scipy
from scipy import ndimage
import matplotlib.pyplot as plt

fname='/Users/sebastiano/Desktop/index.png'
assert os.path.exists(fname)
blur_radius = 1.0
threshold = 50

img = scipy.misc.imread(fname)  # gray-scale image
print(img.shape)

# smooth the image (to remove small objects)
imgf = ndimage.gaussian_filter(img, blur_radius)
threshold = 50

# find connected components
labeled, nr_objects = ndimage.label(imgf > threshold)
print "Number of objects is %d " % nr_objects

plt.imsave('/tmp/out.png', labeled)
plt.imshow(labeled)

plt.show()