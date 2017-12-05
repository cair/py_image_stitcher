# py_image_stitcher - Stiching since 2017!
A small library for stitching images together.
Add a issue to this repository if you require additional functionality. If you want to contribute, make a pull request!


## Install
Only tested in Python 3
```python
pip install https://github.com/UIA-CAIR/py_image_stitcher.git
```

## Example Usage
```python
from py_image_stitcher import ImageStitch
import numpy as np
from PIL import Image

imarray = np.random.rand(100, 100, 3) * 255
img = Image.fromarray(imarray.astype('uint8')).convert('RGB')
img2 = np.zeros((84, 84, 3), dtype=np.uint8)
img3 = np.random.rand(100, 100, 1) * 255
img3 = img3.astype('uint8')

stitch = ImageStitch((84, 84))
stitch.add(img)
stitch.add(img, row=1, column=1)
stitch.add(img, row=2, column=2)
stitch.add(img, row=3, column=3)
stitch.save("./image.png")

```


## Licence
Copyright 2017 Per-Arne Andersen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.