# Documentation

**This [document][2] in English.**

**L'utilisation de ce logiciel vous soumet à nos [Conditions d'utilisation][3].**

# version [1.0.0][4]

## Introduction:

**SQLiteOOo** fait partie d'une [Suite][5] d'extensions [LibreOffice][6] et/ou [OpenOffice][7] permettant de vous offrir des services inovants dans ces suites bureautique.  

Cette extension vous permet d'utiliser la base de données SQLite en mode intégré, rendant la base de donnée portable (un seul fichier odb).

Etant un logiciel libre je vous encourage:
- A dupliquer son [code source][8].
- A apporter des modifications, des corrections, des améliorations.
- D'ouvrir un [dysfonctionnement][9] si nécessaire.

Bref, à participer au developpement de cette extension.  
Car c'est ensemble que nous pouvons rendre le Logiciel Libre plus intelligent.

___
## Prérequis:

[SQLite JDBC][10] est une base de données écrite en Java.  
Son utilisation nécessite [l'installation et la configuration][11] dans LibreOffice / OpenOffice d'un **JRE version 11 ou ultérieure**.  
Je vous recommande [Adoptium][12] comme source d'installation de Java.

___
## Installation:

Il semble important que le fichier n'ait pas été renommé lors de son téléchargement.  
Si nécessaire, renommez-le avant de l'installer.

- Installer l'extension ![jdbcDriverOOo logo][13] **[jdbcDriverOOo.oxt][14]** version 1.0.1.  
Cette extension est nécessaire pour utiliser HsqlDB version 2.7.2 avec toutes ses fonctionnalités.

- Installer l'extension ![SQLiteOOo logo][1] **[SQLiteOOo.oxt][15]** version 1.0.0.

Redémarrez LibreOffice / OpenOffice après l'installation.

___
## Utilisation:

### Comment créer une nouvelle base de données:

Dans LibreOffice / OpenOffice aller à: Fichier -> Nouveau -> Base de données...:

![SQLiteOOo screenshot 1][16]

A l'étape: Sélectionner une base de données:
- selectionner: Créer une nouvelle base de données
- Dans: Base de données intégrée: choisir: Pilote SQLite intégré
- cliquer sur le bouton: Suivant

![SQLiteOOo screenshot 2][17]

A l'étape: Enregistrer et continuer:
- ajuster les paramètres selon vos besoins...
- cliquer sur le bouton: Terminer

![SQLiteOOo screenshot 3][18]

Maintenant à vous d'en profiter...

___
## Comment ça marche:

SQLiteOOo est un service [com.sun.star.sdbc.Driver][19] UNO écrit en Python.  
Il s'agit d'une surcouche à l'extension [jdbcDriverOOo][20] permettant de stocker la base de données SQLite dans un fichier odb (qui est, en fait, un fichier compressé).

Son fonctionnement est assez basique, à savoir:

- Lors d'une demande de connexion, trois choses sont faites:
    1. S'il n'existe pas déjà, un **sous-répertoire** avec le nom: `.` + `nom_du_fichier_odb` + `.lck` est créé à l'emplacement du fichier odb dans lequel tous les fichiers SQLite sont extraits du répertoire **database** du fichier odb (décompression).
    2. Un [DocumentHandler][21] est ajouté en tant que [com.sun.star.util.XCloseListener][22] et [com.sun.star.document.XStorageChangeListener][23] au fichier odb.
    3. L'extension [jdbcDriverOOo][20] est utilisée pour obtenir l'interface [com.sun.star.sdbc.XConnection][24] à partir du chemin du **sous-répertoire** + `nom_du_fichier_odb`.

- Lors de la fermeture ou du renommage (Enregistrer sous) d'un fichier odb, le [DocumentHandler][21] copie tous les fichiers présents dans le **sous-répertoire** dans le (nouveau) répertoire **database** du fichier odb (compression) puis supprime le **sous-répertoire**.

___
## A été testé avec:

* OpenOffice 4.1.8 - Ubuntu 20.04 - LxQt 0.14.1

* OpenOffice 4.1.8 - Windows 7 SP1

* LibreOffice 7.0.4.2 - Ubuntu 20.04 - LxQt 0.14.1

* LibreOffice 6.4.4.2 - Windows 7 SP1

Je vous encourage en cas de problème :confused:  
de créer un [dysfonctionnement][9]  
J'essaierai de le résoudre :smile:

___
## Historique:

### Ce qui a été fait pour la version 1.0.0:

- Integration de SQLite JDBC version 3.42.0.0.

### Que reste-t-il à faire pour la version 1.0.0:

- Ajouter de nouvelles langue pour l'internationalisation...

- Tout ce qui est bienvenu...

[1]: <img/SQLiteOOo.svg>
[2]: <https://prrvchr.github.io/SQLiteOOo/>
[3]: <https://prrvchr.github.io/SQLiteOOo/source/SQLiteOOo/registration/TermsOfUse_fr>
[4]: <https://prrvchr.github.io/SQLiteOOo/README_fr#historique>
[5]: <https://prrvchr.github.io/README_fr>
[6]: <https://fr.libreoffice.org/download/telecharger-libreoffice/>
[7]: <https://www.openoffice.org/fr/Telecharger/>
[8]: <https://github.com/prrvchr/SQLiteOOo/>
[9]: <https://github.com/prrvchr/SQLiteOOo/issues/new>
[10]: <https://github.com/xerial/sqlite-jdbc>
[11]: <https://wiki.documentfoundation.org/Documentation/HowTo/Install_the_correct_JRE_-_LibreOffice_on_Windows_10/fr>
[12]: <https://adoptium.net/releases.html?variant=openjdk11>
[13]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.svg>
[14]: <https://github.com/prrvchr/jdbcDriverOOo/raw/master/jdbcDriverOOo.oxt>
[15]: <https://github.com/prrvchr/SQLiteOOo/raw/main/SQLiteOOo.oxt>
[16]: <img/SQLiteOOo-1_fr.png>
[17]: <img/SQLiteOOo-2_fr.png>
[18]: <img/SQLiteOOo-3_fr.png>
[19]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/Driver.html>
[20]: <https://prrvchr.github.io/jdbcDriverOOo/README_fr>
[21]: <https://github.com/prrvchr/SQLiteOOo/blob/main/uno/lib/uno/embedded/documenthandler.py>
[22]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/util/XCloseListener.html>
[23]: <http://www.openoffice.org/api/docs/common/ref/com/sun/star/document/XStorageChangeListener.html>
[24]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/XConnection.html>
