# OpenClassroom-P9

## Contenu du dépôt :

Scripts et fichiers utilsés pour entrainer, valider deux modèles de recomendation et la réalisation d'un premier MVP qui prend la forme d'une application mobile.


### P9-Scripts.ipynb :

Notebook de développement des algorithmes Content-Based (similarité cosinus) et Collaborative Filtering (utilisant la librairie implicit ). Il comprend également les sauvegardes nécessaires au déploiement du modèle.


### functionOC :

API serverless déployée sur Azure pour interagir avec l'app mobile. Elle reçoit en entrée un n° d'utilisateur et renvoie une liste des 5 recommandations les plus pertinentes.

### bookshelf

Application mobile. Ajout de l'URL de l'API serverless dans le fichier config.json.
