from PIL import Image


def message_to_binary(message, alphabets):
    bin_message = ""

    for letter in message:
        index = alphabets.find(letter)+1
        bin_message += format(index, '#010b')[2:]

    return bin_message


def flatten_image(new_img):
    pixel_values = []
    for i in range(new_img.size[0]):

        for j in range(new_img.size[1]):

            for num in pixels[i, j]:
                pixel_values.append(num)

    return pixel_values


def alter_pixels(pixel_values, bin_message):
    for idx in range(len(bin_message)):
        if (bin_message[idx] == "1" and pixel_values[idx] % 2 == 0) or (bin_message[idx] == "0" and pixel_values[idx] % 2 != 0):
            pixel_values[idx] = (pixel_values[idx] + 1) % 256

    return pixel_values


def stitch_image(pixels, pixel_values):
    k = 0
    i = 0

    while i < new_img.size[0] and k+2 < len(pixel_values):
        j = 0
        while j < new_img.size[1] and k+2 < len(pixel_values):

            r, g, b = pixel_values[k], pixel_values[k+1], pixel_values[k+2]
            # print((i, j), (r, g, b))
            pixels[i, j] = (r, g, b)

            k += 3
            j += 1

        i += 1


filename = input("Enter the name of an image: ")
new_img = Image.open(filename, "r")

pixels = new_img.load()

# TODO: check if message can fit inside the image
message = input("Enter a message:")

alphabets = "abcdefghijklmnopqrstuvwxyz"

bin_message = message_to_binary(message, alphabets)

pixel_values = flatten_image(new_img)

pixel_values = alter_pixels(pixel_values, bin_message)

stitch_image(pixels, pixel_values)

new_img.save("steg_{}".format(filename), "bmp")

print("Message encoded in the file steg_{}".format(filename))
