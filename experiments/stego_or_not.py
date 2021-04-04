from PIL import Image

with Image.open('images_and_texts/pink_flower.jpg') as og_img:
    og_img.show()
    og_px = og_img.load()

    with Image.open('images_and_texts/stego_flower.jpg') as stego_img:
        stego_img.show()
        stego_px = stego_img.load()

        for row in range(og_img.size[1]):
            for col in range(og_img.size[0]):
                if og_px[col,row][2] == stego_px[col, row][2]:
                    print('NO CHANGE', og_px[col,row][2], '==', stego_px[col,row][2])
                else:
                    print('CHANGED', og_px[col,row][2], '!=', stego_px[col,row][2])