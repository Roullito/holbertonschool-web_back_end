# 📦 Projet NoSQL - Holberton School

## 📖 Description
Ce projet introduit **MongoDB** et les bases de **NoSQL** via :
- Le **Mongo Shell** (commandes en ligne)
- Le **driver PyMongo** en Python

Vous apprendrez à manipuler des bases de données orientées documents, à effectuer des requêtes et à gérer des données dans un environnement NoSQL.

---

## 🎯 Objectifs
- Comprendre NoSQL et ses différences avec SQL
- Manipuler MongoDB en Shell et Python
- Effectuer des opérations CRUD
- Utiliser des filtres et agrégations simples

---

## ⚙️ Installation

### MongoDB (Ubuntu 20.04)
```bash
sudo apt update
sudo apt install -y mongodb
sudo systemctl start mongodb
sudo systemctl enable mongodb
```

### PyMongo
```bash
pip install pymongo
```

---

## 📂 Structure du projet
```
NoSQL/
│── 0-list_databases
│── 1-use_or_create_database
│── 2-insert
│── 3-all
│── 4-match
│── 5-count
│── 6-update
│── 7-delete
│── 8-all.py
│── 9-insert_school.py
│── 10-update_topics.py
│── 11-schools_by_topic.py
│── 12-log_stats.py
│── README.md
```

---

## 🚀 Utilisation
### Script Mongo Shell
```bash
cat 0-list_databases | mongo
```

### Script Python
```bash
python3 8-main.py
```

---

## 📜 Tâches principales
- **0-list_databases** → Liste les bases
- **1-use_or_create_database** → Crée/utilise une base
- **2-insert** → Insère un document
- **3-all** → Liste tous les documents
- **4-match** → Filtre par nom
- **5-count** → Compte les documents
- **6-update** → Met à jour un champ
- **7-delete** → Supprime un document
- **8-all.py** → Liste tous les documents (Python)
- **9-insert_school.py** → Insère un document (Python)
- **10-update_topics.py** → Met à jour les topics (Python)
- **11-schools_by_topic.py** → Filtre par topic (Python)
- **12-log_stats.py** → Analyse des logs Nginx

---

## 📚 Ressources
- [MongoDB Documentation](https://docs.mongodb.com/)
- [PyMongo Documentation](https://pymongo.readthedocs.io/)
