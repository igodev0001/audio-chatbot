# Nima
This project is a simple chat bot implementation called Nima, which takes user audio input, displays it in text and performs operations. The program makes use of open source speech recognition tools and various libraries/modules available on the PyPI documentation website. Microsoft Speech API (SAPI version 5) used for speech synthesis and communication.

Please install all required modules using the pip command before you run the program.

IMPORTANT: There is no wheel (prebuilt package) for Python 3.7 on Windows (there is one for Python 2.7 and 3.4 up to 3.6) so you need to prepare build environment on your PC to use this package. Easier would be finding the wheel for 3.7 as some packages are quite hard to build on Windows. 
Christoph Gohlke (University of California, Irvine) hosts Windows wheels for most popular packages for nearly all modern Python versions, including latest PyAudio. You can download the required PyAudio file from the link given below:
https://www.lfd.uci.edu/~gohlke/pythonlibs/

Here’s a step by step process:
•	Find your Python version by python --version (3.7.3 for example)
•	The easiest way to check either you have 64 or 32 Python just open it in the terminal. Most users today have 64 bit machines and the same variant running for Python
•	Find the appropriate .whl file from the link provided above. For example mine is PyAudio 0.2.11 cp37 cp37m win_amd64.whl, and download it.
•	Remember to place the downloaded PyAudio file in the same folder as the code, Otherwise the program won’t work.
•	install the .whl file with pip
