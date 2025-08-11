<div align="center">
  <img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png" alt="Banner">
</div>

# 📚 Pagination – Projet Holberton School

## 📌 Description
Ce projet a pour objectif de comprendre et d’implémenter différents types de **pagination** dans le cadre d’une API ou d’un dataset :
1. **Pagination simple** avec `page` et `page_size`.
2. **Pagination hypermédia** avec métadonnées (HATEOAS).
3. **Pagination résiliente aux suppressions**.

## 🎯 Objectifs pédagogiques
- Savoir paginer un dataset avec de simples paramètres.
- Ajouter des métadonnées pour faciliter la navigation dans les données.
- Gérer la suppression d’éléments sans perdre ou répéter de données.

## 🛠 Technologies utilisées
- **Python 3.9**
- **CSV**
- **Type annotations**
- **Pycodestyle** (PEP8)

## 📂 Structure des fichiers
- `0-simple_helper_function.py` → Fonction `index_range`
- `1-simple_pagination.py` → Méthode `get_page`
- `2-hypermedia_pagination.py` → Méthode `get_hyper`
- `3-hypermedia_del_pagination.py` → Méthode `get_hyper_index`

## 📜 Dataset
Le projet utilise le fichier : Popular_Baby_Names.csv

Contenant 19 418 lignes de données sur les prénoms les plus populaires.

## 🚀 Lancer les tests
```bash
./0-main.py
./1-main.py
./2-main.py
./3-main.py
