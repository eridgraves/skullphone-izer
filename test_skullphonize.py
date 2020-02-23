# test_skullphonize.py
# Eric Graves
# created 02/22/20

# A file to test the skullphonizer using pytest. Since input/output are images,
# there are not very many possible tests outside of weirdly-shaped images and
# various file types. Mostly, we just care that the code compiles and runs
# without throwing errors, since image quality is hard to test for (without
# comparing versus sample outputs).

from skullphonize_image import skullphonize_img
from PIL import Image
import pytest

IMG_SQUARE = 'IMG_3723_ART.PNG' # Bad practice: should have sparate test images for different file types
IMG_PORT = 'lighthouse.jpg'
IMG_LAND = 'planets.jpg'
SCALE = 20

def test_square():
    """
    Test with a Square image.
    """
    out_img = Image.fromarray(skullphonize_img(IMG_SQUARE, SCALE))

def test_landscape():
    """
    Test with a Landscape image. (vconcat/hconcat tests)
    """
    out_img = Image.fromarray(skullphonize_img(IMG_LAND, SCALE))

def test_portrait():
    """
    Test with a Portrait image. (vconcat/hconcat tests)
    """
    out_img = Image.fromarray(skullphonize_img(IMG_PORT, SCALE))

def test_input_format():
    """
    Test image formats (PNG and JPG). Already covered elsewhere.
    """
    jpg_img = Image.fromarray(skullphonize_img(IMG_PORT, SCALE))
    png_img = Image.fromarray(skullphonize_img(IMG_SQUARE, SCALE))
