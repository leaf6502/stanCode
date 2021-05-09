"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x = GRAPH_MARGIN_SIZE + ((width - GRAPH_MARGIN_SIZE * 2) / len(YEARS)) * year_index
    return x


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # 畫水平線
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)

    # 畫垂直線
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)  # 畫線
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)  # 寫字


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    for n in range(len(lookup_names)):
        name = lookup_names[n]
        if name in name_data:  # 如果name在name_data中，要印出線跟文字
            x_axis = []  # 儲存x座標
            y_axis = []  # 儲存y座標
            for i in range(len(YEARS)):
                year = str(YEARS[i])
                x = get_x_coordinate(CANVAS_WIDTH, i)
                x_axis.append(x)
                if year in name_data[name]:
                    rank = name_data[name][year]
                    if int(rank) < 1000:
                        y = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / 1000 * int(rank)
                        canvas.create_text(x + TEXT_DX, y, text=name + rank, anchor=tkinter.NW, fill=COLORS[n])  # 寫字
                    else:  # 如果rank>1000
                        y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                        canvas.create_text(x + TEXT_DX, y, text=name + '*', anchor=tkinter.NW, fill=COLORS[n])  # 寫字
                else:
                    y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    canvas.create_text(x + TEXT_DX, y, text=name + '*', anchor=tkinter.SW, fill=COLORS[n])  # 寫字
                y_axis.append(y)
                # 畫線
                if len(x_axis) > 1:
                    canvas.create_line(x_axis[i-1], y_axis[i-1], x_axis[i], y_axis[i], width=LINE_WIDTH, fill=COLORS[n])


                # 畫線
                # for j in range(len(x_axis)):
                #     for k in range(len(y_axis)):
                #         canvas.create_line(x_axis[j], y_axis[k], x_axis[j+1], y_axis[k+1], width=LINE_WIDTH)









# canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
#     canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT -
#




# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)





    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
