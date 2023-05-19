# Performance Analysis - Optimization of Python Through Integration with C++ and Cython
## Overview
This is the final project for the _Python Developer - Specializing in AI_ educaction at __Teknikhögskolan__ in Göteborg.<br><br>
The subject of the thesis is to measure and compare performance of Python-versions from _2.7_ to _3.11_ and then optimize the performance with C++ and Cython. The Python code is written to run through all different versions, which means the syntax and functionalities is kept on a basic level.<br>
_pyenv_ is used to run the code on all different Python versions and the C++ integration is performed in a separate project. All test cases for the project are located in either the __functions__, __cpp__ or __cython__ directories.

## Results
The final results can be found in the _doc/results_ directory. The final project report will be added when its finalized.

## Run
To perform the test cases on different version, you need to install _pyenv_ and run the code through a terminal. There are different arguments to use in the CLI (the Cython test cases needs to be compiled before run, use setup.py):
```
-d --dict : Run dictionary test cases
-g --generator : Run generator test cases
-i --iterator : Run iterator test cases
-l --list : Run list test cases
-s --set : Run set test cases
-t --tuple : Run tuple test cases
--cython : Run cython test cases
```
To locally install dependencies through pip:
```
pip install -r requirements.txt
```
