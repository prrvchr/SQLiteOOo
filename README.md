# Documentation

**Ce [document][2] en français.**

**The use of this software subjects you to our [Terms Of Use][3].**

# version [1.0.1][4]

## Introduction:

**SQLiteOOo** is part of a [Suite][5] of [LibreOffice][6] and/or [OpenOffice][7] extensions allowing to offer you innovative services in these office suites.  

This extension allows you to use SQLite database in embedded mode, making the database portable (a single odb file).

Being free software I encourage you:
- To duplicate its [source code][8].
- To make changes, corrections, improvements.
- To open [issue][9] if needed.

In short, to participate in the development of this extension.  
Because it is together that we can make Free Software smarter.

___
## Requirement:

[SQLite JDBC][10] is a database written in Java.  
Its use requires the [installation and configuration][11] in LibreOffice / OpenOffice of a **JRE version 11 or later**.  
I recommend [Adoptium][12] as your Java installation source.

This extension cannot be installed together with the [HsqlDriverOOo][13] extension. It's one or the other, but at the moment they can't work together.

___
## Installation:

It seems important that the file was not renamed when it was downloaded.
If necessary, rename it before installing it.

- Install ![jdbcDriverOOo logo][14] **[jdbcDriverOOo.oxt][15]** extension version 1.0.1.  
This extension is necessary to use SQLite version 3.42.0.0 with all its features.

- Install ![SQLiteOOo logo][1] **[SQLiteOOo.oxt][16]** extension version 1.0.1.

Restart LibreOffice / OpenOffice after installation.

___
## Use:

### How to create a new database:

In LibreOffice / OpenOffice go to File -> New -> Database...:

![SQLiteOOo screenshot 1][17]

In step: Select database:
- select: Create a new database
- in: Emdedded database: choose: Embedded SQLite Driver
- click on button: Next

![SQLiteOOo screenshot 2][18]

In step: Save and proceed:
- adjust the parameters according to your needs...
- click on button: Finish

![SQLiteOOo screenshot 3][19]

Have fun...

___
## How does it work:

SQLiteOOo is an [com.sun.star.sdbc.Driver][20] UNO service written in Python.  
It is an overlay to the [jdbcDriverOOo][21] extension allowing to store the SQLite database in an odb file (which is, in fact, a compressed file).

Its operation is quite basic, namely:

- When requesting a connection, three things are done:
    1. If it does not already exist, a **subdirectory** with name: `.` + `odb_file_name` + `.lck` is created in the location of the odb file where all SQLite files are extracted from the **database** directory of the odb file (unzip).
    2. A [DocumentHandler][22] is added as an [com.sun.star.util.XCloseListener][23] and [com.sun.star.document.XStorageChangeListener][24] to the odb file.
    3. The [jdbcDriverOOo][21] extension is used to get the [com.sun.star.sdbc.XConnection][25] interface from the **subdirectory** path + `odb_file_name`.

- When closing or renaming (Save as) an odb file the [DocumentHandler][22] copy all the files present in the **subdirectory** into the (new) **database** directory of the odb file (zip) and then delete the **subdirectory**.

___
## Has been tested with:

* OpenOffice 4.1.8 - Ubuntu 20.04 - LxQt 0.14.1

* OpenOffice 4.1.8 - Windows 7 SP1

* LibreOffice 7.0.4.2 - Ubuntu 20.04 - LxQt 0.14.1

* LibreOffice 6.4.4.2 - Windows 7 SP1

* LibreOffice 7.6.0.1 - Windows 10

* LibreOffice 7.6.0.1 - Ubuntu 22.04

I encourage you in case of problem :confused:  
to create an [issue][9]  
I will try to solve it :smile:

___
## Historical:

### What has been done for version 1.0.0:

- Integration of SQLite JDBC version 3.42.0.0. I especially want to thank [gotson][26] for the [many improvements to the SQLite JDBC driver][27] that made it possible to use SQLite in LibreOffice/OpenOffice.

### What has been done for version 1.0.1:

- Fixed [bug 156511][28] occurring when using the com.sun.star.embed.XStorage interface. The workaround is to use the copyElementTo() method instead of moveElementTo().

### What remains to be done for version 1.0.1:

- Add new language for internationalization...

- Anything welcome...

[1]: <img/SQLiteOOo.svg>
[2]: <https://prrvchr.github.io/SQLiteOOo/README_fr>
[3]: <https://prrvchr.github.io/SQLiteOOo/source/SQLiteOOo/registration/TermsOfUse_en>
[4]: <https://prrvchr.github.io/SQLiteOOo#historical>
[5]: <https://prrvchr.github.io/>
[6]: <https://www.libreoffice.org/download/download/>
[7]: <https://www.openoffice.org/download/index.html>
[8]: <https://github.com/prrvchr/SQLiteOOo/>
[9]: <https://github.com/prrvchr/SQLiteOOo/issues/new>
[10]: <https://github.com/xerial/sqlite-jdbc>
[11]: <https://wiki.documentfoundation.org/Documentation/HowTo/Install_the_correct_JRE_-_LibreOffice_on_Windows_10>
[12]: <https://adoptium.net/releases.html?variant=openjdk11>
[13]: <https://prrvchr.github.io/HsqlDriverOOo/>
[14]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.svg>
[15]: <https://github.com/prrvchr/jdbcDriverOOo/raw/master/jdbcDriverOOo.oxt>
[16]: <https://github.com/prrvchr/SQLiteOOo/raw/main/SQLiteOOo.oxt>
[17]: <img/SQLiteOOo-1.png>
[18]: <img/SQLiteOOo-2.png>
[19]: <img/SQLiteOOo-3.png>
[20]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/Driver.html>
[21]: <https://prrvchr.github.io/jdbcDriverOOo>
[22]: <https://github.com/prrvchr/SQLiteOOo/blob/main/uno/lib/uno/embedded/documenthandler.py>
[23]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/util/XCloseListener.html>
[24]: <http://www.openoffice.org/api/docs/common/ref/com/sun/star/document/XStorageChangeListener.html>
[25]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/XConnection.html>
[26]: <https://github.com/gotson>
[27]: <https://github.com/xerial/sqlite-jdbc/issues/786>
[28]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156511>
