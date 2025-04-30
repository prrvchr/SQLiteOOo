<!--
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
-->
# [![SQLiteOOo logo][1]][2] Documentation

**Ce [document][3] en français.**

**The use of this software subjects you to our [Terms Of Use][4].**

# version [1.2.3][5]

## Introduction:

**SQLiteOOo** is part of a [Suite][6] of [LibreOffice][7] ~~and/or [OpenOffice][8]~~ extensions allowing to offer you innovative services in these office suites.  

This extension allows you to use [SQLite JDBC][9] database in embedded mode, making the database portable (a single odb file).  
It allows you to take advantage of the [ACID][10] properties of the underlying [SQLite][11] database.

Being free software I encourage you:
- To duplicate its [source code][12].
- To make changes, corrections, improvements.
- To open [issue][13] if needed.

In short, to participate in the development of this extension.  
Because it is together that we can make Free Software smarter.

___

## Requirement:

Due to [issue #156471][14] and following [PR#154989][15], the SQLiteOOo extension requires **LibreOffice version 24.2.x** minimum to work.

The SQLiteOOo extension uses the jdbcDriverOOo extension to work.  
It must therefore meet the [requirement of the jdbcDriverOOo extension][16].

If you are using **LibreOffice on Linux** and **LibreOffice was installed with the package manager**, Your Python packages may be system-provided and outdated. The extension's logging will allow you to check if this is the case. It is accessible via the menu: **Tools -> Options -> LibreOffice Base -> Embedded SQLite driver -> View log -> System Info** and requires restarting LibreOffice after activation.  
If outdated packages appear, you can update them with the command:  
`pip install --upgrade <package-name>`

For more information see: [What has been done for version 1.1.0][17].

___

## Installation:

It seems important that the file was not renamed when it was downloaded.  
If necessary, rename it before installing it.

- [![jdbcDriverOOo logo][18]][19] Install **[jdbcDriverOOo.oxt][20]** extension [![Version][21]][20]

    This extension is necessary to use SQLite version 3.42.0.0 with all its features.

- ![SQLiteOOo logo][22] Install **[SQLiteOOo.oxt][23]** extension [![Version][24]][23]

Restart LibreOffice after installation.  
**Be careful, restarting LibreOffice may not be enough.**
- **On Windows** to ensure that LibreOffice restarts correctly, use Windows Task Manager to verify that no LibreOffice services are visible after LibreOffice shuts down (and kill it if so).
- **Under Linux or macOS** you can also ensure that LibreOffice restarts correctly, by launching it from a terminal with the command `soffice` and using the key combination `Ctrl + C` if after stopping LibreOffice, the terminal is not active (no command prompt).

___

## Use:

### How to create a new database:

In LibreOffice / OpenOffice go to File -> New -> Database...:

![SQLiteOOo screenshot 1][25]

In step: Select database:
- select: Create a new database
- in: Emdedded database: choose: Embedded SQLite Driver
- click on button: Next

![SQLiteOOo screenshot 2][26]

In step: Save and proceed:
- adjust the parameters according to your needs...
- click on button: Finish

![SQLiteOOo screenshot 3][27]

Have fun...

___

## How does it work:

SQLiteOOo is an [com.sun.star.sdbc.Driver][28] UNO service written in Python.  
It is an overlay to the [jdbcDriverOOo][19] extension allowing to store the SQLite database in an odb file (which is, in fact, a compressed file).

Its operation is quite basic, namely:

- When requesting a connection, several things are done:
  - If it does not already exist, a **subdirectory** with name: `.` + `odb_file_name` + `.lck` is created in the location of the odb file where all SQLite files are extracted from the **database** directory of the odb file (unzip).
  - The [jdbcDriverOOo][19] extension is used to get the [com.sun.star.sdbc.XConnection][29] interface from the **subdirectory** path + `/sqlite`.
  - If the connection is successful, a [DocumentHandler][30] is added as an [com.sun.star.util.XCloseListener][31] and [com.sun.star.document.XStorageChangeListener][32] to the odb file.
  - If the connection is unsuccessful and the files was extracted in phase 1, the **subdirectory** will be deleted.
- When closing or renaming (Save As) the odb file, if the connection was successful, the [DocumentHandler][30] copies all files present in the **subdirectory** into the (new) **database** directory of the odb file (zip), then delete the **subdirectory**.

The main purpose of this mode of operation is to take advantage of the ACID characteristics of the underlying database in the event of an abnormal closure of LibreOffice.
On the other hand, the function: **file -> Save** has **no effect on the underlying database**. Only closing the odb file or saving it under a different name (File -> Save As) will save the database in the odb file.

___

## Has been tested with:

* LibreOffice 24.2.1.2 - Lubuntu 22.04

* LibreOffice 24.8.0.3 (x86_64) - Windows 10(x64) - Python version 3.9.19 (under Lubuntu 22.04 / VirtualBox 6.1.38)

I encourage you in case of problem :confused:  
to create an [issue][13]  
I will try to solve it :smile:

___

## Historical:

### What has been done for version 1.0.0:

- Integration of SQLite JDBC version 3.42.0.0. I especially want to thank [gotson][33] for the [many improvements to the SQLite JDBC driver][34] that made it possible to use SQLite in LibreOffice/OpenOffice.

### What has been done for version 1.0.1:

- Fixed [bug 156511][35] occurring when using the com.sun.star.embed.XStorage interface. The [workaround][36] is to use the copyElementTo() method instead of moveElementTo(). Versions of LibreOffice 7.6.x and higher become usable.

### What has been done for version 1.0.2:

- The absence or obsolescence of **jdbcDriverOOo** extension necessary for the proper functioning of **SQLiteOOo** now displays an error message.

- Many other things...

### What has been done for version 1.1.0:

- All Python packages necessary for the extension are now recorded in a [requirements.txt][37] file following [PEP 508][38].
- Now if you are not on Windows then the Python packages necessary for the extension can be easily installed with the command:  
  `pip install requirements.txt`
- Modification of the [Requirement][39] section.

### What has been done for version 1.1.1:

- Support for [new features][40] in **jdbcDriverOOo 1.1.2**.

### What has been done for version 1.1.2:

- SQLite driver updated to latest version [SQLite-jdbc-3.45.1.3-SNAPSHOT.jar][41]. This new driver has been implemented to support part of the JDBC 4.1 specifications and more particularly the `java.sql.Statement.getGeneratedKeys()` interface and allows the use of the [com.sun.star.sdbc.XGeneratedResultSet][42] interface.

### What has been done for version 1.1.3:

- Support for the latest version of **jdbcDriverOOo 1.1.4** and the [SQLite-jdbc-3.45.1.6-SNAPSHOT.jar][43].
- Now for proper functioning in Base under: **Edit -> Database -> Advanced Settings... -> Query of generated values** must be left blank. If you want to use an odb file created with a previous version of SQLiteOOo you must change this setting manually.
- Normally the next versions of SQLiteOOo should be able to be updated in the list of extensions installed under LibreOffice: **Tools -> Extension manager... -> Check for Updates**.

### What has been done for version 1.1.4:

- Support for the latest version of **jdbcDriverOOo 1.3.1**.
- When saving under a different name, the database if open will be closed correctly.

### What has been done for version 1.1.5:

- Use of the new data format implemented in version 1.1.4. As a result, if you need to open odb files created with a version lower than 1.1.4 you must first open them with version 1.1.4, otherwise an error will be thrown.

### What has been done for version 1.2.0:

- This version is based on [fix #154989][44] available since LibreOffice 24.2.x. It can therefore work with other extensions offering integrated database services.
- Now SQLiteOOo requires LibreOffice 24.2.x minimum and will load for the url: `sdbc:embedded:sqlite`.

### What has been done for version 1.2.1:

- Updated the [Python packaging][45] package to version 24.1.
- Updated the [Python setuptools][46] package to version 72.1.0.
- The extension will ask you to install the jdbcDriverOOo extension in versions 1.4.2 minimum.

### What has been done for version 1.2.2:

- Fixed [issue #2][47] which appears to be a regression related to the release of JaybirdOOo. Thanks to madalienist for reporting it.
- Updated the [Python setuptools][48] package to version 73.0.1.
- The extension options are now accessible via: **Tools -> Options -> LibreOffice Base -> Embedded SQLite Driver**
- Logging accessible in extension options now displays correctly on Windows.
- Changes to extension options that require a restart of LibreOffice will result in a message being displayed.
- In the extension options it is possible to define the options: **View system tables**, **Use bookmarks** and **Force SQL mode** which will be specific to this driver.
- Requires the latest version of **jdbcDriverOOo 1.4.4**.
- Support for LibreOffice version 24.8.x.

### What has been done for version 1.2.3:

- The extension will ask you to install jdbcDriverOOo extension in versions 1.4.6 minimum.
- Modification of the extension options accessible via: **Tools -> Options -> LibreOffice Base -> Embedded SQLite Driver** in order to comply with the new graphic charter.

### What has been done for version 1.3.0:

- The extension will ask you to install jdbcDriverOOo extension in versions 1.4.6 minimum.
- Modification of the extension options accessible via: **Tools -> Options -> LibreOffice Base -> Embedded SQLite Driver** in order to comply with the new graphic charter.

### What remains to be done for version 1.3.0:

- Add new language for internationalization...

- Anything welcome...

[1]: </img/sqlite.svg#collapse>
[2]: <https://prrvchr.github.io/SQLiteOOo/>
[3]: <https://prrvchr.github.io/SQLiteOOo/README_fr>
[4]: <https://prrvchr.github.io/SQLiteOOo/source/SQLiteOOo/registration/TermsOfUse_en>
[5]: <https://prrvchr.github.io/SQLiteOOo#what-has-been-done-for-version-123>
[6]: <https://prrvchr.github.io/>
[7]: <https://www.libreoffice.org/download/download/>
[8]: <https://www.openoffice.org/download/index.html>
[9]: <https://github.com/xerial/sqlite-jdbc>
[10]: <https://en.wikipedia.org/wiki/ACID>
[11]: <https://www.sqlite.org/transactional.html>
[12]: <https://github.com/prrvchr/SQLiteOOo/>
[13]: <https://github.com/prrvchr/SQLiteOOo/issues/new>
[14]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156471>
[15]: <https://gerrit.libreoffice.org/c/core/+/154989>
[16]: <https://prrvchr.github.io/jdbcDriverOOo/#requirement>
[17]: <https://prrvchr.github.io/SQLiteOOo/#what-has-been-done-for-version-115>
[18]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.svg#middle>
[19]: <https://prrvchr.github.io/jdbcDriverOOo>
[20]: <https://github.com/prrvchr/jdbcDriverOOo/releases/latest/download/jdbcDriverOOo.oxt>
[21]: <https://img.shields.io/github/v/tag/prrvchr/jdbcDriverOOo?label=latest#right>
[22]: <img/SQLiteOOo.svg#middle>
[23]: <https://github.com/prrvchr/SQLiteOOo/releases/latest/download/SQLiteOOo.oxt>
[24]: <https://img.shields.io/github/downloads/prrvchr/SQLiteOOo/latest/total?label=v1.2.3#right>
[25]: <img/SQLiteOOo-1.png>
[26]: <img/SQLiteOOo-2.png>
[27]: <img/SQLiteOOo-3.png>
[28]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/Driver.html>
[29]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/XConnection.html>
[30]: <https://github.com/prrvchr/SQLiteOOo/blob/main/uno/lib/uno/embedded/documenthandler.py>
[31]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/util/XCloseListener.html>
[32]: <http://www.openoffice.org/api/docs/common/ref/com/sun/star/document/XStorageChangeListener.html>
[33]: <https://github.com/gotson>
[34]: <https://github.com/xerial/sqlite-jdbc/issues/786>
[35]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156511>
[36]: <https://github.com/prrvchr/uno/commit/a2fa9f5975a35e8447907e51b0f78ac1b1b76e17>
[37]: <https://github.com/prrvchr/SQLiteOOo/releases/latest/download/requirements.txt>
[38]: <https://peps.python.org/pep-0508/>
[39]: <https://prrvchr.github.io/SQLiteOOo/#requirement>
[40]: <https://prrvchr.github.io/jdbcDriverOOo/#what-has-been-done-for-version-112>
[41]: <https://github.com/prrvchr/sqlite-jdbc/releases/download/3.45.1.3-SNAPSHOT/sqlite-jdbc-3.45.1.3-SNAPSHOT.jar>
[42]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/XGeneratedResultSet.html>
[43]: <https://github.com/prrvchr/sqlite-jdbc/releases/download/3.45.1.6-SNAPSHOT/sqlite-jdbc-3.45.1.6-SNAPSHOT.jar>
[44]: <https://gerrit.libreoffice.org/c/core/+/154989>
[45]: <https://pypi.org/project/packaging/>
[46]: <https://pypi.org/project/setuptools/>
[47]: <https://github.com/prrvchr/SQLiteOOo/issues/2>
[48]: <https://pypi.org/project/setuptools/>
