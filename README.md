# Projet Expedition 5300 - Analyses R

Ce dossier contient l'ensemble du code que j'ai développé dans le cadre du projet Expedition 5300 enfants.  
Il est organisé en plusieurs fichiers R Markdown correspondant aux étapes principales du travail.

---

## Contenu des fichiers

- **01_stats_generales.Rmd**  
  Analyses et visualisations des données suivant des questions posées préalablement avec catégories visibles dans le fichier.

- **02_boxplots_barplots.Rmd**  
  Generation de boxplots et barplots pour visualiser les distributions et comparaisons entre villes pour chaque variable numérique (boxplots) et chaque variable catégorielle (barplots).

- **03_tableaux_variables.Rmd**  
  Analyses statistiques principales (tableaux desctiptifs, modèles linéaires siples, comparaisons entre groupes).

---

## Ordre d’exécution

1. `01_stats_generales.Rmd`  
2. `02_boxplots_barplots.Rmd`  
3. `03_tableaux_variables.Rmd`

Chaque fichier peut être exécuté indépendamment, mais il est recommandé de suivre l’ordre ci-dessus.

---

## Dépendances

### Version de R
- R >= 4.3.0

### Packages nécessaires
Les packages nécessaires sont listés au début de chaque fichier RMD.

---

## Données

⚠️ Les données originales utilisées dans ce projet ne sont pas incluses pour des raisons de confidentialité.  
Chaque RMD suppose que les fichiers de données sont disponibles dans le dossier `\02_R_scripts`.  
Adapter les chemins si nécessaire.

---