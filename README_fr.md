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

**This [document][3] in English.**

**L'utilisation de ce logiciel vous soumet à nos [Conditions d'utilisation][4].**

# version [1.1.4][5]

## Introduction:

**SQLiteOOo** fait partie d'une [Suite][6] d'extensions [LibreOffice][7] ~~et/ou [OpenOffice][8]~~ permettant de vous offrir des services inovants dans ces suites bureautique.  

Cette extension vous permet d'utiliser la base de données [SQLite JDBC][9] en mode intégré, rendant la base de donnée portable (un seul fichier odb).  
Elle permet de profiter des propriétés [ACID][10] de la base de données [SQLite][11] sous jancente.

Etant un logiciel libre je vous encourage:
- A dupliquer son [code source][12].
- A apporter des modifications, des corrections, des améliorations.
- D'ouvrir un [dysfonctionnement][13] si nécessaire.

Bref, à participer au developpement de cette extension.  
Car c'est ensemble que nous pouvons rendre le Logiciel Libre plus intelligent.

___

## Prérequis:

L'extension SQLiteOOo utilise l'extension jdbcDriverOOo pour fonctionner.  
Elle doit donc répondre aux [prérequis de l'extension jdbcDriverOOo][14].

Cette extension ne peut pas être installée avec l'extension [HyperSQLOOo][15].  
C'est l'une ou l'autre, mais pour le moment, elles ne peuvent pas fonctionner ensemble (voir [dysfonctionnement #156471][16]).

**Sous Linux et macOS les paquets Python** utilisés par l'extension, peuvent s'il sont déja installé provenir du système et donc, **peuvent ne pas être à jour**.  
Afin de s'assurer que vos paquets Python sont à jour il est recommandé d'utiliser l'option **Info système** dans les Options de l'extension accessible par:  
**Outils -> Options -> Pilotes Base -> Pilote SQLite intégré -> Voir journal -> Info système**  
Si des paquets obsolètes apparaissent, vous pouvez les mettre à jour avec la commande:  
`pip install --upgrade <package-name>`

Pour plus d'information voir: [Ce qui a été fait pour la version 1.1.0][17].

___

## Installation:

Il semble important que le fichier n'ait pas été renommé lors de son téléchargement.  
Si nécessaire, renommez-le avant de l'installer.

- [![jdbcDriverOOo logo][18]][19] Installer l'extension **[jdbcDriverOOo.oxt][20]** [![Version][21]][20]

    Cette extension est nécessaire pour utiliser SQLite version 3.42.0.0 avec toutes ses fonctionnalités.

- ![SQLiteOOo logo][22] Installer l'extension **[SQLiteOOo.oxt][23]** [![Version][24]][23]

Redémarrez LibreOffice après l'installation.  
**Attention, redémarrer LibreOffice peut ne pas suffire.**
- **Sous Windows** pour vous assurer que LibreOffice redémarre correctement, utilisez le Gestionnaire de tâche de Windows pour vérifier qu'aucun service LibreOffice n'est visible après l'arrêt de LibreOffice (et tuez-le si ç'est le cas).
- **Sous Linux ou macOS** vous pouvez également vous assurer que LibreOffice redémarre correctement, en le lançant depuis un terminal avec la commande `soffice` et en utilisant la combinaison de touches `Ctrl + C` si après l'arrêt de LibreOffice, le terminal n'est pas actif (pas d'invité de commande).

___

## Utilisation:

### Comment créer une nouvelle base de données:

Dans LibreOffice / OpenOffice aller à: Fichier -> Nouveau -> Base de données...:

![SQLiteOOo screenshot 1][25]

A l'étape: Sélectionner une base de données:
- selectionner: Créer une nouvelle base de données
- Dans: Base de données intégrée: choisir: Pilote SQLite intégré
- cliquer sur le bouton: Suivant

![SQLiteOOo screenshot 2][26]

A l'étape: Enregistrer et continuer:
- ajuster les paramètres selon vos besoins...
- cliquer sur le bouton: Terminer

![SQLiteOOo screenshot 3][27]

Maintenant à vous d'en profiter...

___

## Comment ça marche:

SQLiteOOo est un service [com.sun.star.sdbc.Driver][28] UNO écrit en Python.  
Il s'agit d'une surcouche à l'extension [jdbcDriverOOo][19] permettant de stocker la base de données SQLite dans un fichier odb (qui est, en fait, un fichier compressé).

Son fonctionnement est assez basique, à savoir:

- Lors d'une demande de connexion, trois choses sont faites:
    1. S'il n'existe pas déjà, un **sous-répertoire** avec le nom: `.` + `nom_du_fichier_odb` + `.lck` est créé à l'emplacement du fichier odb dans lequel tous les fichiers SQLite sont extraits du répertoire **database** du fichier odb (décompression).
    2. Un [DocumentHandler][29] est ajouté en tant que [com.sun.star.util.XCloseListener][30] et [com.sun.star.document.XStorageChangeListener][31] au fichier odb.
    3. L'extension [jdbcDriverOOo][19] est utilisée pour obtenir l'interface [com.sun.star.sdbc.XConnection][32] à partir du chemin du **sous-répertoire** + `nom_du_fichier_odb`.

- Lors de la fermeture ou du renommage (Enregistrer sous) d'un fichier odb, le [DocumentHandler][29] copie tous les fichiers présents dans le **sous-répertoire** dans le (nouveau) répertoire **database** du fichier odb (compression) puis supprime le **sous-répertoire**.

___

## A été testé avec:

* OpenOffice 4.1.8 - Ubuntu 20.04 - LxQt 0.14.1

* OpenOffice 4.1.8 - Windows 7 SP1

* LibreOffice 7.0.4.2 - Ubuntu 20.04 - LxQt 0.14.1

* LibreOffice 6.4.4.2 - Windows 7 SP1

* LibreOffice 7.6.0.1 - Windows 10

* LibreOffice 7.6.0.1 - Ubuntu 22.04

Je vous encourage en cas de problème :confused:  
de créer un [dysfonctionnement][13]  
J'essaierai de le résoudre :smile:

___

## Historique:

### Ce qui a été fait pour la version 1.0.0:

- Intégration de SQLite JDBC version 3.42.0.0. Je tiens tout particulièrement à remercier [gotson][33] pour les [nombreuses améliorations apportées au pilote SQLite JDBC][34] qui ont rendu possible l'utilisation de SQLite dans LibreOffice/OpenOffice.

### Ce qui a été fait pour la version 1.0.1:

- Résolution du [dysfonctionnement 156511][35] survenant lors de l'utilisation de l'interface com.sun.star.embed.XStorage. Le [contournement][36] consiste à utiliser la méthode copyElementTo() au lieu de moveElementTo(). Les versions de LibreOffice 7.6.x et supérieures deviennent utilisables.

### Ce qui a été fait pour la version 1.0.2:

- L'absence ou l'obsolescence de l'extension **jdbcDriverOOo** nécessaires au bon fonctionnement de **SQLiteOOo** affiche désormais un message d'erreur.

- Encore plein d'autres choses...

### Ce qui a été fait pour la version 1.1.0:

- Tous les paquets Python nécessaires à l'extension sont désormais enregistrés dans un fichier [requirements.txt][37] suivant la [PEP 508][38].
- Désormais si vous n'êtes pas sous Windows alors les paquets Python nécessaires à l'extension peuvent être facilement installés avec la commande:  
  `pip install requirements.txt`
- Modification de la section [Prérequis][39].

### Ce qui a été fait pour la version 1.1.1:

- Prise en charge des [nouvelles fonctionnalités][40] de **jdbcDriverOOo 1.1.2**.

### Ce qui a été fait pour la version 1.1.2:

- Pilote SQLite mis à jour vers la dernière version [SQLite-jdbc-3.45.1.3-SNAPSHOT.jar][41]. Ce nouveau pilote a été implémenté pour supporter une partie des spécifications JDBC 4.1 et plus particulièrement l'interface `java.sql.Statement.getGeneratedKeys()` et permet l'utilisation de l'interface [com.sun.star.sdbc.XGeneratedResultSet][42].

### Ce qui a été fait pour la version 1.1.3:

- Prise en charge de la dernière version de **jdbcDriverOOo 1.1.4** et de [SQLite-jdbc-3.45.1.6-SNAPSHOT.jar][43].
- Maintenant, pour un bon fonctionnement dans Base sous : **Édition -> Base de données -> Paramètres avancés... -> Requête des valeurs générées** doit être laissée vide. Si vous souhaitez utiliser un fichier odb créé avec une version précédente de SQLiteOOo vous devez modifier ce paramètre manuellement.
- Normalement les prochaines versions de SQLiteOOo devraient pouvoir être mises à jour dans la liste des extensions installées sous LibreOffice: **Outils -> Gestionnaire des extensions... -> Vérifier les mises à jour**.

### Ce qui a été fait pour la version 1.1.4:

- Prise en charge de la dernière version de **jdbcDriverOOo 1.3.1**.
- Lors de l'enregistrement sous un nom différent, la base de données si ouverte sera fermée correctement.

### Que reste-t-il à faire pour la version 1.1.4:

- Ajouter de nouvelles langue pour l'internationalisation...

- Tout ce qui est bienvenu...

[1]: </img/sqlite.svg#collapse>
[2]: <https://prrvchr.github.io/SQLiteOOo/>
[3]: <https://prrvchr.github.io/SQLiteOOo/>
[4]: <https://prrvchr.github.io/SQLiteOOo/source/SQLiteOOo/registration/TermsOfUse_fr>
[5]: <https://prrvchr.github.io/SQLiteOOo/README_fr#historique>
[6]: <https://prrvchr.github.io/README_fr>
[7]: <https://fr.libreoffice.org/download/telecharger-libreoffice/>
[8]: <https://www.openoffice.org/fr/Telecharger/>
[9]: <https://github.com/xerial/sqlite-jdbc>
[10]: <https://en.wikipedia.org/wiki/ACID>
[11]: <https://www.sqlite.org/transactional.html>
[12]: <https://github.com/prrvchr/SQLiteOOo/>
[13]: <https://github.com/prrvchr/SQLiteOOo/issues/new>
[14]: <https://prrvchr.github.io/jdbcDriverOOo/README_fr#pr%C3%A9requis>
[15]: <https://prrvchr.github.io/HyperSQLOOo/README_fr#prérequis>
[16]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156471>
[17]: <https://prrvchr.github.io/SQLiteOOo/README_fr#ce-qui-a-%C3%A9t%C3%A9-fait-pour-la-version-114>
[18]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.svg#middle>
[19]: <https://prrvchr.github.io/jdbcDriverOOo/README_fr>
[20]: <https://github.com/prrvchr/jdbcDriverOOo/releases/latest/download/jdbcDriverOOo.oxt>
[21]: <https://img.shields.io/github/v/tag/prrvchr/jdbcDriverOOo?label=latest#right>
[22]: <img/SQLiteOOo.svg#middle>
[23]: <https://github.com/prrvchr/SQLiteOOo/releases/latest/download/SQLiteOOo.oxt>
[24]: <https://img.shields.io/github/downloads/prrvchr/SQLiteOOo/latest/total?label=v1.1.4#right>
[25]: <img/SQLiteOOo-1_fr.png>
[26]: <img/SQLiteOOo-2_fr.png>
[27]: <img/SQLiteOOo-3_fr.png>
[28]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/Driver.html>
[29]: <https://github.com/prrvchr/SQLiteOOo/blob/main/uno/lib/uno/embedded/documenthandler.py>
[30]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/util/XCloseListener.html>
[31]: <http://www.openoffice.org/api/docs/common/ref/com/sun/star/document/XStorageChangeListener.html>
[32]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/XConnection.html>
[33]: <https://github.com/gotson>
[34]: <https://github.com/xerial/sqlite-jdbc/issues/786>
[35]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156511>
[36]: <https://github.com/prrvchr/uno/commit/a2fa9f5975a35e8447907e51b0f78ac1b1b76e17>
[37]: <https://github.com/prrvchr/SQLiteOOo/releases/latest/download/requirements.txt>
[38]: <https://peps.python.org/pep-0508/>
[39]: <https://prrvchr.github.io/SQLiteOOo/README_fr#pr%C3%A9requis>
[40]: <https://prrvchr.github.io/jdbcDriverOOo/README_fr#ce-qui-a-%C3%A9t%C3%A9-fait-pour-la-version-112>
[41]: <https://github.com/prrvchr/sqlite-jdbc/releases/download/3.45.1.3-SNAPSHOT/sqlite-jdbc-3.45.1.3-SNAPSHOT.jar>
[42]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/XGeneratedResultSet.html>
[43]: <https://github.com/prrvchr/sqlite-jdbc/releases/download/3.45.1.6-SNAPSHOT/sqlite-jdbc-3.45.1.6-SNAPSHOT.jar>
