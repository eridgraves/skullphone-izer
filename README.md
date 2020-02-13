# skullphone-izer
Make images into the style of Skullphone's "digital media painting" artwork.


Here is an example of the current input/output of the notebook:
![Example Output](example_output.PNG)

## Usage:
**In Terminal**
- cd to the same directory as process_image.py and the desired image.
- Run the script with python (requires NumPy, OpenCV2, MatPlotLib, PIL, sys), with the image and scale as arguments:
    - "python skullphonize_image.py IMG_3723_ART.PNG 20"
- If a readable image is given, MatPlotLib will open a window showing input and output images side-by-side.
- Errors will be printed to the terminal.

**In Jupyter**
- Just open and run the notebook cell-by-cell.

## TODO:
- ~~Working prototype on single image~~
- ~~Fix first cluster junk bug.~~
- ~~Fix mysterious range error.~~
- ~~Make image scale user-configurable.~~
- ~~Script assumes that the image is square.~~ --> Now just goes off of rescaled image width. Should be fine.
- ~~Move processing code to single function.~~
- ~~Refactor to single cell, remove test/exploration code.~~
- ~~Migrate to .py script.~~
- ~~Make input/output images flexbily nameable/user specified.~~

- Write tests.  
- Build out GUI for input/output?
- Move to webapp (Docker based?)
- Expand to process video in real-time (ish). Use to build a "mirror".
