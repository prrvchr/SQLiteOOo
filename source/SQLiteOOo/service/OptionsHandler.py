#!
# -*- coding: utf_8 -*-

"""
╔════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                    ║
║   Copyright (c) 2020 https://prrvchr.github.io                                     ║
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

import uno
import unohelper

from com.sun.star.awt import XContainerWindowEventHandler

from com.sun.star.lang import XServiceInfo

from hsqldriver import OptionsManager

from hsqldriver import g_identifier

import traceback

# pythonloader looks for a static g_ImplementationHelper variable
g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationName = '%s.OptionsHandler' % g_identifier


class OptionsHandler(unohelper.Base,
                     XServiceInfo,
                     XContainerWindowEventHandler):
    def __init__(self, ctx):
        self._ctx = ctx
        self._manager = None

    # XContainerWindowEventHandler
    def callHandlerMethod(self, window, event, method):
        try:
            handled = False
            if method == 'external_event':
                if event == 'initialize':
                    self._manager = OptionsManager(self._ctx, window)
                    handled = True
                elif event == 'ok':
                    self._manager.saveSetting()
                    handled = True
                elif event == 'back':
                    self._manager.loadSetting()
                    handled = True
            elif method == 'Base':
                self._manager.setDriverService(0)
                handled = True
            elif method == 'Enhanced':
                self._manager.setDriverService(1)
                handled = True
            elif method == 'Level0':
                self._manager.setConnectionService(0)
                handled = True
            elif method == 'Level1':
                self._manager.setConnectionService(1)
                handled = True
            elif method == 'Level2':
                self._manager.setConnectionService(2)
                handled = True
            return handled
        except Exception as e:
            print("ERROR: %s - %s" % (e, traceback.format_exc()))

    def getSupportedMethodNames(self):
        return ('external_event',
                'Base',
                'Enhanced',
                'Level0',
                'Level1',
                'Level2')

    # XServiceInfo
    def supportsService(self, service):
        return g_ImplementationHelper.supportsService(g_ImplementationName, service)
    def getImplementationName(self):
        return g_ImplementationName
    def getSupportedServiceNames(self):
        return g_ImplementationHelper.getSupportedServiceNames(g_ImplementationName)


g_ImplementationHelper.addImplementation(OptionsHandler,                            # UNO object class
                                         g_ImplementationName,                      # Implementation name
                                         (g_ImplementationName,))                   # List of implemented services
