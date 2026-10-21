#!
# -*- coding: utf-8 -*-

"""
╔════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                    ║
║   Copyright (c) 2020-25 https://prrvchr.github.io                                  ║
║                                                                                    ║
║   Permission is hereby granted, free of charge, to any person obtaining            ║
║   a copy of this software and associated documentation files (the "Software"),     ║
║   to deal in the Software without restriction, including without limitation        ║
║   the rights to use, copy, modify, merge, publish, distribute, sublicense,         ║
║   and/or sell copies of the Software, and to permit persons to whom the Software   ║
║   is furnished to do so, subject to the following conditions:                      ║
║                                                                                    ║
║   The above copyright notice and this permission notice shall be included in       ║
║   all copies or substantial portions of the Software.                              ║
║                                                                                    ║
║   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,                  ║
║   EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES                  ║
║   OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.        ║
║   IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY             ║
║   CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,             ║
║   TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE       ║
║   OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                                    ║
║                                                                                    ║
╚════════════════════════════════════════════════════════════════════════════════════╝
"""

import unohelper

from sqlite.sdbc.driver import Driver as SdbcDriver
from sqlite.sdbcx.driver import Driver as SdbcxDriver

from sqlite.unotool import getConfiguration

from sqlite.configuration import g_identifier

from threading import RLock

# pythonloader looks for a static g_ImplementationHelper variable
g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationName = 'io.github.prrvchr.SQLiteOOo.Driver'
g_ServiceNames = ('io.github.prrvchr.SQLiteOOo.Driver',
                  'com.sun.star.sdbc.Driver')

# XXX: This class is simply a bootstrap to enable the following:
# XXX: - Provide a single entry for different services meeting the required API levels
# XXX: - Log any errors that occur while loading the Java driver


class Driver():
    def __new__(cls, ctx):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    config = getConfiguration(ctx, g_identifier)
                    level = config.getByName('ApiLevel')
                    instance = SdbcDriver if level == 0 else SdbcxDriver
                    cls._instance = instance(ctx, config, cls._lock, level, g_ImplementationName)
        return cls._instance

    _instance = None
    _lock = RLock()


g_ImplementationHelper.addImplementation(Driver,                          # UNO object class
                                         g_ImplementationName,            # Implementation name
                                         g_ServiceNames)                  # List of implemented services
