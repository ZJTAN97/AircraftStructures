import matplotlib.pyplot as plt
import numpy as np

bending_moments = [117720, 529740, 735750, 662175, 294300]

stacked_moments = []
current_bending = sum(bending_moments)

for moment in bending_moments:
    current_bending = current_bending - moment
    stacked_moments.append(current_bending)

stacked_moments.insert(0, sum(bending_moments))




distance = [0, 3, 9, 15, 22.5, 30.0]


plt.plot(distance, [moment*-1 for moment in stacked_moments], marker='o', color='b')
plt.xlabel('Distance (m)')
plt.ylabel('Moments (Nm) ')
plt.ylim([-sum(bending_moments), sum(bending_moments)])
plt.axhline(linewidth=2, color='black')
plt.axvline(linewidth=2, color='black')
plt.grid()
plt.show()