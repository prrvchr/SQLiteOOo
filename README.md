<!--
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
-->
# [![SQLiteOOo logo][1]][2] Documentation

**Ce [document][3] en français.**

**The use of this software subjects you to our [Terms Of Use][4].**

# version [1.1.0][5]

## Introduction:

**SQLiteOOo** is part of a [Suite][6] of [LibreOffice][7] ~~and/or [OpenOffice][8]~~ extensions allowing to offer you innovative services in these office suites.  

This extension allows you to use [SQLite JDBC][9] database in embedded mode, making the database portable (a single odb file).

Being free software I encourage you:
- To duplicate its [source code][10].
- To make changes, corrections, improvements.
- To open [issue][11] if needed.

In short, to participate in the development of this extension.  
Because it is together that we can make Free Software smarter.

___

## Requirement:

The SQLiteOOo extension uses the jdbcDriverOOo extension to work.  
It must therefore meet the [requirement of the jdbcDriverOOo extension][12].

This extension cannot be installed together with the [HyperSQLOOo][13] extension.  
It's one or the other, but at the moment they can't work together (see [issue #156471][14]).

**On Linux and macOS the Python packages** used by the extension, if already installed, may come from the system and therefore **may not be up to date**.  
To ensure that your Python packages are up to date it is recommended to use the **System Info** option in the extension Options accessible by:  
**Tools -> Options -> Base drivers -> Embedded SQLite Driver -> View log -> System Info**  
If outdated packages appear, you can update them with the command:  
`pip install --upgrade <package-name>`

For more information see: [What has been done for version 1.1.0][15].

___

## Installation:

It seems important that the file was not renamed when it was downloaded.
If necessary, rename it before installing it.

- [![jdbcDriverOOo logo][16]][17] Install **[jdbcDriverOOo.oxt][18]** extension [![Version][19]][18]

    This extension is necessary to use SQLite version 3.42.0.0 with all its features.

- ![SQLiteOOo logo][20] Install **[SQLiteOOo.oxt][21]** extension [![Version][22]][21]

Restart LibreOffice / OpenOffice after installation.

**On Windows, restarting LibreOffice may not be enough.**  
To ensure that LibreOffice restarts correctly, use the Windows Task Manager to verify that no LibreOffice services are visible after LibreOffice is shut down.

___

## Use:

### How to create a new database:

In LibreOffice / OpenOffice go to File -> New -> Database...:

![SQLiteOOo screenshot 1][23]

In step: Select database:
- select: Create a new database
- in: Emdedded database: choose: Embedded SQLite Driver
- click on button: Next

![SQLiteOOo screenshot 2][24]

In step: Save and proceed:
- adjust the parameters according to your needs...
- click on button: Finish

![SQLiteOOo screenshot 3][25]

Have fun...

___

## How does it work:

SQLiteOOo is an [com.sun.star.sdbc.Driver][26] UNO service written in Python.  
It is an overlay to the [jdbcDriverOOo][17] extension allowing to store the SQLite database in an odb file (which is, in fact, a compressed file).

Its operation is quite basic, namely:

- When requesting a connection, three things are done:
    1. If it does not already exist, a **subdirectory** with name: `.` + `odb_file_name` + `.lck` is created in the location of the odb file where all SQLite files are extracted from the **database** directory of the odb file (unzip).
    2. A [DocumentHandler][27] is added as an [com.sun.star.util.XCloseListener][28] and [com.sun.star.document.XStorageChangeListener][29] to the odb file.
    3. The [jdbcDriverOOo][17] extension is used to get the [com.sun.star.sdbc.XConnection][30] interface from the **subdirectory** path + `odb_file_name`.

- When closing or renaming (Save as) an odb file the [DocumentHandler][27] copy all the files present in the **subdirectory** into the (new) **database** directory of the odb file (zip) and then delete the **subdirectory**.

___

## Has been tested with:

* OpenOffice 4.1.8 - Ubuntu 20.04 - LxQt 0.14.1

* OpenOffice 4.1.8 - Windows 7 SP1

* LibreOffice 7.0.4.2 - Ubuntu 20.04 - LxQt 0.14.1

* LibreOffice 6.4.4.2 - Windows 7 SP1

* LibreOffice 7.6.0.1 - Windows 10

* LibreOffice 7.6.0.1 - Ubuntu 22.04

I encourage you in case of problem :confused:  
to create an [issue][10]  
I will try to solve it :smile:

___

## Historical:

### What has been done for version 1.0.0:

- Integration of SQLite JDBC version 3.42.0.0. I especially want to thank [gotson][31] for the [many improvements to the SQLite JDBC driver][32] that made it possible to use SQLite in LibreOffice/OpenOffice.

### What has been done for version 1.0.1:

- Fixed [bug 156511][33] occurring when using the com.sun.star.embed.XStorage interface. The [workaround][34] is to use the copyElementTo() method instead of moveElementTo(). Versions of LibreOffice 7.6.x and higher become usable.

### What has been done for version 1.0.2:

- The absence or obsolescence of **jdbcDriverOOo** extension necessary for the proper functioning of **SQLiteOOo** now displays an error message.

- Many other things...

### What has been done for version 1.1.0:

- All Python packages necessary for the extension are now recorded in a [requirements.txt][35] file following [PEP 508][36].
- Now if you are not on Windows then the Python packages necessary for the extension can be easily installed with the command:  
  `pip install requirements.txt`
- Modification of the [Requirement][37] section.

### What remains to be done for version 1.1.0:

- Add new language for internationalization...

- Anything welcome...

[1]: </img/sqlite.svg#collapse>
[2]: <https://prrvchr.github.io/SQLiteOOo/>
[3]: <https://prrvchr.github.io/SQLiteOOo/README_fr>
[4]: <https://prrvchr.github.io/SQLiteOOo/source/SQLiteOOo/registration/TermsOfUse_en>
[5]: <https://prrvchr.github.io/SQLiteOOo#historical>
[6]: <https://prrvchr.github.io/>
[7]: <https://www.libreoffice.org/download/download/>
[8]: <https://www.openoffice.org/download/index.html>
[9]: <https://github.com/xerial/sqlite-jdbc>
[10]: <https://github.com/prrvchr/SQLiteOOo/>
[11]: <https://github.com/prrvchr/SQLiteOOo/issues/new>
[12]: <https://prrvchr.github.io/jdbcDriverOOo/#requirement>
[13]: <https://prrvchr.github.io/HyperSQLOOo/#requirement>
[14]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156471>
[15]: <https://prrvchr.github.io/SQLiteOOo/#what-has-been-done-for-version-110>
[16]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.svg#middle>
[17]: <https://prrvchr.github.io/jdbcDriverOOo>
[18]: <https://github.com/prrvchr/jdbcDriverOOo/releases/latest/download/jdbcDriverOOo.oxt>
[19]: <https://img.shields.io/github/v/tag/prrvchr/jdbcDriverOOo?label=latest#right>
[20]: <img/SQLiteOOo.svg#middle>
[21]: <https://github.com/prrvchr/SQLiteOOo/releases/latest/download/SQLiteOOo.oxt>
[22]: <https://img.shields.io/github/downloads/prrvchr/SQLiteOOo/latest/total?label=v1.1.0#right>
[23]: <img/SQLiteOOo-1.png>
[24]: <img/SQLiteOOo-2.png>
[25]: <img/SQLiteOOo-3.png>
[26]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/Driver.html>
[27]: <https://github.com/prrvchr/SQLiteOOo/blob/main/uno/lib/uno/embedded/documenthandler.py>
[28]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/util/XCloseListener.html>
[29]: <http://www.openoffice.org/api/docs/common/ref/com/sun/star/document/XStorageChangeListener.html>
[30]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/XConnection.html>
[31]: <https://github.com/gotson>
[32]: <https://github.com/xerial/sqlite-jdbc/issues/786>
[33]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156511>
[34]: <https://github.com/prrvchr/uno/commit/a2fa9f5975a35e8447907e51b0f78ac1b1b76e17>
[35]: <https://github.com/prrvchr/SQLiteOOo/tree/main/source/SQLiteOOo/requirements.txt>
[36]: <https://peps.python.org/pep-0508/>
[37]: <https://prrvchr.github.io/SQLiteOOo/#requirement>
