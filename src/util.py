storage = []



def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    return tuple(int(value[i:i + 2], 16)*257 for i in range(0, 6, 2))

def create_circle(x, y, r, canvas, **kwargs): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, **kwargs)
