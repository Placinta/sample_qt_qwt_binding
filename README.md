# Super minimal example of binding the Qt QWT library using Shiboken and CMake

Only tested on macOS 10.12, Python 2.7. 
Prerequisites:
- Assumes Qt 5.9.x is already installed via online installer
- Assumes Qt For Python (PySide2) is installed in the current python virtualenv
- Some recent version of XCode installed (9.x)
- Some recent version of CMake installed (3.1+)

# Building QWT library
Download qwt source code at http://qwt.sourceforge.net/ (I used version 6.1.3 at
https://sourceforge.net/projects/qwt/files/qwt/6.1.3/)

- Extract source to directory of preference (for me ~/Dev/qwt/source)
- Change installation location by editing qwt/source/qwtconfig.pri and setting `QWT_INSTALL_PREFIX = ~/Dev/qwt/installed`
- Build it
```cd ~/Dev/qwt/build
~/Dev/Qt/5.9.4/clang_64/bin/qmake ../source/qwt.pro
make -j8
make install
```

# Building and testing QWT bindings
- Clone this repo to ~/Dev/qwt/py
- Build the bindings and install them to source directory
``` ./build.sh ```
- Test a super minimal app
``` python test_plot.py```

# Clean up
``` git clean -xfd ```

# License

Same as rest of Qt examples, dual Commercial / BSD license.

I couldn't find the proper template.
