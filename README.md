Rendering Service
=================

Installation
------------

### Ubuntu

    virtual env
    chmod +x pre_install.sh && sudo ./pre_install.sh
    . env/bin/activate
    python setup.py install


Usage
-----

### Convert web page to PDF:

    GET:/pdf?url=<url>
    --- OR ---
    POST:/pdf
    BODY: <HTML>

### Convert web page to IMG:

    GET:/img?url=<url>
    --- OR ---
    POST:/img
    BODY: <HTML>

### Add watermark to image:

    GET:/watermark?url=<url>&text=<text>
    --- OR ---
    POST:/watermark?text=<text>
    BODY: <IMG_FILE>

#### Additional options:

* `proportion=<proportion|1.5>` - Size of text
* `font=<font>` - Name of font
* `rotation=<angle>` - Angle relative to the horizon
* `repeat=<none/x/y/xy>` - Repeat of text

### Resize image:

    GET:/resize?url=<url>
    --- OR ---
    POST:/resize
    BODY: <IMG_FILE>

#### Additional options:

* `x=<width|450>>`
* `y=<height|450>`
* `proportions=<true/false>`
    
Know Issues
-----------

TBD
