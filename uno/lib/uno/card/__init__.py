#!
# -*- coding: utf-8 -*-

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

from .database import DataBase

from .datasource import DataSource

from .options import OptionsManager

from .oauth2 import getOAuth2Version

from .logger import getLogger

from .dbtool import getConnectionUrl
from .dbtool import getDriverPropertyInfos
from .dbtool import getSqlException

from .unotool import checkVersion
from .unotool import createMessageBox
from .unotool import createService
from .unotool import getDesktop
from .unotool import getDialog
from .unotool import getExtensionVersion
from .unotool import getFileSequence
from .unotool import getResourceLocation
from .unotool import getSimpleFile
from .unotool import getStringResource
# FIXME Import necessary exclusively for vCardOOo
from .unotool import getUrl

from .oauth2 import g_extension as g_oauth2ext
from .oauth2 import g_version as g_oauth2ver

from .jdbcdriver import g_extension as g_jdbcext
from .jdbcdriver import g_identifier as g_jdbcid
from .jdbcdriver import g_version as g_jdbcver

from .configuration import g_identifier
from .configuration import g_extension
from .configuration import g_protocol
from .configuration import g_defaultlog
from .configuration import g_scheme
from .configuration import g_host

from .dbconfig import g_folder
from .dbconfig import g_version

