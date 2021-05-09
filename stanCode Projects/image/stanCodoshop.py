"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO: photoshop
"""

import os
import sys
import math
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):  # 取出指定點的color distance
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    color_distance = math.sqrt((red - pixel.red) ** 2 + (green - pixel.green) ** 2 + (blue - pixel.blue) ** 2 )
    return color_distance


def get_average(pixels):  # 取各pixel red, green, blue的平均
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red_sum = 0
    green_sum = 0
    blue_sum = 0
    # int = []
    for pixel in pixels:
        red_sum += pixel.red
        green_sum += pixel.green
        blue_sum += pixel.blue
    red_avg = red_sum // len(pixels)
    green_avg = green_sum // len(pixels)
    blue_avg = blue_sum // len(pixels)
    int = [red_avg, green_avg, blue_avg]
    return int


def get_best_pixel(pixels):  # 取color_distance最近的pixel
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    rgb_avg = get_average(pixels)  # get the average red, green, blue of the pixels
    red = rgb_avg[0]
    green = rgb_avg[1]
    blue = rgb_avg[2]
    inf = float('inf')
    min_color_distance = inf
    for pixel in pixels:  # 不同張圖的同一個座標
        color_distance = get_pixel_dist(pixel, red, green, blue)  # put the average red, green, blue of the pixels
        if color_distance < min_color_distance:
            min_color_distance = color_distance
            best = pixel
    return best

    # pixel_distance = {}  # record the color distance of each pixel
    # for pixel in pixels:
    #     color_distance = get_pixel_dist(pixel, red, green, blue)  # put the average red, green, blue of the pixels
    #     pixel_distance[pixel] = color_distance
    # min_distance = min(pixel_distance)
    # for pixel, color_distance in pixel_distance:  # 找color_distance最小的key
    #     if color_distance == min_distance:
    #         return pixel
            # return pixel.red, pixel.green, pixel.blue


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    # green_im = SimpleImage.blank(20, 20, 'green')
    # green_pixel = green_im.get_pixel(0, 0)
    # print(get_pixel_dist(green_pixel, 5, 255, 10))

    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # # print(get_average([green_pixel, green_pixel, green_pixel, blue_pixel]))
    # best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    # print(best1.red, best1.green, best1.blue)

    ######## YOUR CODE ENDS HERE ###########

    for x in range(width):
        for y in range(height):
            pixels = []  # 選定座標後，打開每張圖取他的特定座標x,y
            for image in images:  # 打開每個image
                pixel = image.get_pixel(x, y)
                result_pixel = result.get_pixel(x, y)
                pixels.append(pixel)  # 把pixel放到list裡面
                best = get_best_pixel(pixels)  # 得到最好的pixel
                result_pixel.red = best.red  # 把最好的pixel送給result
                result_pixel.green = best.green
                result_pixel.blue = best.blue

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
