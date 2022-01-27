import pygame
import random
import math
pygame.init()


class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [
        (105, 135, 213),
        (151, 186, 236),
        (187, 223, 250)
    ]
    SIDE_PADDING = 100
    TOP_PADDING = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualization")
        self.set_lst(lst)

    def set_lst(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PADDING) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PADDING) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PADDING // 2


# drawing the screen
def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    draw_lst(draw_info)
    pygame.display.update()


# draw out the list
def draw_lst(draw_info):
    lst = draw_info.lst

    color_idx = 0
    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.GRADIENTS[color_idx]
        if color_idx >= 2:
            color_idx = 0
        else:
            color_idx += 1

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))



def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst


def main():
    run = True
    clock = pygame.time.Clock()

    length = 14
    min_val = 0
    max_val = 100
    lst = generate_starting_list(length, min_val, max_val)

    print(lst)
    # create the gui interface
    draw_info = DrawInformation(800, 600, lst)

    while run:
        clock.tick(60)

        draw(draw_info)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == "__main__":
	main()