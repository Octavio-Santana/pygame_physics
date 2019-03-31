# Color RGB Values
AQUA = (0, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
GREEN = (0, 128, 0)
LIME = (0, 255, 0)
MAROON = (128, 0 , 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 128, 0)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
CYAN = (  0, 255, 255)

def trans_color(color, alpha):
    c = list(color)
    if alpha < 0 or alpha > 255:
        c.append(255)
    else:
        c.append(int(alpha))
    return tuple(c)