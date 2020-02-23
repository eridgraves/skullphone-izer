# sklphn_gui.py
# Eric Graves
# Created: 2/23/20

# Serve GUI for Skullphonizer project

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw
import sys
import os
import tkinter as tk
from skullphonize_image import skullphonize_img

def call_sklphnize():
    #print("Called with %s , %s" % (e1.get(), e2.get()))
    TEST_IMAGE_IN = e1.get()
    IMAGE_SCALE_IN = int(e2.get())
    # Call skullphonize_img()
    processed_img = skullphonize_img(TEST_IMAGE_IN, IMAGE_SCALE_IN)

    # Output resulting image
    if processed_img is not None:
        fig = plt.figure(figsize=(12,6))
        p_orig = fig.add_subplot(2,2,1)
        p_orig.set_title("Original Image")
        img = plt.imread(TEST_IMAGE_IN, 0)
        plt.imshow(img)
        p_scaled = fig.add_subplot(2,2,2)
        fig.subplots_adjust(left=0.13, bottom=0, right=0.9, top=0.9, wspace=0.2, hspace=0.06)
        p_scaled.set_title("Skullphone-ized Image")
        plt.imshow(processed_img)
        plt.show()

        # Save to file: hacky, TODO: fix later
        img_out = Image.fromarray(processed_img)

        #-- strip extension, add scale

        img_out_name = os.path.splitext(TEST_IMAGE_IN)[0] + "_" + str(IMAGE_SCALE_IN) + os.path.splitext(TEST_IMAGE_IN)[1]
        img_out.save(img_out_name)
        print("File saved as " + img_out_name)

    else:
        print("Error with file type.")


master = tk.Tk()
tk.Label(master, text="Image Name").grid(row=0)
tk.Label(master, text="Scale").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

# Buttons
tk.Button(master, text="skullphone-ize", command=call_sklphnize).grid(row=2, column=1)
tk.Button(master, text="quit", command=master.quit).grid(row=2, column=3)


master.mainloop()
