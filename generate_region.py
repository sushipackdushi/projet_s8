import numpy as np
import random
from collections import deque

def generate_regions(num_regions: int, num_dimensions: int) -> (np.ndarray, list):
    """
    Generate a grid of size 'num_dimensions' x 'num_dimensions' that is divided into 
    'num_regions' contiguous regions and produce a list of coordinates for each region.
    
    Parameters:
        num_regions (int): Number of regions.
        num_dimensions (int): Size of the square grid.
    
    Returns:
        tuple:
            np.ndarray: The grid with each cell assigned a region number.
            list: A list of length 'num_regions', where each element is a sorted list of 
                  (x, y) tuples indicating the coordinates in the grid for that region.
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
    
    # Create a sorted list of coordinates for each region ordered by region number
    region_coords_list = [sorted(regions_dict[i]) for i in range(num_regions)]
    
    # Print the grid view (matrix representation)
    print("Grid representation:")
    print(grid)
    
    # Print the coordinates of each region with each coordinate on a new line
    print("\nList of sorted coordinates for each region:")
    for idx, coords in enumerate(region_coords_list):
        print(f"Region {idx}:")
        for coord in coords:
            print(f"  {coord}")
        print()  # newline for spacing between regions
    
    return grid, region_coords_list

# Example usage:
grid, region_coords = generate_regions(3, 4)
