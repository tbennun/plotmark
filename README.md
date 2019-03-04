# Plot markers for Matplotlib
This code adds oriented line markers on existing line plots, marking on or between points.

## Usage

Call `plotmark` with a matplotlib `Line2D` object and a list of x points to draw markers at. Additional keyword arguments may be used to override marker style.

## Example

Running the following code:

```python
import numpy as np
import matplotlib.pyplot as plt
import plotmark as pm

x = np.arange(0.0, 2.0, 0.01)
y = 1 + np.sin(2 * np.pi * x)
p = plt.plot(x, y)

pm.plotmark(p[0], np.arange(0.0, 2.0, 0.15))
plt.savefig('example.png')
```

would yield:

![example 1](example1.png)

In a denser range, the output would be:

![example 2](example2.png)
