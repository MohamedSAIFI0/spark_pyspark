# TP1 — Spark RDD (PySpark)

Ceci est un petit projet d'exemples d'opérations sur des RDDs avec PySpark. Le script principal est `app.py` et un `docker-compose.yml` est fourni pour démarrer un cluster Spark (master + worker) à des fins de test.

## Contenu

- `app.py` : script Python qui crée un RDD local et exécute plusieurs opérations (collect, count, sum, mean, map, filter, take, etc.).
- `docker-compose.yml` : compose pour lancer un master Spark et un worker (image officielle Apache Spark).

## Contrat rapide

- Entrée : aucune (le script utilise une liste en dur `ma_liste`).
- Sortie : logs/prints sur la sortie standard montrant les résultats des opérations RDD.
## Prérequis

- Pour exécution locale (hors Docker) :
  - Python 3.8+
  - Java 8 ou 11 (nécessaire pour Spark/PySpark)
  - PySpark (recommandé : `pyspark==3.5.1` pour correspondre à l'image Docker fournie)

- Pour exécution avec Docker :
  - Docker
  - docker-compose

## Installation (locale)

1. (optionnel) Créer et activer un environnement virtuel :

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Installer PySpark :

```bash
pip install pyspark==3.5.1
```

3. Lancer le script :

```bash
python app.py
```

Vous verrez les résultats imprimés dans la console.

## Exécution avec Docker Compose

Le fichier `docker-compose.yml` démarre un master et un worker Spark. Il ne soumet pas automatiquement `app.py` aux containers — deux approches possibles :

1) Copier le script dans le container maître et lancer `spark-submit` :

```bash
docker-compose up -d
docker cp app.py spark-master:/opt/app/app.py
docker exec -it spark-master /opt/spark/bin/spark-submit --master spark://spark-master:7077 /opt/app/app.py
```

2) (Recommandé pour usage répété) Modifier `docker-compose.yml` pour monter le dossier du projet dans le container et ajouter un service `submit` ou lancer `spark-submit` depuis un conteneur client qui a accès au code monté. Exemple d'idée : monter `.:/opt/app` et lancer `/opt/spark/bin/spark-submit --master spark://spark-master:7077 /opt/app/app.py`.

Remarque : l'image utilisée est `apache/spark:3.5.1`. Assurez-vous d'utiliser la même version de PySpark localement si vous mélangez exécution locale et container.

## Que fait `app.py` ?

Le script :

- crée un SparkContext en mode `local`
- crée un RDD à partir d'une liste d'entiers
- exécute et affiche plusieurs actions et transformations : `collect`, `count`, `sum`, `mean`, `map`, `filter`, `max`, `min`, `take`...

Exemple de sortie attendue (abrégée) :

```
[1, 2, 3, 4, 5, 6, 7]
7
28
4.0
[False, True, False, True, False, True, False]
<...>
```

## Débogage et vérification

- Vérifier que Java est installé :

```bash
java -version
```

- Vérifier la version de PySpark :

```bash
python -c "import pyspark; print(pyspark.__version__)"
```

- Pour Docker : consulter les UIs Spark :
  - Master UI : http://localhost:8080
  - Worker UI : http://localhost:8081

