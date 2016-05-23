**zipic**(ZIP Images Compressor) is a console utility purposed for compressing images that contains in
 provided ZIP archive.
 
 **zipic** require installed **python 3** and **pngquant**

> **_Note:_** Current version only converts PNG format images.

Usage
-----

Syntax for usage of **zipic** is very simple.
Type the next command in the parent directory of the **zipic** python package in the **terminal**:

    $ python zipic -h
    usage: Zipic [-h] [-v {0,1,2}] file

    This is the console app intended for compressing image files nested in ZIP
    archive
    
    positional arguments:
      file                  A path to the file.
    
    optional arguments:
      -h, --help            show this help message and exit
      -v {0,1,2}, --verbosity {0,1,2}
                            increase output verbosity


To compress all png files in your zip archive you should provide path to this
ZIP archive or any PNG file:

    $ python zipic tmp/water_.png

and it will be silently compressed to optimal size 256 colors image.


To increase verbosity use ``-v`` optional key with ``1``:


    $ python zipic tmp/sandbox.zip -v 1 
    INFO:root:Running the Zipic...
    INFO:root:"tmp/sandbox.zip" is a zip file
    INFO:root:PNG files in given zip =>
    sky/1.png, sky/2.png, nTEBkdbTA.png, prohibition.png, sunbird.png
    INFO:root:Processing PNG files...
    INFO:root:Update the source archive...
    INFO:root:"zip" console call:
        updating: sky/1.png (deflated 0%)
        updating: sky/2.png (deflated 0%)
        updating: nTEBkdbTA.png (deflated 0%)
        updating: prohibition.png (deflated 0%)
        updating: sunbird.png (deflated 1%)
        
    INFO:root:Done!
