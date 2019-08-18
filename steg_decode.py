from PIL import Image


def flatten_image(new_img):
    pixel_values = []
    for i in range(new_img.size[0]):

        for j in range(new_img.size[1]):

            for num in pixels[i, j]:
                pixel_values.append(num)

    return pixel_values


def steg_find(px_values, alphabets):

    # conver decimal to binary
    bin_str = ""
    for value in px_values:

        bin_str += format(value, '#010b')[-1]

    # take 8 bit at a time convert to decimal to alphabets
    result = ""

    for i in range(0, len(bin_str), 8):
        index = int(bin_str[i:i+8], 2)
        if 0 < index <= 26:
            result += alphabets[index-1]

    return result


filename = input("Enter the image that has a message encoded: ")
img = Image.open(filename, "r")

pixels = img.load()

alphabets = "abcdefghijklmnopqrstuvwxyz"


px_values = flatten_image(img)

result = steg_find(px_values, alphabets)

print("NOTE: LOOK FOR THE TEXT AT THE START OF THE MESSAGE")
print("Decoded text is: {}".format(result))
