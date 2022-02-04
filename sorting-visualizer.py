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

    length = 25
    min_val = 0
    max_val = 75
    curr_length = "Small"
    lst = generate_starting_list(length, min_val, max_val)

    draw_info = gui.DrawInformation(1500, 1000, lst)
    sorting = False
    sorting_algorithm = None
    sorting_algo_name = "Sorting Algorithm Visualizer"
    sorting_algorithm_generator = None

    speed = 60
    curr_speed = "Fast"

    while run:
        clock.tick(speed)

        gui.draw(draw_info, sorting_algo_name, curr_speed, curr_length)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            gui.draw(draw_info, sorting_algo_name, curr_speed, curr_length)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                speed = 60
                sorting = False
                lst = generate_starting_list(length, min_val, max_val)
                draw_info.set_lst(lst)

            elif event.key == pygame.K_SPACE and sorting is False:
                if sorting_algorithm == algorithms.merge_sort or sorting_algorithm == algorithms.quick_sort:
                    start = 0
                    end = len(draw_info.lst)
                    if sorting_algorithm == algorithms.quick_sort:
                        end -= 1
                    if curr_speed == "Slow" and sorting_algorithm == algorithms.merge_sort:
                        speed = 50
                    elif curr_speed == "Slow" and sorting_algorithm == algorithms.quick_sort:
                        speed = 100
                    else:
                        speed = 2
                    sorting_algorithm(draw_info, draw_info.lst, start, end, speed)

                elif sorting_algorithm is not None:
                    if curr_speed == "Slow":
                        speed = 3
                    sorting = True
                    sorting_algorithm_generator = sorting_algorithm(draw_info)

            elif event.key == pygame.K_1 and not sorting:
                sorting_algorithm = algorithms.bubble_sort
                sorting_algo_name = "1. Bubble Sort"

            elif event.key == pygame.K_2 and not sorting:
                sorting_algorithm = algorithms.insertion_sort
                sorting_algo_name = "2. Insertion Sort"

            elif event.key == pygame.K_3 and not sorting:
                sorting_algorithm = algorithms.selection_sort
                sorting_algo_name = "3. Selection Sort"

            elif event.key == pygame.K_4 and not sorting:
                sorting_algorithm = algorithms.quick_sort
                sorting_algo_name = "4. Quick Sort"

            elif event.key == pygame.K_5 and not sorting:
                sorting_algorithm = algorithms.merge_sort
                sorting_algo_name = "5. Merge Sort"

            elif event.key == pygame.K_s and not sorting:
                if curr_speed == "Fast":
                    curr_speed = "Slow"
                else:
                    curr_speed = "Fast"

            elif event.key == pygame.K_q and not sorting:
                if curr_length == "Small":
                    curr_length = "Medium"
                    length = 50
                elif curr_length == "Medium":
                    curr_length = "Large"
                    length = 75
                elif curr_length == "Large":
                    curr_length = "Small"
                    length = 25
                lst = generate_starting_list(length, min_val, max_val)
                draw_info.set_lst(lst)

    pygame.quit()


if __name__ == "__main__":
    main()
