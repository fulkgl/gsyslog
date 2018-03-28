#!/usr/bin/python

"""!
@package TBD
Unit test for the gsyslog procedure.

To execute the unit test from base dir location, enter:
@code
cd base_location
set pythonpath=.
python tests\unittest_gsyslog.py [-v]
@endcode
@author <A email="fulkgl@gmail.com">fulkgl@gmail.com</A>
"""

__author__ = "George L Fulk"
__version__ = 0.10

import unittest  # this is a unit test module
import os  # delete file needs this
import sys  # add curdir to PythonPath

sys.path.append(".")  # "   "      "  "
from gsyslog import gsyslog  # the target of the test


def delete_file(filespec):
    """!
    Delete a file if it exists.
    @param filespec file to delete
    """
    if os.path.exists(filespec):
        os.remove(filespec)


def read_file_contents(filespec):
    """!
    Read the contents of a file and return those contents as a string of bytes.
    @param filespec String file specification to read
    @return string contents of the file, or an empty "" string for file
        find and read error.
    :rtype: string
    :str filespec: file specification to read from
    """
    read_file_contents_str = ""
    try:
        read_file_contents_str = open(filespec, "rb").read()
    except Exception as ex:
        print("Exeception(%s)(%s)" % (type(ex), str(ex)))
        # read_file_contents_str = ""
    return read_file_contents_str


class TestCard(unittest.TestCase):
    """!
    Unit test for the gsyslog module.
    """

    def test_simple(self):
        """!
        Simple log example.
        """
        temp_file = "/tmp/ut1.log"
        delete_file(temp_file)
        log = gsyslog.start_log(temp_file)  # default to retail info+ level
        log.debug("low level debug build only")
        log.info("retail build")
        log.warn("handled error")
        # log.shutdown()
        # log = None
        contents = read_file_contents(temp_file)
        #!< @TODO delete_file file in use still here.
        # delete_file(temp_file)
        # ....v....1....v....2....v....3....v....4....v....5....v....6....v....7....v....8....v....9....v....0....v....1
        # 2018-03-26 11:30:51,424       start_log:69   INFO     ==start_log== filespec(/tmp/ut1.log) name() level(20)
        # 2018-03-26 11:30:51,424     test_simple:42   INFO     retail build
        # 2018-03-26 11:30:51,424     test_simple:43   WARNING  handled error
        # ---
        #
        # some amount of logging needs to have happened
        self.assertTrue(0 < len(contents), "file should have some length >0")
        # split the lines, should be 3 lines of output, tailing \n causes 4.
        out = contents.split('\n')
        actual1 = len(out)
        self.assertEqual(4, actual1, "expect 3 lines of output(%d)" % actual1)
        # Lets walk the first line of output
        actual2 = out[0][23:40]
        self.assertEqual("       start_log:",
                         actual2,
                         "proc name(%s)" % actual2)
        actual3 = out[0][45:]
        if actual3[-1] == '\r':     # Windows EOLN is \r\n not just \n
            actual3 = actual3[:-1]  # so remove the \r is present
        expect3 = "INFO     ===gsyslog.start_log(log_filespec='%s',"+\
                  "log_name='%s',log_level=%d)"
        self.assertEqual(expect3 % (temp_file,'',20),
                         actual3,
                         "tail(%s)" % actual3)
        actual4 = out[1][23:40]
        actual5 = out[2][23:40]
        self.assertEqual("     test_simple:",
                         actual4,
                         "proc name(%s)" % actual4)
        self.assertEqual("     test_simple:",
                         actual5,
                         "proc name(%s)" % actual5)
        actual6 = out[1][45:]
        actual7 = out[2][45:]
        if actual6[-1] == '\r':
            actual6 = actual6[:-1]
        if actual7[-1] == '\r':
            actual7 = actual7[:-1]
        self.assertEqual("INFO     retail build",
                         actual6,
                         "tail(%s)" % actual6)
        self.assertEqual("WARNING  handled error",
                         actual7,
                         "tail(%s)" % actual7)
        self.assertTrue(len(out[3]) < 2, "should be empty line")

    def test_tostring(self):
        """!
        test __str__ method
        """
        # temp_file = "/tmp/ut2.log"
        # delete_file(temp_file)
        log = gsyslog.start_log()
        actual = str(log)
        expect = "<logging.RootLogger object at 0x0000000005277940>"
        #         ....v....1....v....2....v....3....v....4....v....5
        self.assertEqual(expect[:33], actual[:33], "str(%s)" % actual)

    @unittest.skip('do not run')
    def test_hash(self):
        """!
        __hash__
        """
        card1 = Card(5, 's')
        card2 = Card(7, 'h')
        card3 = Card(5, 's')
        h1 = card1.__hash__()
        # print("h1(%s)" % str(h1))
        self.assertTrue(h1 == card3.__hash__(), "card 1 and 3 same value")
        self.assertFalse(h1 == card2.__hash__(), "card 1 and 2 diff")

    # @unittest.skip('do not run')
    def test_inherit(self):
        """!
        inheritted things from parent class:
        ['__class__', '__delattr__', '__dict__', '__doc__', '__format__',
        '__getattribute__', '__hash__', '__init__', '__module__', '__new__',
        '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
        '__sizeof__', '__str__', '__subclasshook__', '__weakref__',

        'critical', 'debug', 'disabled', 'error', 'exception', 'fatal', 'info',
        'warn', 'warning',
        'addFilter', 'filter', 'filters', 'removeFilter',
        'addHandler', 'callHandlers', 'removeHandler', 'handle', 'handlers',
        'findCaller', 'getChild', 'parent',
        'getEffectiveLevel', 'isEnabledFor',
        'level', 'setLevel',
        '_log', 'log', 'makeRecord', 'manager', 'name', 'propagate', 'root', ]
        @todo inherit tests
        """
        # check namespace values
        log = gsyslog.start_log()
        # print("dir_log(%s)"%str(dir(log)))
        class_actual = str(log.__class__)
        self.assertEqual("<class 'logging.RootLogger'>", class_actual,
                         ".class(%s)" % class_actual)
        module_actual = str(log.__module__)
        self.assertEqual("logging", module_actual,
                         ".module(%s)" % module_actual)
        """
        docstring = c5s.__doc__
        self.assertTrue(isinstance(docstring, str), "docstring is string")
        self.assertTrue(0 < len(docstring), "some string of >0 exists")
        # __repr__  (<method-wrapper '__repr__' of Card object at 0x0336FD50>)
        # __sizeof__(<built-in method __sizeof__ of Card object at 0x02A08F70>)
        """

    # @todo usage examples


#
# Command line entry point
#
if __name__ == '__main__':
    unittest.main()
