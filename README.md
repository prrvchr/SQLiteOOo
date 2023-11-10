# Documentation

**Ce [document][1] en français.**

**The use of this software subjects you to our [Terms Of Use][2].**

# version [1.0.2][3]

## Introduction:

**SQLiteOOo** is part of a [Suite][4] of [LibreOffice][5] and/or [OpenOffice][6] extensions allowing to offer you innovative services in these office suites.  

This extension allows you to use SQLite database in embedded mode, making the database portable (a single odb file).

Being free software I encourage you:
- To duplicate its [source code][7].
- To make changes, corrections, improvements.
- To open [issue][8] if needed.

In short, to participate in the development of this extension.  
Because it is together that we can make Free Software smarter.

___

## Requirement:

[SQLite JDBC][9] is a database written in Java.  
Its use requires the [installation and configuration][10] in LibreOffice / OpenOffice of a **JRE version 11 or later**.  
I recommend [Adoptium][11] as your Java installation source.

This extension cannot be installed together with the [HyperSQLOOo][12] extension. It's one or the other, but at the moment they can't work together.

___

## Installation:

It seems important that the file was not renamed when it was downloaded.
If necessary, rename it before installing it.

- Install ![jdbcDriverOOo logo][13] **[jdbcDriverOOo.oxt][14]** extension [![Version][15]][14]
    This extension is necessary to use SQLite version 3.42.0.0 with all its features.

- Install ![SQLiteOOo logo][16] **[SQLiteOOo.oxt][17]** extension [![Version][18]][17]

Restart LibreOffice / OpenOffice after installation.

___

## Use:

### How to create a new database:

In LibreOffice / OpenOffice go to File -> New -> Database...:

![SQLiteOOo screenshot 1][19]

In step: Select database:
- select: Create a new database
- in: Emdedded database: choose: Embedded SQLite Driver
- click on button: Next

![SQLiteOOo screenshot 2][20]

In step: Save and proceed:
- adjust the parameters according to your needs...
- click on button: Finish

![SQLiteOOo screenshot 3][21]

Have fun...

___

## How does it work:

SQLiteOOo is an [com.sun.star.sdbc.Driver][22] UNO service written in Python.  
It is an overlay to the [jdbcDriverOOo][23] extension allowing to store the SQLite database in an odb file (which is, in fact, a compressed file).

Its operation is quite basic, namely:

- When requesting a connection, three things are done:
    1. If it does not already exist, a **subdirectory** with name: `.` + `odb_file_name` + `.lck` is created in the location of the odb file where all SQLite files are extracted from the **database** directory of the odb file (unzip).
    2. A [DocumentHandler][24] is added as an [com.sun.star.util.XCloseListener][25] and [com.sun.star.document.XStorageChangeListener][26] to the odb file.
    3. The [jdbcDriverOOo][23] extension is used to get the [com.sun.star.sdbc.XConnection][27] interface from the **subdirectory** path + `odb_file_name`.

- When closing or renaming (Save as) an odb file the [DocumentHandler][24] copy all the files present in the **subdirectory** into the (new) **database** directory of the odb file (zip) and then delete the **subdirectory**.

___

## Has been tested with:

* OpenOffice 4.1.8 - Ubuntu 20.04 - LxQt 0.14.1

* OpenOffice 4.1.8 - Windows 7 SP1

* LibreOffice 7.0.4.2 - Ubuntu 20.04 - LxQt 0.14.1

* LibreOffice 6.4.4.2 - Windows 7 SP1

* LibreOffice 7.6.0.1 - Windows 10

* LibreOffice 7.6.0.1 - Ubuntu 22.04

I encourage you in case of problem :confused:  
to create an [issue][8]  
I will try to solve it :smile:

___

## Historical:

### What has been done for version 1.0.0:

- Integration of SQLite JDBC version 3.42.0.0. I especially want to thank [gotson][28] for the [many improvements to the SQLite JDBC driver][29] that made it possible to use SQLite in LibreOffice/OpenOffice.

### What has been done for version 1.0.1:

- Fixed [bug 156511][30] occurring when using the com.sun.star.embed.XStorage interface. The [workaround][31] is to use the copyElementTo() method instead of moveElementTo(). Versions of LibreOffice 7.6.x and higher become usable.

### What has been done for version 1.0.2:

- The absence or obsolescence of **jdbcDriverOOo** extension necessary for the proper functioning of **SQLiteOOo** now displays an error message.

- Many other things...

### What remains to be done for version 1.0.2:

- Add new language for internationalization...

- Anything welcome...

[1]: <https://prrvchr.github.io/SQLiteOOo/README_fr>
[2]: <https://prrvchr.github.io/SQLiteOOo/source/SQLiteOOo/registration/TermsOfUse_en>
[3]: <https://prrvchr.github.io/SQLiteOOo#historical>
[4]: <https://prrvchr.github.io/>
[5]: <https://www.libreoffice.org/download/download/>
[6]: <https://www.openoffice.org/download/index.html>
[7]: <https://github.com/prrvchr/SQLiteOOo/>
[8]: <https://github.com/prrvchr/SQLiteOOo/issues/new>
[9]: <https://github.com/xerial/sqlite-jdbc>
[10]: <https://wiki.documentfoundation.org/Documentation/HowTo/Install_the_correct_JRE_-_LibreOffice_on_Windows_10>
[11]: <https://adoptium.net/releases.html?variant=openjdk11>
[12]: <https://prrvchr.github.io/HyperSQLOOo/>
[13]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.svg#middle>
[14]: <https://github.com/prrvchr/jdbcDriverOOo/releases/latest/download/jdbcDriverOOo.oxt>
[15]: <https://img.shields.io/github/downloads/prrvchr/jdbcDriverOOo/latest/total?label=v1.0.5#right>
[16]: <img/SQLiteOOo.svg#middle>
[17]: <https://github.com/prrvchr/SQLiteOOo/releases/latest/download/SQLiteOOo.oxt>
[18]: <https://img.shields.io/github/downloads/prrvchr/SQLiteOOo/latest/total?label=v1.0.2#right>
[19]: <img/SQLiteOOo-1.png>
[20]: <img/SQLiteOOo-2.png>
[21]: <img/SQLiteOOo-3.png>
[22]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/Driver.html>
[23]: <https://prrvchr.github.io/jdbcDriverOOo>
[24]: <https://github.com/prrvchr/SQLiteOOo/blob/main/uno/lib/uno/embedded/documenthandler.py>
[25]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/util/XCloseListener.html>
[26]: <http://www.openoffice.org/api/docs/common/ref/com/sun/star/document/XStorageChangeListener.html>
[27]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/XConnection.html>
[28]: <https://github.com/gotson>
[29]: <https://github.com/xerial/sqlite-jdbc/issues/786>
[30]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156511>
[31]: <https://github.com/prrvchr/uno/commit/a2fa9f5975a35e8447907e51b0f78ac1b1b76e17>
