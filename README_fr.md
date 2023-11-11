# Documentation

**This [document][1] in English.**

**L'utilisation de ce logiciel vous soumet à nos [Conditions d'utilisation][2].**

# version [1.0.2][3]

## Introduction:

**SQLiteOOo** fait partie d'une [Suite][4] d'extensions [LibreOffice][5] et/ou [OpenOffice][6] permettant de vous offrir des services inovants dans ces suites bureautique.  

Cette extension vous permet d'utiliser la base de données SQLite en mode intégré, rendant la base de donnée portable (un seul fichier odb).

Etant un logiciel libre je vous encourage:
- A dupliquer son [code source][7].
- A apporter des modifications, des corrections, des améliorations.
- D'ouvrir un [dysfonctionnement][8] si nécessaire.

Bref, à participer au developpement de cette extension.  
Car c'est ensemble que nous pouvons rendre le Logiciel Libre plus intelligent.

___

## Prérequis:

[SQLite JDBC][9] est une base de données écrite en Java.  
Son utilisation nécessite [l'installation et la configuration][10] dans LibreOffice / OpenOffice d'un **JRE version 11 ou ultérieure**.  
Je vous recommande [Adoptium][11] comme source d'installation de Java.

Cette extension ne peut pas être installée avec l'extension [HyperSQLOOo][12]. C'est l'une ou l'autre, mais pour le moment, elles ne peuvent pas fonctionner ensemble.

Si vous utilisez **LibreOffice sous Linux**, alors vous êtes sujet au [dysfonctionnement 139538][13]. Pour contourner le problème, veuillez **désinstaller les paquets** avec les commandes:
- `sudo apt remove libreoffice-sdbc-hsqldb` (pour désinstaller le paquet libreoffice-sdbc-hsqldb)
- `sudo apt remove libhsqldb1.8.0-java` (pour désinstaller le paquet libhsqldb1.8.0-java)

OpenOffice et LibreOffice sous Windows ne sont pas soumis à ce dysfonctionnement.

___

## Installation:

Il semble important que le fichier n'ait pas été renommé lors de son téléchargement.  
Si nécessaire, renommez-le avant de l'installer.

- [![jdbcDriverOOo logo][14]][15] Installer l'extension **[jdbcDriverOOo.oxt][16]** [![Version][17]][16]

    Cette extension est nécessaire pour utiliser SQLite version 3.42.0.0 avec toutes ses fonctionnalités.

- ![SQLiteOOo logo][18] Installer l'extension **[SQLiteOOo.oxt][19]** [![Version][20]][19]

Redémarrez LibreOffice / OpenOffice après l'installation.

___

## Utilisation:

### Comment créer une nouvelle base de données:

Dans LibreOffice / OpenOffice aller à: Fichier -> Nouveau -> Base de données...:

![SQLiteOOo screenshot 1][21]

A l'étape: Sélectionner une base de données:
- selectionner: Créer une nouvelle base de données
- Dans: Base de données intégrée: choisir: Pilote SQLite intégré
- cliquer sur le bouton: Suivant

![SQLiteOOo screenshot 2][22]

A l'étape: Enregistrer et continuer:
- ajuster les paramètres selon vos besoins...
- cliquer sur le bouton: Terminer

![SQLiteOOo screenshot 3][23]

Maintenant à vous d'en profiter...

___

## Comment ça marche:

SQLiteOOo est un service [com.sun.star.sdbc.Driver][24] UNO écrit en Python.  
Il s'agit d'une surcouche à l'extension [jdbcDriverOOo][15] permettant de stocker la base de données SQLite dans un fichier odb (qui est, en fait, un fichier compressé).

Son fonctionnement est assez basique, à savoir:

- Lors d'une demande de connexion, trois choses sont faites:
    1. S'il n'existe pas déjà, un **sous-répertoire** avec le nom: `.` + `nom_du_fichier_odb` + `.lck` est créé à l'emplacement du fichier odb dans lequel tous les fichiers SQLite sont extraits du répertoire **database** du fichier odb (décompression).
    2. Un [DocumentHandler][25] est ajouté en tant que [com.sun.star.util.XCloseListener][26] et [com.sun.star.document.XStorageChangeListener][27] au fichier odb.
    3. L'extension [jdbcDriverOOo][15] est utilisée pour obtenir l'interface [com.sun.star.sdbc.XConnection][28] à partir du chemin du **sous-répertoire** + `nom_du_fichier_odb`.

- Lors de la fermeture ou du renommage (Enregistrer sous) d'un fichier odb, le [DocumentHandler][25] copie tous les fichiers présents dans le **sous-répertoire** dans le (nouveau) répertoire **database** du fichier odb (compression) puis supprime le **sous-répertoire**.

___

## A été testé avec:

* OpenOffice 4.1.8 - Ubuntu 20.04 - LxQt 0.14.1

* OpenOffice 4.1.8 - Windows 7 SP1

* LibreOffice 7.0.4.2 - Ubuntu 20.04 - LxQt 0.14.1

* LibreOffice 6.4.4.2 - Windows 7 SP1

* LibreOffice 7.6.0.1 - Windows 10

* LibreOffice 7.6.0.1 - Ubuntu 22.04

Je vous encourage en cas de problème :confused:  
de créer un [dysfonctionnement][8]  
J'essaierai de le résoudre :smile:

___

## Historique:

### Ce qui a été fait pour la version 1.0.0:

- Intégration de SQLite JDBC version 3.42.0.0. Je tiens tout particulièrement à remercier [gotson][29] pour les [nombreuses améliorations apportées au pilote SQLite JDBC][30] qui ont rendu possible l'utilisation de SQLite dans LibreOffice/OpenOffice.

### Ce qui a été fait pour la version 1.0.1:

- Résolution du [dysfonctionnement 156511][31] survenant lors de l'utilisation de l'interface com.sun.star.embed.XStorage. Le [contournement][32] consiste à utiliser la méthode copyElementTo() au lieu de moveElementTo(). Les versions de LibreOffice 7.6.x et supérieures deviennent utilisables.

### Ce qui a été fait pour la version 1.0.2:

- L'absence ou l'obsolescence de l'extension **jdbcDriverOOo** nécessaires au bon fonctionnement de **SQLiteOOo** affiche désormais un message d'erreur.

- Encore plein d'autres choses...

### Que reste-t-il à faire pour la version 1.0.2:

- Ajouter de nouvelles langue pour l'internationalisation...

- Tout ce qui est bienvenu...

[1]: <https://prrvchr.github.io/SQLiteOOo/>
[2]: <https://prrvchr.github.io/SQLiteOOo/source/SQLiteOOo/registration/TermsOfUse_fr>
[3]: <https://prrvchr.github.io/SQLiteOOo/README_fr#historique>
[4]: <https://prrvchr.github.io/README_fr>
[5]: <https://fr.libreoffice.org/download/telecharger-libreoffice/>
[6]: <https://www.openoffice.org/fr/Telecharger/>
[7]: <https://github.com/prrvchr/SQLiteOOo/>
[8]: <https://github.com/prrvchr/SQLiteOOo/issues/new>
[9]: <https://github.com/xerial/sqlite-jdbc>
[10]: <https://wiki.documentfoundation.org/Documentation/HowTo/Install_the_correct_JRE_-_LibreOffice_on_Windows_10/fr>
[11]: <https://adoptium.net/releases.html?variant=openjdk11>
[12]: <https://prrvchr.github.io/HyperSQLOOo/README_fr#prérequis>
[13]: <https://bugs.documentfoundation.org/show_bug.cgi?id=139538>
[14]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.svg#middle>
[15]: <https://prrvchr.github.io/jdbcDriverOOo/README_fr>
[16]: <https://github.com/prrvchr/jdbcDriverOOo/releases/latest/download/jdbcDriverOOo.oxt>
[17]: <https://img.shields.io/github/v/tag/prrvchr/jdbcDriverOOo?label=latest#right>
[18]: <img/SQLiteOOo.svg#middle>
[19]: <https://github.com/prrvchr/SQLiteOOo/releases/latest/download/SQLiteOOo.oxt>
[20]: <https://img.shields.io/github/downloads/prrvchr/SQLiteOOo/latest/total?label=v1.0.2#right>
[21]: <img/SQLiteOOo-1_fr.png>
[22]: <img/SQLiteOOo-2_fr.png>
[23]: <img/SQLiteOOo-3_fr.png>
[24]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/Driver.html>
[25]: <https://github.com/prrvchr/SQLiteOOo/blob/main/uno/lib/uno/embedded/documenthandler.py>
[26]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/util/XCloseListener.html>
[27]: <http://www.openoffice.org/api/docs/common/ref/com/sun/star/document/XStorageChangeListener.html>
[28]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/XConnection.html>
[29]: <https://github.com/gotson>
[30]: <https://github.com/xerial/sqlite-jdbc/issues/786>
[31]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156511>
[32]: <https://github.com/prrvchr/uno/commit/a2fa9f5975a35e8447907e51b0f78ac1b1b76e17>
