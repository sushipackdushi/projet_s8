import numpy as np
import random
from collections import deque

def generate_regions(num_regions: int, num_dimensions: int) -> np.ndarray:
    """
    Generate grid of size 'num_dimensions' that is divided into 'num_regions' contiguous regions
    
    Parameters:
        num_regions (int): Number of regions.
        num_dimensions (int): Size of the square grid.
    
    Returns:
        np.ndarray: A NumPy array containing coordinate arrays for each region.
    """
    # Initialize grid with -1 (unassigned)
    grid = np.full((num_dimensions, num_dimensions), -1, dtype=int)
    
    # Generate all positions and randomly pick seed positions for each region
    all_positions = [(i, j) for i in range(num_dimensions) for j in range(num_dimensions)]
    random.shuffle(all_positions)
    seeds = all_positions[:num_regions]
    
    # Use a queue for multi-seed flood fill and a dict to store each region's coordinates
    queues = deque()
    regions_dict = {i: [] for i in range(num_regions)}
    
    # Assign seeds and initialize the queue
    for region, (x, y) in enumerate(seeds):
        grid[x, y] = region
        queues.append((x, y, region))
        regions_dict[region].append((x, y))
    
    # Define possible neighbor directions (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Flood fill until all cells are assigned
    while queues:
        x, y, region = queues.popleft()
        random.shuffle(directions)  # Randomize the order of expansion
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < num_dimensions and 0 <= ny < num_dimensions and grid[nx, ny] == -1:
                grid[nx, ny] = region
                queues.append((nx, ny, region))
                regions_dict[region].append((nx, ny))
    
    # Print the grid view (matrix representation)
    print("Grid representation:")
    print(grid)
    
    # Return an array of coordinate arrays (each region's coordinates)
    return np.array([np.array(regions_dict[r]) for r in range(num_regions)], dtype=object)
