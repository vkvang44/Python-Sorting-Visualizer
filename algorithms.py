import gui
import pygame


def bubble_sort(draw_info):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            gui.draw_lst(draw_info, {j: draw_info.GREEN, j + 1: draw_info.LIGHT_GREEN}, True)
            yield True

            if num1 > num2 :
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                gui.draw_lst(draw_info, {j: draw_info.RED, j + 1: draw_info.LIGHT_RED}, True)
                yield True

    return lst


def insertion_sort(draw_info):
    lst = draw_info.lst

    gui.draw_lst(draw_info, {0: draw_info.GREEN}, True)
    yield True

    for i in range(1, len(lst)):
        current = lst[i]

        gui.draw_lst(draw_info, {i: draw_info.GREEN}, True)
        yield True

        while True:
            ascending_sort = i > 0 and lst[i-1] > current

            if not ascending_sort:
                break

            gui.draw_lst(draw_info, {i-1: draw_info.LIGHT_GREEN, i: draw_info.GREEN}, True)
            yield True

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current
            gui.draw_lst(draw_info, {i: draw_info.RED, i+1: draw_info.LIGHT_RED}, True)
            yield True

    return lst


def selection_sort(draw_info):
    lst = draw_info.lst

    for i in range(len(lst)):
        gui.draw_lst(draw_info, {i: draw_info.GREEN}, True)
        yield True
        min_idx = i

        for j in range(i+1, len(lst)):
            gui.draw_lst(draw_info, {min_idx: draw_info.GREEN, j: draw_info.LIGHT_GREEN}, True)
            yield True

            if lst[min_idx] > lst[j]:
                min_idx = j
                gui.draw_lst(draw_info, {min_idx: draw_info.GREEN}, True)
                yield True

        gui.draw_lst(draw_info, {i: draw_info.RED, min_idx: draw_info.LIGHT_RED}, True)
        yield True
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

        gui.draw_lst(draw_info, {i: draw_info.LIGHT_RED, min_idx: draw_info.RED}, True)
        yield True

    return lst


def quick_sort(draw_info, array, startIdx, endIdx):
    if startIdx >= endIdx:
        return array

    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx

    gui.draw_lst(draw_info,
                 {
                          pivotIdx: draw_info.YELLOW,
                          leftIdx: draw_info.LIGHT_GREEN,
                          rightIdx: draw_info.GREEN},
                 True)
    pygame.time.wait(50)

    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            gui.draw_lst(draw_info,
                         {pivotIdx: draw_info.YELLOW,
                          leftIdx: draw_info.RED,
                          rightIdx: draw_info.LIGHT_RED},
                         True)
            pygame.time.wait(50)

            array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]

            gui.draw_lst(draw_info,
                         {pivotIdx: draw_info.YELLOW,
                          leftIdx: draw_info.RED,
                          rightIdx: draw_info.LIGHT_RED},
                         True)
            pygame.time.wait(50)

            gui.draw_lst(draw_info,
                         {pivotIdx: draw_info.YELLOW,
                          leftIdx: draw_info.LIGHT_GREEN,
                          rightIdx: draw_info.GREEN},
                         True)
            pygame.time.wait(50)

        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1

            gui.draw_lst(draw_info,
                         {pivotIdx: draw_info.YELLOW,
                          leftIdx: draw_info.LIGHT_GREEN,
                          rightIdx: draw_info.GREEN},
                         True)
            pygame.time.wait(50)

        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1

            gui.draw_lst(draw_info,
                         {pivotIdx: draw_info.YELLOW,
                          leftIdx: draw_info.LIGHT_GREEN,
                          rightIdx: draw_info.GREEN},
                         True)
            pygame.time.wait(50)

    gui.draw_lst(draw_info,
                 {pivotIdx: draw_info.YELLOW,
                  rightIdx: draw_info.GREEN},
                 True)
    pygame.time.wait(50)

    gui.draw_lst(draw_info,
                 {pivotIdx: draw_info.RED,
                  rightIdx: draw_info.LIGHT_RED},
                 True)
    pygame.time.wait(50)

    array[pivotIdx], array[rightIdx] = array[rightIdx], array[pivotIdx]

    gui.draw_lst(draw_info,
                 {pivotIdx: draw_info.LIGHT_RED,
                  rightIdx: draw_info.RED},
                 True)
    pygame.time.wait(50)

    left_lst_is_smaller = (rightIdx - 1) - startIdx < endIdx - (rightIdx + 1)
    if left_lst_is_smaller:
        quick_sort(draw_info, array, startIdx, rightIdx - 1)
        quick_sort(draw_info, array, rightIdx + 1, endIdx)
    else:
        quick_sort(draw_info, array, rightIdx + 1, endIdx)
        quick_sort(draw_info, array, startIdx, rightIdx - 1)
