# Projet d'Introduction à Python

Ce projet contient une série de notebooks Jupyter pour apprendre les bases de Python, y compris les variables, les structures de données, les conditions, les boucles, les fonctions, la programmation orientée objet, et plus encore.

## Contenu des Notebooks

- **0 - Installation Python.pptx** : Présentation sur l'installation de Python.
- **1-introduction.ipynb** : Introduction à Python (scripts vs notebooks, commentaires, raccourcis).
- **2-les-variables.ipynb** : Les variables en Python.
- **3-data-structures.ipynb** : Les structures de données en Python.
- **3b-data-structures.ipynb** : Suite des structures de données.
- **4-les_conditions_et_les_boucles.ipynb** : Les conditions et les boucles.
- **5-Les_fonctions.ipynb** : Les fonctions en Python.
- **5b-lambda.ipynb** : Les fonctions lambda.
- **5c-le_typage.ipynb** : Le typage en Python.
- **6-les-packages.ipynb** : Gestion des packages et environnements virtuels.
- **7-functions-args.ipynb** : Les arguments de fonctions avancés (*args, **kwargs).
- **8-fonction-recursive.ipynb** : Les fonctions récursives.
- **9-falsy-values.ipynb** : Les valeurs falsy en Python.
- **exos.ipynb** : Exercices pratiques.

## Programmation Orientée Objet (POO)

Le dossier `oop/` contient des notebooks et des scripts pour apprendre la programmation orientée objet en Python :

- **1-Introduction_POO.ipynb** : Introduction à la POO (classes, attributs, méthodes, héritage).
- **class_to_test.py** : Classe servant de support aux tests unitaires.
- **test_class_to_test.py** : Tests unitaires avec pytest.
- **correction.py** : Corrections des exercices (encapsulation, @property, classes abstraites, zoo).
- **correction_conce_bis.py** : Correction alternative de l'exercice de conception.
- **correction_concessionnaire.py** : Correction de l'exercice concessionnaire.
- **correction_exercice_blog.py** : Correction de l'exercice blog.
- **correction_toolbox.py** / **correction_toolbox_bis.py** : Corrections de l'exercice toolbox.
- **correction_zoo.py** : Correction de l'exercice zoo.
- **Correction_exercice_concessionnaire.ipynb** : Correction notebook concessionnaire.
- **Correction_forum.ipynb** : Correction notebook forum.
- **img/** : Diagrammes de classes (héritage, premier diagramme).

## Fichiers de support (imports)

- **Same_level.py** : Fonctions de démonstration pour les imports depuis le même répertoire (utilisé dans le notebook 6).
- **other_folder/other_folder_file.py** : Fonction de démonstration pour les imports depuis un sous-dossier (utilisé dans le notebook 6).
- **recursif.py** : Script de démonstration pour les fonctions récursives.

## Utilisation des Environnements Virtuels

Dans le notebook **6-les-packages.ipynb**, vous apprendrez à utiliser les environnements virtuels avec `venv`, `virtualenv`, et `conda`.

### Commandes Principales

- **Créer un environnement virtuel** :
  ```bash
  python -m venv venv
  ```
- **Activer l'environnement virtuel** :
  - Unix : `source venv/bin/activate`
  - Windows : `venv\Scripts\activate`
- **Désactiver l'environnement virtuel** :
  ```bash
  deactivate
  ```

## Installation des Dépendances

Pour installer les dépendances nécessaires, utilisez la commande suivante après avoir activé votre environnement virtuel :

```bash
pip install -r requirements.txt
```

## Lancer les tests

```bash
pytest oop/ -v
```

## Contribuer

Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour discuter des changements que vous souhaitez apporter.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
