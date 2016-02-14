Rendering Service
=================


Usage
-----

Convert web page to PDF:

    GET:/pdf?url=<url>

Convert web page to IMG:

    GET:/img?url=<url>

Add watermark to image:

    GET:/watermark?[proportion=<proportion|1.5>&]text=<text>&url=<url>
    
Resize image:

    GET:/resize?[x=<width|450>&][y=<height|450>&]url=<url>
    
Know Issues
-----------

* Resize: Size selection doesn't work 
* Watermark: Proportion selection doesn't work
