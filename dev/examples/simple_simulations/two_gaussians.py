"""Creates a 2D hyperspectrum consisting of two gaussians and plots it.

This example can serve as starting point to test other functionalities on the simulated hyperspectrum.

"""


# If running from hyperspy's interactive the next two imports can be omitted 
# omitted (i.e. the next 4 lines)
import numpy as np
import matplotlib.pyplot as plt

from hyperspy.signals.spectrum import Spectrum

# Create an empty spectrum
s = Spectrum({'data' : np.zeros((32,32,1024))})

# Generate some simple data: two Gaussians with random centers and area

# First we create a model
m = create_model(s)

## Define the first gaussian
gs1 = components.Gaussian()
# Add it to the model
m.append(gs1)

# Set the sparameters
gs1.sigma.value = 10
# Make the center vary in the -5,5 range around 128
gs1.origin.map['values'][:] = 256 + (np.random.random((32,32)) - 0.5) * 10
gs1.origin.map['is_set'][:] = True

# Make the area vary between 0 and 10000
gs1.A.map['values'][:] = 10000 * np.random.random((32,32))
gs1.A.map['is_set'][:] = True

## Second gaussian
gs2 = components.Gaussian()
# Add it to the model
m.append(gs2)

# Set the parameters
gs2.sigma.value = 20

# Make the center vary in the -10,10 range around 768
gs2.origin.map['values'][:] = 768 + (np.random.random((32,32)) - 0.5) * 20
gs2.origin.map['is_set'][:] = True

# Make the area vary between 0 and 20000
gs2.A.map['values'][:] = 20000 * np.random.random((32,32))
gs2.A.map['is_set'][:] = True

# Create the dataset
m.generate_cube()

# Assign the data generated to the Spectrum with some poissonian noise
s.data = np.random.poisson(m.model_cube)

# Plot the result

s.plot()

# If running from hyperspy's interactive console the next line can be 
# omitted
plt.show()


