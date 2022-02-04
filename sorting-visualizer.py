import gui
import algorithms
import pygame
import random
pygame.init()


def generate_starting_list(n, min_val, max_val):
    lst = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    return lst


def main():
    run = True
    clock = pygame.time.Clock()

    length = 150
    min_val = 0
    max_val = 20
    lst = generate_starting_list(length, min_val, max_val)

    draw_info = gui.DrawInformation(1000, 600, lst)
    sorting = False
    sorting_algorithm = algorithms.merge_sort
    sorting_algorithm_generator = None

    while run:
        clock.tick(60)

        gui.draw(draw_info)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            gui.draw(draw_info)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = generate_starting_list(length, min_val, max_val)
                draw_info.set_lst(lst)
                sorting = False

            elif event.key == pygame.K_SPACE and sorting is False and sorting_algorithm == algorithms.merge_sort:
                start = 0
                end = len(draw_info.lst)
                print(draw_info.lst)
                sorting_algorithm(draw_info, draw_info.lst, start, end)

            elif event.key == pygame.K_SPACE and sorting is False and sorting_algorithm == algorithms.quick_sort:
                lst = draw_info.lst
                sorting_algorithm(draw_info, lst, 0, len(lst)-1)

            elif event.key == pygame.K_SPACE and sorting is False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info)

    pygame.quit()


if __name__ == "__main__":
    main()
