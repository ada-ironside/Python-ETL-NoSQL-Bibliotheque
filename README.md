# Projet Final : Gestion de Bibliothèque & Pipeline ETL NoSQL

**Auteur :** Ada Faty GATH

**Cours :** Programmation Python

---

## 📋 Description du Projet
Ce projet académique est une application complète de gestion de bibliothèque numérique développée en Python. 
Au-delà des fonctionnalités classiques de gestion, il a été conçu pour simuler une **architecture de données NoSQL** et mettre en œuvre un **pipeline ETL** (Extract, Transform, Load) complet.

L'objectif est double :
1. **Répondre au cahier des charges** : CRUD, emprunts, statistiques et persistance.
2. **Démontrer une expertise Data** : Validation des données (Data Quality), sérialisation JSON et calcul de KPIs.

---

## ⚙️ Fonctionnalités & Architecture Technique

### 1. Ingestion et Gestion des Données (CRUD & Data Quality)
- **Ingestion (Extract)** : Saisie des livres via l'interface console.
- **Data Quality (Transform)** : Implémentation de règles de validation strictes (cohérence des années, prix positifs, types de données) pour garantir l'intégrité de la base avant insertion.
- **CRUD** : Création, Lecture, Mise à jour et Suppression des enregistrements dans le catalogue.

### 2. Gestion des Flux (Emprunts/Retours)
- **Transactionnel** : Gestion des états de disponibilité des livres en temps réel.
- **Filtrage** : Moteur de recherche multicritères et extraction de sous-ensembles par genre.

### 3. Reporting & KPIs (Analytics)
Un module d'analyse génère un tableau de bord statistique affichant :
- **Volumétrie** : Nombre total de livres et taux de disponibilité.
- **Valorisation** : Calcul de la valeur financière du stock.
- **Tendances** : Identification du genre dominant (Mode) et des valeurs extrêmes (Prix Max/Min).

### 4. Persistance NoSQL (Load)
- **Stockage** : Utilisation du format **JSON** pour simuler une base de données documentaire légère (NoSQL).
- **Sérialisation** : Sauvegarde automatique de l'état du système à chaque transaction (Commit).

---

## 📂 Structure du Projet

Le projet est organisé en 3 fichiers respectant le principe de séparation des responsabilités :

1. **`main.py` (Interface / Orchestrateur)** : 
   Point d'entrée du programme. Il gère le menu interactif et déclenche les fonctions métier.
   
2. **`bibliotheque.py` (Core Logic / ETL)** : 
   Module contenant les algorithmes de transformation, les règles de validation et la logique de gestion des fichiers.
   
3. **`bibliotheque.json` (Base de Données)** : 
   Fichier de persistance agissant comme une base NoSQL (généré automatiquement).

---

## 🚀 Installation et Exécution

### Prérequis
- Python 3.x installé.
- Librairies standards uniquement (`json`, `os`, `datetime`).

### Démarrage
1. Placez les fichiers `main.py` et `bibliotheque.py` dans le même dossier.
2. Ouvrez un terminal dans ce dossier.
3. Lancez la commande :
   ```bash
   python main.py

📝 Scénario de Test (Validation)
​Pour valider le bon fonctionnement de l'application, suivez ces étapes :
​Initialisation : Lancez l'application via le terminal.
​Data Entry : Choisissez l'option 1 et ajoutez un livre (ex: 1984, Orwell, SF, 1949, 10.0). Le système validera la cohérence de l'année.
​Consultation : Vérifiez l'affichage dans le catalogue avec l'option 2.
​Analyse : Affichez le rapport statistique avec l'option 7 pour voir les KPIs mis à jour (Valorisation du stock, genre dominant).
​Persistance : Quittez avec l'option 9. Relancez l'application pour vérifier que les données sont bien rechargées depuis le JSON.
​<!-- end list -->
