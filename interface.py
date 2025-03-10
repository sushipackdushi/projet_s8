# interface.py
import tkinter as tk
from generate_region import generate_regions

def draw_grid(num_regions: int, grid_size: int):
    """
    Create a resizable GUI window displaying a 'grid_size x grid_size' grid
    with thick borders. Each cell is colored and labeled according to the 
    region number obtained from 'generate_regions' in 'generate_region.py'.
    
    Parameters:
        num_regions (int): Number of contiguous regions to generate.
        grid_size (int): The size of the square grid (grid_size x grid_size).
    """
    # 1) Call 'generate_regions' to get the grid data
    region_grid, region_coords = generate_regions(num_regions, grid_size)

    # 2) Create the main window
    root = tk.Tk()
    root.title(f"{grid_size}x{grid_size} Region Grid")

    # 3) Set up a canvas
    canvas_size = 600  # Initial size of the canvas in pixels
    border_thickness = 5
    canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="white")
    canvas.pack(fill="both", expand=True)

    # A lighter pastel color palette
    color_palette = [
        "#B5EAD7", "#FFDAC1", "#FF9AA2", "#C7CEEA", "#FFB7B2",
        "#E2F0CB", "#C1E1C1", "#FAD2E1", "#F9F7C9", "#A2D2FF"
    ]

    def resize_grid(event):
        """
        Clear the canvas and redraw the grid lines, colored cells,
        and region numbers whenever the window is resized.
        """
        canvas.delete("all")  # Clear any previous drawings

        width = canvas.winfo_width()
        height = canvas.winfo_height()

        # Calculate the size of each cell based on current window size
        cell_width = width / grid_size
        cell_height = height / grid_size

        # 4) First, fill each cell with its region color and label it
        for row in range(grid_size):
            for col in range(grid_size):
                region_number = region_grid[row, col]
                
                # Determine the color for this region (cycling through palette if needed)
                color = color_palette[region_number % len(color_palette)]
                
                # Coordinates for the rectangle
                x1 = col * cell_width
                y1 = row * cell_height
                x2 = (col + 1) * cell_width
                y2 = (row + 1) * cell_height
                
                # Draw a rectangle for the cell with the region's color
                canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color, outline=""
                )
                
                # Place the region number text in the center of the cell
                x_center = x1 + (cell_width / 2)
                y_center = y1 + (cell_height / 2)
                canvas.create_text(
                    x_center, y_center,
                    text=str(region_number),
                    font=("Helvetica", 30, "bold"),  # Font size set to 30
                    fill="#202123",                  # Dark mode color
                    anchor="center"
                )

        # 5) Draw the grid lines on top (so they appear over the colored cells)
        for i in range(grid_size + 1):
            line_width = border_thickness if i == 0 or i == grid_size else 2

            # Horizontal lines
            canvas.create_line(
                0, i * cell_height,
                width, i * cell_height,
                width=line_width, fill="black"
            )
            # Vertical lines
            canvas.create_line(
                i * cell_width, 0,
                i * cell_width, height,
                width=line_width, fill="black"
            )

    # Redraw the grid whenever the canvas is resized
    canvas.bind("<Configure>", resize_grid)

    # 6) Run the GUI event loop
    root.mainloop()


# Example usage:
if __name__ == '__main__':
    # Adjust these values to try different settings
    NUM_REGIONS = 3
    GRID_SIZE = 4
    draw_grid(NUM_REGIONS, GRID_SIZE)
