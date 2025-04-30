#!
# -*- coding: utf_8 -*-

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

from com.sun.star.logging.LogLevel import INFO
from com.sun.star.logging.LogLevel import SEVERE

from com.sun.star.uno import Exception as UNOException

from sqlite import sdbc
from sqlite import sdbcx

from sqlite import checkConfiguration
from sqlite import getConfiguration
from sqlite import getLogger

from sqlite import g_basename
from sqlite import g_defaultlog
from sqlite import g_identifier
from sqlite import g_services

from threading import Lock
import traceback

# pythonloader looks for a static g_ImplementationHelper variable
g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationName = 'io.github.prrvchr.SQLiteOOo.Driver'
g_ServiceNames = ('io.github.prrvchr.SQLiteOOo.Driver', 'com.sun.star.sdbc.Driver')

# XXX: This class is simply a bootstrap to enable the following:
# XXX: - Provide a single entry for different services meeting the required API levels

class Driver():
    def __new__(cls, ctx, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    logger = getLogger(ctx, g_defaultlog, g_basename)
                    apilevel = getConfiguration(ctx, g_identifier).getByName('ApiLevel')
                    try:
                        checkConfiguration(ctx, logger)
                        if apilevel == 'com.sun.star.sdbc':
                            instance = sdbc.Driver(ctx, cls._lock, logger, g_services[apilevel], g_ImplementationName)
                        else:
                            instance = sdbcx.Driver(ctx, cls._lock, logger, g_services[apilevel], g_ImplementationName)
                        cls._instance = instance
                        logger.logprb(INFO, 'Driver', '__new__', 101, g_ImplementationName, apilevel)
                    except UNOException as e:
                        if cls._logger is None:
                            cls._logger = logger
                        logger.logprb(SEVERE, 'Driver', '__new__', 102, g_ImplementationName, apilevel, e.Message)
                        raise e
        return cls._instance

    # XXX: If the driver fails to load then we keep a reference
    # XXX: to the logger so we can read the error message later
    _logger = None
    _instance = None
    _lock = Lock()

g_ImplementationHelper.addImplementation(Driver,                          # UNO object class
                                         g_ImplementationName,            # Implementation name
                                         g_ServiceNames)                  # List of implemented services
