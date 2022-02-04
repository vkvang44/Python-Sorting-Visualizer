import pygame
import math
pygame.init()


class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 75, 230, 35
    LIGHT_GREEN = 75, 215, 35
    RED = 230, 75, 35
    LIGHT_RED = 220,20,60
    YELLOW = 255, 234, 0
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [
        (105, 135, 213),
        (151, 186, 236),
        (187, 223, 250)
    ]

    FONT = pygame.font.SysFont('comicsans', 30)
    LARGE_FONT = pygame.font.SysFont('comicsans', 40)
    SIDE_PADDING = 100
    TOP_PADDING = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_lst(lst)

    def set_lst(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PADDING) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PADDING) / (self.max_val - 0))
        self.start_x = self.SIDE_PADDING // 2


def draw(draw_info, sorting_algo_name, cur_speed, curr_length):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(f"{sorting_algo_name} ", 1, draw_info.GRADIENTS[0])
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))

    algo = draw_info.FONT.render("1 - Bubble | 2 - Insertion | 3 - Selection | 4 - Quick | 5 - Merge", 1,
                                 draw_info.GRADIENTS[1])
    draw_info.window.blit(algo, (draw_info.width / 2 - algo.get_width() / 2, 55))

    controls = draw_info.FONT.render(f"R - Reset | SPACE - Start | S - Change Speed ({cur_speed}) "
                                     f"| Q - Change Size ({curr_length})", 1, draw_info.GRADIENTS[1])
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 100))

    draw_lst(draw_info)
    pygame.display.update()


def draw_lst(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst
    if clear_bg:
        clear_rect = (draw_info.SIDE_PADDING // 2, draw_info.TOP_PADDING,
                      draw_info.width - draw_info.SIDE_PADDING, draw_info.height - draw_info.TOP_PADDING)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    color_idx = 0
    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        if val == draw_info.min_val:
            half_block_height = draw_info.block_height // 2
            block_height_diff = half_block_height + (half_block_height // 2)
            y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
            y -= block_height_diff
        else:
            y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.GRADIENTS[color_idx]
        if color_idx >= 2:
            color_idx = 0
        else:
            color_idx += 1

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

    if clear_bg:
        pygame.display.update()
