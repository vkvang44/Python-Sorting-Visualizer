import pygame
import random
import math
pygame.init()


class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 75, 230, 35
    LIGHT_GREEN = 75, 215, 35
    RED = 230, 75, 35
    LIGHT_RED = 220,20,60
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
        pygame.display.set_caption("Sorting Algorithm Visualization")
        self.set_lst(lst)

    def set_lst(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PADDING) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PADDING) / (self.max_val - 0))
        self.start_x = self.SIDE_PADDING // 2


def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1,draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 5))

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
            half = draw_info.block_height // 2
            y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
            y -= half
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


def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst


def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            draw_lst(draw_info, {j: draw_info.GREEN, j + 1: draw_info.LIGHT_GREEN}, True)
            yield True

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_lst(draw_info, {j: draw_info.RED, j + 1: draw_info.LIGHT_RED}, True)
                yield True

    return lst


def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    draw_lst(draw_info, {0: draw_info.GREEN}, True)
    yield True

    for i in range(1, len(lst)):
        current = lst[i]

        draw_lst(draw_info, {i: draw_info.GREEN}, True)
        yield True

        while True:
            ascending_sort = i > 0 and lst[i-1] > current and ascending

            if not ascending_sort:
                break

            draw_lst(draw_info, {i-1: draw_info.LIGHT_GREEN, i: draw_info.GREEN}, True)
            yield True

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current
            draw_lst(draw_info, {i: draw_info.RED, i+1: draw_info.LIGHT_RED}, True)
            yield True

    return lst


def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst)):
        draw_lst(draw_info, {i: draw_info.GREEN}, True)
        yield True
        min_idx = i

        for j in range(i+1, len(lst)):
            draw_lst(draw_info, {min_idx: draw_info.GREEN, j: draw_info.LIGHT_GREEN}, True)
            yield True

            if lst[min_idx] > lst[j]:
                min_idx = j
                draw_lst(draw_info, {min_idx: draw_info.GREEN}, True)
                yield True

        draw_lst(draw_info, {i: draw_info.RED, min_idx: draw_info.LIGHT_RED}, True)
        yield True
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

        draw_lst(draw_info, {i: draw_info.LIGHT_RED, min_idx: draw_info.RED}, True)
        yield True

    return lst

def main():
    run = True
    clock = pygame.time.Clock()

    length = 15
    min_val = 1
    max_val = 50
    lst = generate_starting_list(length, min_val, max_val)


    # create the gui interface
    draw_info = DrawInformation(1000, 600, lst)
    sorting = False
    ascending = True
    sorting_algorithm = insertion_sort
    sorting_algorithm_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(60)

        draw(draw_info)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = generate_starting_list(length, min_val, max_val)
                draw_info.set_lst(lst)
                sorting = False

            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)

            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_a and not sorting:
                ascending = False

    pygame.quit()


if __name__ == "__main__":
	main()