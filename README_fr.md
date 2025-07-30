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

**This [document][3] in English.**

**L'utilisation de ce logiciel vous soumet à nos [Conditions d'utilisation][4].**

# version [1.3.2][5]

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

De plus, en raison du [dysfonctionnement #156471][15] et suivant le [PR#154989][16], l'extension SQLiteOOo nécessite **LibreOffice version 24.2.x** minimum pour fonctionner.

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

Après avoir redémarré LibreOffice, vous pouvez vous assurer que l'extension et son pilote sont correctement installés en vérifiant que le pilote `io.github.prrvchr.SQLiteOOo.Driver` est répertorié dans le **Pool de Connexions**, accessible via le menu: **Outils -> Options -> LibreOffice Base -> Connexions**. Il n'est pas nécessaire d'activer le pool de connexions.

Si le pilote n'est pas répertorié, la raison de l'échec du chargement du pilote peut être trouvée dans la journalisation de l'extension. Cette journalisation est accessible via le menu: **Outils -> Options -> LibreOffice Base -> Pilote SQLite intégré -> Options de journalisation**.  
La journalisation `SQLiteLogger` doit d'abord être activée, puis LibreOffice redémarré pour obtenir le message d'erreur dans le journal.

N'oubliez pas au préalable de mettre à jour la version du JRE ou JDK Java installée sur votre ordinateur, cette extension utilise la nouvelle version de jdbcDriverOOo qui nécessite **Java version 17 ou ultérieure** au lieu de Java 11 auparavant.

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

- Lors d'une demande de connexion, plusieurs choses sont faites:
  - S'il n'existe pas déjà, un **sous-répertoire** avec le nom: `.` + `nom_du_fichier_odb` + `.lck` est créé à l'emplacement du fichier odb dans lequel tous les fichiers SQLite sont extraits du répertoire **database** du fichier odb (décompression).
  - L'extension [jdbcDriverOOo][19] est utilisée pour obtenir l'interface [com.sun.star.sdbc.XConnection][29] à partir du chemin du **sous-répertoire** + `/sqlite`.
  - Si la connexion réussi, un [DocumentHandler][30] est ajouté en tant que [com.sun.star.util.XCloseListener][31] et [com.sun.star.document.XStorageChangeListener][32] au fichier odb.
  - Si la connexion échoue et que les fichiers ont été extraits lors de la phase 1, le **sous-répertoire** est supprimé.
- Lors de la fermeture ou du changement de nom (Enregistrer sous) du fichier odb, si la connexion a réussi, le [DocumentHandler][30] copie tous les fichiers présents dans le **sous-répertoire** dans le (nouveau) répertoire **database** du fichier odb (zip), puis supprime le **sous-répertoire**.

Le but principal de ce mode de fonctionnement est de profiter des caractéristiques ACID de la base de données sous-jacente en cas de fermeture anormale de LibreOffice.
En contre partie, la fonction: **fichier -> Sauvegarder** n'a **aucun effet sur la base de données sous jacente**. Seul la fermeture du fichier odb ou son enregistrement sous un nom different (Fichier -> Enregistrer sous) effectura la sauvegarde de la base de donnée dans le fichier odb.

___

## Comment créer l'extension:

Normalement, l'extension est créée avec Eclipse pour Java et [LOEclipse][33]. Pour contourner Eclipse, j'ai modifié LOEclipse afin de permettre la création de l'extension avec Apache Ant.  
Pour créer l'extension SQLiteOOo avec l'aide d'Apache Ant, vous devez:
- Installer le [SDK Java][34] version 8 ou supérieure.
- Installer [Apache Ant][35] version 1.10.0 ou supérieure.
- Installer [LibreOffice et son SDK][36] version 7.x ou supérieure.
- Cloner le dépôt [SQLiteOOo][37] sur GitHub dans un dossier.
- Depuis ce dossier, accédez au répertoire: `source/SQLiteOOo/`
- Dans ce répertoire, modifiez le fichier `build.properties` afin que les propriétés `office.install.dir` et `sdk.dir` pointent vers les dossiers d'installation de LibreOffice et de son SDK, respectivement.
- Lancez la création de l'archive avec la commande: `ant`
- Vous trouverez l'archive générée dans le sous-dossier: `dist/`

___

## A été testé avec:

* LibreOffice 24.2.1.2 - Lubuntu 22.04

* LibreOffice 24.8.0.3 (X86_64) - Windows 10(x64) - Python version 3.9.19 (sous Lubuntu 22.04 / VirtualBox 6.1.38)

Je vous encourage en cas de problème :confused:  
de créer un [dysfonctionnement][13]  
J'essaierai de le résoudre :smile:

___

## Historique:

### Ce qui a été fait pour la version 1.0.0:

- Intégration de SQLite JDBC version 3.42.0.0. Je tiens tout particulièrement à remercier [gotson][38] pour les [nombreuses améliorations apportées au pilote SQLite JDBC][39] qui ont rendu possible l'utilisation de SQLite dans LibreOffice/OpenOffice.

### Ce qui a été fait pour la version 1.0.1:

- Résolution du [dysfonctionnement 156511][40] survenant lors de l'utilisation de l'interface com.sun.star.embed.XStorage. Le [contournement][41] consiste à utiliser la méthode copyElementTo() au lieu de moveElementTo(). Les versions de LibreOffice 7.6.x et supérieures deviennent utilisables.

### Ce qui a été fait pour la version 1.0.2:

- L'absence ou l'obsolescence de l'extension **jdbcDriverOOo** nécessaires au bon fonctionnement de **SQLiteOOo** affiche désormais un message d'erreur.

- Encore plein d'autres choses...

### Ce qui a été fait pour la version 1.1.0:

- Tous les paquets Python nécessaires à l'extension sont désormais enregistrés dans un fichier [requirements.txt][42] suivant la [PEP 508][43].
- Désormais si vous n'êtes pas sous Windows alors les paquets Python nécessaires à l'extension peuvent être facilement installés avec la commande:  
  `pip install requirements.txt`
- Modification de la section [Prérequis][44].

### Ce qui a été fait pour la version 1.1.1:

- Prise en charge des [nouvelles fonctionnalités][45] de **jdbcDriverOOo 1.1.2**.

### Ce qui a été fait pour la version 1.1.2:

- Pilote SQLite mis à jour vers la dernière version [SQLite-jdbc-3.45.1.3-SNAPSHOT.jar][46]. Ce nouveau pilote a été implémenté pour supporter une partie des spécifications JDBC 4.1 et plus particulièrement l'interface `java.sql.Statement.getGeneratedKeys()` et permet l'utilisation de l'interface [com.sun.star.sdbc.XGeneratedResultSet][47].

### Ce qui a été fait pour la version 1.1.3:

- Prise en charge de la dernière version de **jdbcDriverOOo 1.1.4** et de [SQLite-jdbc-3.45.1.6-SNAPSHOT.jar][48].
- Maintenant, pour un bon fonctionnement dans Base sous : **Édition -> Base de données -> Paramètres avancés... -> Requête des valeurs générées** doit être laissée vide. Si vous souhaitez utiliser un fichier odb créé avec une version précédente de SQLiteOOo vous devez modifier ce paramètre manuellement.
- Normalement les prochaines versions de SQLiteOOo devraient pouvoir être mises à jour dans la liste des extensions installées sous LibreOffice: **Outils -> Gestionnaire des extensions... -> Vérifier les mises à jour**.

### Ce qui a été fait pour la version 1.1.4:

- Prise en charge de la dernière version de **jdbcDriverOOo 1.3.1**.
- Lors de l'enregistrement sous un nom différent, la base de données si ouverte sera fermée correctement.

### Ce qui a été fait pour la version 1.1.5:

- Utilisation du nouveau format de données implémenté dans la version 1.1.4. Par conséquent, si vous devez ouvrir des fichiers odb créés avec une version inférieure à 1.1.4, vous devez d'abord les ouvrir avec la version 1.1.4, sinon une erreur sera générée.

### Ce qui a été fait pour la version 1.2.0:

- Cette version est basée sur la [correction #154989][49] disponible depuis LibreOffice 24.2.x. Elle peut donc fonctionner avec les autres extensions proposant des services de bases de données intégrées.
- Désormais, SQLiteOOo nécessite LibreOffice 24.2.x minimum et se chargera pour l'url: `sdbc:embedded:sqlite`.

### Ce qui a été fait pour la version 1.2.1:

- Mise à jour du paquet [Python packaging][50] vers la version 24.1.
- Mise à jour du paquet [Python setuptools][51] vers la version 72.1.0.
- L'extension vous demandera d'installer l'extensions jdbcDriverOOo en version 1.4.2 minimum.

### Ce qui a été fait pour la version 1.2.2:

- Correction du [problème n°2][52] qui semble être une régression liée à la sortie de JaybirdOOo. Merci à madalienist de l'avoir signalé.
- Mise à jour du paquet [Python setuptools][51] vers la version 73.0.1.
- Les options de l'extension sont désormais accessibles via: **Outils -> Options -> LibreOffice Base -> Pilote SQLite intégré**
- La journalisation accessible dans les options de l’extension s’affiche désormais correctement sous Windows.
- Les modifications apportées aux options de l'extension, qui nécessitent un redémarrage de LibreOffice, entraîneront l'affichage d'un message.
- Dans les options de l'extension il est possible de définir les options: **Afficher les tables système**, **Utiliser les signets** et **Forcer le mode SQL** qui seront spécifiques à ce pilote.
- Nécessite la dernière version de **jdbcDriverOOo 1.4.4**.
- Support de LibreOffice version 24.8.x.

### Ce qui a été fait pour la version 1.2.3:

- L'extension vous demandera d'installer l'extensions jdbcDriverOOo en version 1.4.6 minimum.
- Modification des options de l'extension accessibles via : **Outils -> Options -> LibreOffice Base -> Pilote SQLite intégré** afin de respecter la nouvelle charte graphique.

### Ce qui a été fait pour la version 1.3.0:

- Mise à jour du paquet [Python packaging][50] vers la version 25.0.
- Mise à jour du paquet [Python setuptools][51] vers la version 75.3.2.
- Déploiement de l'enregistrement passif permettant une installation beaucoup plus rapide des extensions et de différencier les services UNO enregistrés de ceux fournis par une implémentation Java ou Python. Cet enregistrement passif est assuré par l'extension [LOEclipse][33] via les [PR#152][53] et [PR#157][54].
- Modification de [LOEclipse][33] pour prendre en charge le nouveau format de fichier `rdb` produit par l'utilitaire de compilation `unoidl-write`. Les fichiers `idl` ont été mis à jour pour prendre en charge les deux outils de compilation disponibles: idlc et unoidl-write.
- Implémentation de [PEP 570][55] dans la [journalisation][56] pour prendre en charge les arguments multiples uniques.
- Il est désormais possible de créer le fichier oxt de l'extension SQLiteOOo uniquement avec Apache Ant et une copie du dépôt GitHub. La section [Comment créer l'extension][57] a été ajoutée à la documentation.
- Toute erreur survenant lors du chargement du pilote sera consignée dans le journal de l'extension si la journalisation a été préalablement activé. Cela facilite l'identification des problèmes d'installation sous Windows.
- Nécessite l'extension **jdbcDriverOOo en version 1.5.0 minimum**.

### Ce qui a été fait pour la version 1.3.1:

- De nombreuses corrections qui empêchaient le bon fonctionnement ont été apportées au pilote écrit en Python et enveloppant le pilote fourni par jdbcDriverOOo.
- Nécessite l'extension **jdbcDriverOOo en version 1.5.1 minimum**.

### Ce qui a été fait pour la version 1.3.2:

- Nécessite l'extension **jdbcDriverOOo en version 1.5.4 minimum**.

### Que reste-t-il à faire pour la version 1.3.2:

- Ajouter de nouvelles langue pour l'internationalisation...

- Tout ce qui est bienvenu...

[1]: </img/sqlite.svg#collapse>
[2]: <https://prrvchr.github.io/SQLiteOOo/>
[3]: <https://prrvchr.github.io/SQLiteOOo/>
[4]: <https://prrvchr.github.io/SQLiteOOo/source/SQLiteOOo/registration/TermsOfUse_fr>
[5]: <https://prrvchr.github.io/SQLiteOOo/README_fr#ce-qui-a-%C3%A9t%C3%A9-fait-pour-la-version-132>
[6]: <https://prrvchr.github.io/README_fr>
[7]: <https://fr.libreoffice.org/download/telecharger-libreoffice/>
[8]: <https://www.openoffice.org/fr/Telecharger/>
[9]: <https://github.com/xerial/sqlite-jdbc>
[10]: <https://en.wikipedia.org/wiki/ACID>
[11]: <https://www.sqlite.org/transactional.html>
[12]: <https://github.com/prrvchr/SQLiteOOo/>
[13]: <https://github.com/prrvchr/SQLiteOOo/issues/new>
[14]: <https://prrvchr.github.io/jdbcDriverOOo/README_fr#pr%C3%A9requis>
[15]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156471>
[16]: <https://gerrit.libreoffice.org/c/core/+/154989>
[18]: <https://prrvchr.github.io/jdbcDriverOOo/img/jdbcDriverOOo.svg#middle>
[19]: <https://prrvchr.github.io/jdbcDriverOOo/README_fr>
[20]: <https://github.com/prrvchr/jdbcDriverOOo/releases/latest/download/jdbcDriverOOo.oxt>
[21]: <https://img.shields.io/github/v/tag/prrvchr/jdbcDriverOOo?label=latest#right>
[22]: <img/SQLiteOOo.svg#middle>
[23]: <https://github.com/prrvchr/SQLiteOOo/releases/latest/download/SQLiteOOo.oxt>
[24]: <https://img.shields.io/github/downloads/prrvchr/SQLiteOOo/latest/total?label=v1.3.2#right>
[25]: <img/SQLiteOOo-1_fr.png>
[26]: <img/SQLiteOOo-2_fr.png>
[27]: <img/SQLiteOOo-3_fr.png>
[28]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/Driver.html>
[29]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/XConnection.html>
[30]: <https://github.com/prrvchr/SQLiteOOo/blob/main/uno/lib/uno/embedded/documenthandler.py>
[31]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/util/XCloseListener.html>
[32]: <http://www.openoffice.org/api/docs/common/ref/com/sun/star/document/XStorageChangeListener.html>
[33]: <https://github.com/LibreOffice/loeclipse>
[34]: <https://adoptium.net/temurin/releases/?version=8&package=jdk>
[35]: <https://ant.apache.org/manual/install.html>
[36]: <https://downloadarchive.documentfoundation.org/libreoffice/old/7.6.7.2/>
[37]: <https://github.com/prrvchr/SQLiteOOo.git>
[38]: <https://github.com/gotson>
[39]: <https://github.com/xerial/sqlite-jdbc/issues/786>
[40]: <https://bugs.documentfoundation.org/show_bug.cgi?id=156511>
[41]: <https://github.com/prrvchr/uno/commit/a2fa9f5975a35e8447907e51b0f78ac1b1b76e17>
[42]: <https://github.com/prrvchr/SQLiteOOo/releases/latest/download/requirements.txt>
[43]: <https://peps.python.org/pep-0508/>
[44]: <https://prrvchr.github.io/SQLiteOOo/README_fr#pr%C3%A9requis>
[45]: <https://prrvchr.github.io/jdbcDriverOOo/README_fr#ce-qui-a-%C3%A9t%C3%A9-fait-pour-la-version-112>
[46]: <https://github.com/prrvchr/sqlite-jdbc/releases/download/3.45.1.3-SNAPSHOT/sqlite-jdbc-3.45.1.3-SNAPSHOT.jar>
[47]: <https://www.openoffice.org/api/docs/common/ref/com/sun/star/sdbc/XGeneratedResultSet.html>
[48]: <https://github.com/prrvchr/sqlite-jdbc/releases/download/3.45.1.6-SNAPSHOT/sqlite-jdbc-3.45.1.6-SNAPSHOT.jar>
[49]: <https://gerrit.libreoffice.org/c/core/+/154989>
[50]: <https://pypi.org/project/packaging/>
[51]: <https://pypi.org/project/setuptools/>
[52]: <https://github.com/prrvchr/SQLiteOOo/issues/2>
[53]: <https://github.com/LibreOffice/loeclipse/pull/152>
[54]: <https://github.com/LibreOffice/loeclipse/pull/157>
[55]: <https://peps.python.org/pep-0570/>
[56]: <https://github.com/prrvchr/SQLiteOOo/blob/main/uno/lib/uno/logger/logwrapper.py#L109>
[57]: <https://prrvchr.github.io/SQLiteOOo/README_fr#comment-cr%C3%A9er-lextension>
