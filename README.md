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

# version [1.4.0][5]

## Introduction:

**SQLiteOOo** is part of a [Suite][6] of [LibreOffice][7] ~~and/or [OpenOffice][8]~~ extensions allowing to offer you innovative services in these office suites.  

This extension allows you to use [SQLite JDBC][9] database in embedded mode, making the database portable (a single odb file).  
It allows you to take advantage of the [ACID][10] properties of the underlying [SQLite][11] database.

Being free software I encourage you:
- To duplicate its [source code][12].
- To make changes, corrections, improvements.
- To open [issue][13] if needed.
- To [participate in the costs][14] of [CASA certification][15].

In short, to participate in the development of this extension.  
Because it is together that we can make Free Software smarter.

___

## Requirement:

The SQLiteOOo extension uses the jdbcDriverOOo extension to work.  
It must therefore meet the [requirement of the jdbcDriverOOo extension][16].

Additionally, due to [issue #156471][17] and following [PR#154989][18], the SQLiteOOo extension requires **LibreOffice version 24.2.x** minimum to work.

___

## Installation:

It seems important that the file was not renamed when it was downloaded.  
If necessary, rename it before installing it.

- [![jdbcDriverOOo logo][20]][21] Install **[jdbcDriverOOo.oxt][22]** extension [![Version][23]][22]

    This extension is required to use the latest version of SQLite with all its features.

- ![SQLiteOOo logo][24] Install **[SQLiteOOo.oxt][25]** extension [![Version][26]][25]

Restart LibreOffice after installation.  
**Be careful, restarting LibreOffice may not be enough.**
- **On Windows** to ensure that LibreOffice restarts correctly, use Windows Task Manager to verify that no LibreOffice services are visible after LibreOffice shuts down (and kill it if so).
- **Under Linux or macOS** you can also ensure that LibreOffice restarts correctly, by launching it from a terminal with the command `soffice` and using the key combination `Ctrl + C` if after stopping LibreOffice, the terminal is not active (no command prompt).

After restarting LibreOffice, you can ensure that the extension and its driver are correctly installed by checking that the `io.github.prrvchr.SQLiteOOo.Driver` driver is listed in the **Connection Pool**, accessible via the menu: **Tools -> Options -> LibreOffice Base -> Connections**. It is not necessary to enable the connection pool.

If the driver is not listed, the reason for the driver failure can be found in the extension's logging. This log is accessible via the menu: **Tools -> Options -> LibreOffice Base -> Embedded SQLite Driver -> Logging Options**.  
The `SQLiteLogger` logging must first be enabled and then LibreOffice restarted to get the error message in the log.

Remember to first update the version of the Java JRE or JDK installed on your computer, this extension need the new version of jdbcDriverOOo that requires **Java version 17 or later** instead of Java 11 previously.

___

## Use:

### How to create a new database:

In LibreOffice / OpenOffice go to File -> New -> Database...:

![SQLiteOOo screenshot 1][27]

In step: Select database:
- select: Create a new database
- in: Emdedded database: choose: Embedded SQLite Driver
- click on button: Next

![SQLiteOOo screenshot 2][28]

In step: Save and proceed:
- adjust the parameters according to your needs...
- click on button: Finish

![SQLiteOOo screenshot 3][29]

Have fun...

___

## How does it work:

SQLiteOOo is an [com.sun.star.sdbc.Driver][30] UNO service written in Python.  
It is an overlay to the [jdbcDriverOOo][21] extension allowing to store the SQLite database in an odb file (which is, in fact, a compressed file).

Its operation is quite basic, namely:

- When requesting a connection, several things are done:
  - If it does not already exist, a **subdirectory** with name: `.` + `odb_file_name` + `.lck` is created in the location of the odb file where all SQLite files are extracted from the **database** directory of the odb file (unzip).
  - The [jdbcDriverOOo][21] extension is used to get the [com.sun.star.sdbc.XConnection][31] interface from the **subdirectory** path + `/sqlite`.
  - If the connection is successful, a [DocumentHandler][32] is added as an [com.sun.star.util.XCloseListener][33] and [com.sun.star.document.XStorageChangeListener][34] to the odb file.
  - If the connection is unsuccessful and the files was extracted in phase 1, the **subdirectory** will be deleted.
- When closing or renaming (Save As) the odb file, if the connection was successful, the [DocumentHandler][32] copies all files present in the **subdirectory** into the (new) **database** directory of the odb file (zip), then delete the **subdirectory**.

The main purpose of this mode of operation is to take advantage of the ACID characteristics of the underlying database in the event of an abnormal closure of LibreOffice.
On the other hand, the function: **file -> Save** has **no effect on the underlying database**. Only closing the odb file or saving it under a different name (File -> Save As) will save the database in the odb file.

___

## How to build the extension:

Normally, the extension is created with Eclipse for Java and [LOEclipse][35]. To work around Eclipse, I modified LOEclipse to allow the extension to be created with Apache Ant.  
To create the SQLiteOOo extension with the help of Apache Ant, you need to:
- Install the [Java SDK][36] version 8 or higher.
- Install [Apache Ant][37] version 1.10.0 or higher.
- Install [LibreOffice and its SDK][38] version 7.x or higher.
- Clone the [SQLiteOOo][39] repository on GitHub into a folder.
- From this folder, move to the directory: `source/SQLiteOOo/`
- In this directory, edit the file: `build.properties` so that the `office.install.dir` and `sdk.dir` properties point to the folders where LibreOffice and its SDK were installed, respectively.
- Start the archive creation process using the command: `ant`
- You will find the generated archive in the subfolder: `dist/`

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

- Integration of SQLite JDBC version 3.42.0.0. I especially want to thank [gotson][40] for the [many improvements to the SQLite JDBC driver][41] that made it possible to use SQLite in LibreOffice/OpenOffice.

### What has been done for version 1.0.1:

- Fixed [bug 156511][42] occurring when using the com.sun.star.embed.XStorage interface. The [workaround][43] is to use the copyElementTo() method instead of moveElementTo(). Versions of LibreOffice 7.6.x and higher become usable.

### What has been done for version 1.0.2:

- The absence or obsolescence of **jdbcDriverOOo** extension necessary for the proper functioning of **SQLiteOOo** now displays an error message.

- Many other things...

### What has been done for version 1.1.0:

- All Python packages necessary for the extension are now recorded in a [requirements.txt][44] file following [PEP 508][45].
- Now if you are not on Windows then the Python packages necessary for the extension can be easily installed with the command:  
  `pip install requirements.txt`
- Modification of the [Requirement][46] section.

### What has been done for version 1.1.1:

- Support for [new features][47] in **jdbcDriverOOo 1.1.2**.

### What has been done for version 1.1.2:

- SQLite driver updated to latest version [SQLite-jdbc-3.45.1.3-SNAPSHOT.jar][48]. This new driver has been implemented to support part of the JDBC 4.1 specifications and more particularly the `java.sql.Statement.getGeneratedKeys()` interface and allows the use of the [com.sun.star.sdbc.XGeneratedResultSet][49] interface.

### What has been done for version 1.1.3:

- Support for the latest version of **jdbcDriverOOo 1.1.4** and the [SQLite-jdbc-3.45.1.6-SNAPSHOT.jar][50].
- Now for proper functioning in Base under: **Edit -> Database -> Advanced Settings... -> Query of generated values** must be left blank. If you want to use an odb file created with a previous version of SQLiteOOo you must change this setting manually.
- Normally the next versions of SQLiteOOo should be able to be updated in the list of extensions installed under LibreOffice: **Tools -> Extension manager... -> Check for Updates**.

### What has been done for version 1.1.4:

- Support for the latest version of **jdbcDriverOOo 1.3.1**.
- When saving under a different name, the database if open will be closed correctly.

### What has been done for version 1.1.5:

- Use of the new data format implemented in version 1.1.4. As a result, if you need to open odb files created with a version lower than 1.1.4 you must first open them with version 1.1.4, otherwise an error will be thrown.

### What has been done for version 1.2.0:

- This version is based on [fix #154989][51] available since LibreOffice 24.2.x. It can therefore work with other extensions offering integrated database services.
- Now SQLiteOOo requires LibreOffice 24.2.x minimum and will load for the url: `sdbc:embedded:sqlite`.

### What has been done for version 1.2.1:

- Updated the [Python packaging][52] package to version 24.1.
- Updated the [Python setuptools][53] package to version 72.1.0.
- The extension will ask you to install the jdbcDriverOOo extension in versions 1.4.2 minimum.

### What has been done for version 1.2.2:

- Fixed [issue #2][54] which appears to be a regression related to the release of JaybirdOOo. Thanks to madalienist for reporting it.
- Updated the [Python setuptools][53] package to version 73.0.1.
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

- Updated the [Python packaging][52] package to version 25.0.
- Updated the [Python setuptools][53] package to version 75.3.2.
- Passive registration deployment that allows for much faster installation of extensions and differentiation of registered UNO services from those provided by a Java or Python implementation. This passive registration is provided by the [LOEclipse][35] extension via [PR#152][55] and [PR#157][56].
- Modified [LOEclipse][35] to support the new `rdb` file format produced by the `unoidl-write` compilation utility. `idl` files have been updated to support both available compilation tools: idlc and unoidl-write.
- Implemented [PEP 570][57] in [logging][58] to support unique multiple arguments.
- It is now possible to build the oxt file of the SQLiteOOo extension only with the help of Apache Ant and a copy of the GitHub repository. The [How to build the extension][59] section has been added to the documentation.
- Any errors occurring while loading the driver will be logged in the extension's log if logging has been previously enabled. This makes it easier to identify installation problems on Windows.
- Requires the **jdbcDriverOOo extension at least version 1.5.0**.

### What has been done for version 1.3.1:

- Many fixes that prevented proper functioning have been made to the driver written in Python and wrapping the driver that jdbcDriverOOo provides.
- Requires the **jdbcDriverOOo extension at least version 1.5.1**.

### What has been done for version 1.3.2:

- Requires the **jdbcDriverOOo extension at least version 1.5.4**.

### What has been done for version 1.3.3:

- Requires the **jdbcDriverOOo extension at least version 1.5.7**.

### What has been done for version 1.4.0:

- If the jdbcDriverOOo extension works without Java instrumentation, a warning message will be displayed in the extension options.
- Requires the **jdbcDriverOOo extension at least version 1.6.1**.
- Has been tested under LibreOfficeDev 26.2.

### What remains to be done for version 1.4.0:

- Add new language for internationalization...

- Anything welcome...

[1]: </img/sqlite.svg#collapse>
[2]: <https://prrvchr.github.io/SQLiteOOo/>
[3]: <https://prrvchr.github.io/SQLiteOOo/README_fr>
[4]: <https://prrvchr.github.io/SQLiteOOo/source/SQLiteOOo/registration/TermsOfUse_en>
[5]: <https://prrvchr.github.io/SQLiteOOo#what-has-been-done-for-version-140>
[6]: <https://prrvchr.github.io/>
[7]: <https://www.libreoffice.org/download/download/>
[8]: <https://www.openoffice.org/download/index.html>
[9]: <https://github.com/xerial/sqlite-jdbc>
[10]: <https://en.wikipedia.org/wiki/ACID>
[11]: <https://www.sqlite.org/transactional.html>
[12]: <https://github.com/prrvchr/SQLiteOOo/>
[13]: <https://github.com/prrvchr/SQLiteOOo/issues/new>
[14]: <https://github.com/sponsors/prrvchr>
[15]: <https://appdefensealliance.dev/casa>
[16]: <https://prrvchr.github.io/jdbcDriverOOo/#requirement>
[17]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156471>
[18]: <https://gerrit.libreoffice.org/c/core/+/154989>
[20]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.svg#middle>
[21]: <https://prrvchr.github.io/jdbcDriverOOo>
[22]: <https://github.com/prrvchr/jdbcDriverOOo/releases/latest/download/jdbcDriverOOo.oxt>
[23]: <https://img.shields.io/github/v/tag/prrvchr/jdbcDriverOOo?label=latest#right>
[24]: <img/SQLiteOOo.svg#middle>
[25]: <https://github.com/prrvchr/SQLiteOOo/releases/latest/download/SQLiteOOo.oxt>
[26]: <https://img.shields.io/github/downloads/prrvchr/SQLiteOOo/latest/total?label=v1.4.0#right>
[27]: <img/SQLiteOOo-1.png>
[28]: <img/SQLiteOOo-2.png>
[29]: <img/SQLiteOOo-3.png>
[30]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/Driver.html>
[31]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/XConnection.html>
[32]: <https://github.com/prrvchr/SQLiteOOo/blob/main/uno/lib/uno/embedded/documenthandler.py>
[33]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/util/XCloseListener.html>
[34]: <http://www.openoffice.org/api/docs/common/ref/com/sun/star/document/XStorageChangeListener.html>
[35]: <https://github.com/LibreOffice/loeclipse>
[36]: <https://adoptium.net/temurin/releases/?version=8&package=jdk>
[37]: <https://ant.apache.org/manual/install.html>
[38]: <https://downloadarchive.documentfoundation.org/libreoffice/old/7.6.7.2/>
[39]: <https://github.com/prrvchr/SQLiteOOo.git>
[40]: <https://github.com/gotson>
[41]: <https://github.com/xerial/sqlite-jdbc/issues/786>
[42]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156511>
[43]: <https://github.com/prrvchr/uno/commit/a2fa9f5975a35e8447907e51b0f78ac1b1b76e17>
[44]: <https://github.com/prrvchr/SQLiteOOo/releases/latest/download/requirements.txt>
[45]: <https://peps.python.org/pep-0508/>
[46]: <https://prrvchr.github.io/SQLiteOOo/#requirement>
[47]: <https://prrvchr.github.io/jdbcDriverOOo/#what-has-been-done-for-version-112>
[48]: <https://github.com/prrvchr/sqlite-jdbc/releases/download/3.45.1.3-SNAPSHOT/sqlite-jdbc-3.45.1.3-SNAPSHOT.jar>
[49]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/XGeneratedResultSet.html>
[50]: <https://github.com/prrvchr/sqlite-jdbc/releases/download/3.45.1.6-SNAPSHOT/sqlite-jdbc-3.45.1.6-SNAPSHOT.jar>
[51]: <https://gerrit.libreoffice.org/c/core/+/154989>
[52]: <https://pypi.org/project/packaging/>
[53]: <https://pypi.org/project/setuptools/>
[54]: <https://github.com/prrvchr/SQLiteOOo/issues/2>
[55]: <https://github.com/LibreOffice/loeclipse/pull/152>
[56]: <https://github.com/LibreOffice/loeclipse/pull/157>
[57]: <https://peps.python.org/pep-0570/>
[58]: <https://github.com/prrvchr/SQLiteOOo/blob/main/uno/lib/uno/logger/logwrapper.py#L109>
[59]: <https://prrvchr.github.io/SQLiteOOo/README_fr#comment-cr%C3%A9er-lextension>
