from PIL import Image

def load_image(image_path):
    return Image.open(image_path)

# Ganti 'nama_gambar.png' dengan nama gambar Anda
image = load_image('mot.jpg')
def text_to_binary(text):
    binary_data = ''.join(format(ord(char), '08b') for char in text)
    return binary_data

# Ganti 'data_yang_ingin_disematkan' dengan data yang ingin Anda sematkan
data_to_hide = "This is dark world"
binary_data = text_to_binary(data_to_hide)
def hide_data(image, data):
    data_index = 0
    data_length = len(data)

    width, height = image.size
    for y in range(height):
        for x in range(width):
            pixel = list(image.getpixel((x, y)))

            for i in range(3):
                if data_index < data_length:
                    # Mengganti LSB dengan bit data
                    pixel[i] = pixel[i] & ~1 | int(data[data_index])
                    data_index += 1

            image.putpixel((x, y), tuple(pixel))

    return image

# Menyematkan data ke dalam gambar
image_with_hidden_data = hide_data(image.copy(), binary_data)
def save_image(image, output_path):
    image.save(output_path)

# Ganti 'output_gambar.png' dengan nama file keluaran yang Anda inginkan
output_path = 'hide.jpg'
save_image(image_with_hidden_data, output_path)