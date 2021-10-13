import matplotlib.pyplot as plt
import numpy as np

bending_moments = [117720, 529740, 735750, 662175, 294300]
shear_forces = [186390, 147150, 88290, 39240, 9810]

stacked_moments = []
current_bending = sum(bending_moments)
distance = [0, 3, 9, 15, 22.5, 30.0]


for moment in bending_moments:
    current_bending = current_bending - moment
    stacked_moments.append(current_bending)

stacked_moments.insert(0, sum(bending_moments))


distance_2 = [3, 6, 6, 7.5, 7.5]
area = []

for i, force in enumerate(shear_forces):
    area.append(force * distance_2[i])


stacked_area = []
current_area = sum(area)
for item in area:
    current_area = current_area - item
    stacked_area.append(current_area)

stacked_area.insert(0, sum(area))


plt.plot(distance, [area*-1 for area in stacked_area], marker='o', color='b')
plt.xlabel('Distance (m)')
plt.ylabel('Moments (Nm) ')
plt.ylim([-sum(bending_moments), sum(bending_moments)])
plt.axhline(linewidth=2, color='black')
plt.axvline(linewidth=2, color='black')
plt.grid()
plt.show()