# main.py
import matplotlib.pyplot as plt
from solar_system_3d import SolarSystem, SolarSystemBody

solar_system = SolarSystem(400)

body = SolarSystemBody(solar_system, 100, velocity=(1,1,1))
body.draw()
body.move()
body.draw()

plt.show()