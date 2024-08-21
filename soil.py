import numpy as np
import matplotlib.pyplot as plt

# Grid size
size = 50
erosion_factor = 0.01

# Initialize grid with random heights
grid = np.random.rand(size, size)

# Function to simulate erosion
def erode(grid, erosion_factor):
    new_grid = np.copy(grid)
    for i in range(1, grid.shape[0] - 1):
        for j in range(1, grid.shape[1] - 1):
            # Compute the average height of the neighboring cells
            average_height = (
                grid[i-1, j] + grid[i+1, j] + grid[i, j-1] + grid[i, j+1]
            ) / 4
            
            # Erode the current cell based on the difference with neighbors
            erosion = erosion_factor * (grid[i, j] - average_height)
            new_grid[i, j] -= erosion
    
    return new_grid

# Simulate erosion for a number of steps
steps = 100
for step in range(steps):
    grid = erode(grid, erosion_factor)

# Plot the final eroded landscape
plt.imshow(grid, cmap='terrain')
plt.colorbar(label='Height')
plt.title('Soil Erosion Simulation')
plt.show()
