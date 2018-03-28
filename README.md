# gsyslog
George's application syslog type of logger
Create an easy to use logger facility the act similar to the Linux syslog,
but can be used by any application. That way a user application can write
logs very similar to root syslog an be consistant.

To check out a copy of the source:
    cd base-location
    git clone https://github.com/fulkgl/gsyslog.git

Run each of the following with:
    Python 2.7.13

Run unit tests:
    cd base-location
    python tests\unittest_gsyslog.py

To check the coding standards and minor quality check:
    cd base-location
    pycodestyle pybaccarat\playingcards.py
    pycodestyle pybaccarat\baccarat.py
    pycodestyle pybaccarat\baccaratsystems.py
    pycodestyle bin\play_baccarat.py
    pylint --rcfile=\usr\local\bin\pylint2.rc pybaccarat\playingcards.py
    pylint --rcfile=\usr\local\bin\pylint2.rc pybaccarat\baccarat.py
    pylint --rcfile=\usr\local\bin\pylint2.rc pybaccarat\baccaratsystems.py
    pylint --rcfile=\usr\local\bin\pylint2.rc bin\play_baccarat.py

To run the build and make distribution packages:
    cd base-location
    python setup.py sdist bdist_egg
    rem dist/* contains source and binary distribution packages


How to publish to git and pypi.
1. create project and files
    1.1 gsyslog\gsyslog.py and __init__.py
    1.2 tests\unittest_gsyslog.py and __init__.py
    1.3 setup.cfg
    1.4 setup.py
    1.5 README.md
    1.6 MANIFEST.in
    1.7 LICENSE (use MIT, avoid GNU)
    1.8 .gitignore and doxygen.cfg (optional)
2. run unittest to success
3. pycharm vcs/git/add the whole project