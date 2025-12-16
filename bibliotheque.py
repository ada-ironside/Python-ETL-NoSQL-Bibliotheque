import json
import os
import datetime

# Nom du fichier de sauvegarde
FICHIER_DB = "bibliotheque.json"

def charger_bibliotheque():
    """
    Charge les données depuis le fichier JSON.
    Retourne une liste vide si le fichier n'existe pas ou est corrompu.
    """
    if not os.path.exists(FICHIER_DB):
        return []
    
    try:
        with open(FICHIER_DB, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("⚠️  Le fichier de sauvegarde est corrompu. Démarrage avec une bibliothèque vide.")
        return []

def sauvegarder_bibliotheque(livres):
    """
    Sauvegarde la liste des livres dans le fichier JSON.
    """
    try:
        with open(FICHIER_DB, 'w', encoding='utf-8') as f:
            json.dump(livres, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"❌ Erreur lors de la sauvegarde : {e}")

def ajouter_livre(livres, titre, auteur, genre, annee, prix):
    """
    Ajoute un livre à la bibliothèque après validation des données.
    """
    # Validation des données
    if not titre or not auteur or not genre:
        print("❌ Erreur : Le titre, l'auteur et le genre ne peuvent pas être vides.")
        return

    try:
        annee = int(annee)
        prix = float(prix)
        annee_actuelle = datetime.date.today().year
        
        if not (1000 <= annee <= annee_actuelle):
            print(f"❌ Erreur : L'année doit être comprise entre 1000 et {annee_actuelle}.")
            return
        
        if prix <= 0:
            print("❌ Erreur : Le prix doit être strictement positif.")
            return

    except ValueError:
        print("❌ Erreur : L'année doit être un entier et le prix un nombre.")
        return

    # Génération de l'ID unique
    nouvel_id = 1
    if livres:
        nouvel_id = max(livre['id'] for livre in livres) + 1

    nouveau_livre = {
        'id': nouvel_id,
        'titre': titre,
        'auteur': auteur,
        'genre': genre,
        'année_publication': annee,
        'prix': prix,
        'disponible': True
    }

    livres.append(nouveau_livre)
    print(f"✅ Livre '{titre}' ajouté avec succès (ID: {nouvel_id}).")

def afficher_tous_les_livres(livres):
    """
    Affiche la liste des livres sous forme de tableau.
    """
    if not livres:
        print("📂 La bibliothèque est vide.")
        return

    print(f"{'ID':<5} | {'Titre':<30} | {'Auteur':<20} | {'Genre':<15} | {'Prix':<8} | {'État'}")
    print("-" * 95)
    
    for livre in livres:
        etat = "✅ Dispo" if livre['disponible'] else "❌ Emprunté"
        titre_court = (livre['titre'][:27] + '..') if len(livre['titre']) > 27 else livre['titre']
        print(f"{livre['id']:<5} | {titre_court:<30} | {livre['auteur']:<20} | {livre['genre']:<15} | {livre['prix']:<6.2f}€ | {etat}")

def rechercher_livre(livres, critere, valeur):
    """
    Recherche un livre par titre, auteur ou genre (insensible à la casse).
    """
    resultats = []
    valeur = valeur.lower()
    
    for livre in livres:
        # On gère le cas où le critère est l'année (int) en convertissant en str
        contenu = str(livre.get(critere, '')).lower()
        if valeur in contenu:
            resultats.append(livre)
            
    if resultats:
        print(f"🔍 {len(resultats)} résultat(s) trouvé(s) :")
        afficher_tous_les_livres(resultats)
    else:
        print("🚫 Aucun livre ne correspond à votre recherche.")

def supprimer_livre(livres, id_livre):
    """
    Supprime un livre par son ID après confirmation.
    """
    for index, livre in enumerate(livres):
        if livre['id'] == id_livre:
            confirmation = input(f"⚠️  Voulez-vous vraiment supprimer '{livre['titre']}' ? (o/n) : ")
            if confirmation.lower() == 'o':
                del livres[index]
                print("🗑️  Livre supprimé avec succès.")
            else:
                print("Annulation.")
            return
    print("❌ ID introuvable.")

def emprunter_livre(livres, id_livre):
    """
    Passe le statut d'un livre à 'Non disponible'.
    """
    for livre in livres:
        if livre['id'] == id_livre:
            if not livre['disponible']:
                print("❌ Ce livre est déjà emprunté.")
            else:
                livre['disponible'] = False
                print(f"📖 Vous avez emprunté '{livre['titre']}'. Bonne lecture !")
            return
    print("❌ ID introuvable.")

def retourner_livre(livres, id_livre):
    """
    Passe le statut d'un livre à 'Disponible'.
    """
    for livre in livres:
        if livre['id'] == id_livre:
            if livre['disponible']:
                print("❌ Ce livre est déjà marqué comme disponible.")
            else:
                livre['disponible'] = True
                print(f"📥 Merci d'avoir retourné '{livre['titre']}'.")
            return
    print("❌ ID introuvable.")

def filtrer_par_genre(livres, genre):
    """
    Affiche uniquement les livres d'un genre spécifique.
    """
    resultats = [livre for livre in livres if livre['genre'].lower() == genre.lower()]
    if resultats:
        print(f"📂 Livres du genre '{genre}' :")
        afficher_tous_les_livres(resultats)
    else:
        print(f"🚫 Aucun livre trouvé pour le genre '{genre}'.")

def generer_rapport(livres):
    """
    Génère et affiche des statistiques sur la bibliothèque.
    """
    if not livres:
        print("🚫 Pas de données suffisantes pour générer un rapport.")
        return

    total_livres = len(livres)
    disponibles = sum(1 for l in livres if l['disponible'])
    empruntes = total_livres - disponibles
    valeur_totale = sum(l['prix'] for l in livres)
    
    # Livre le plus cher / moins cher
    livre_plus_cher = max(livres, key=lambda x: x['prix'])
    livre_moins_cher = min(livres, key=lambda x: x['prix'])

    # Genre le plus représenté
    genres = [l['genre'] for l in livres]
    genre_top = max(set(genres), key=genres.count)

    print("\n📊 === RAPPORT STATISTIQUE ===")
    print(f"📚 Nombre total de livres : {total_livres}")
    print(f"✅ Livres disponibles     : {disponibles}")
    print(f"❌ Livres empruntés       : {empruntes}")
    print(f"💰 Valeur du stock        : {valeur_totale:.2f} €")
    print(f"💎 Livre le plus cher     : {livre_plus_cher['titre']} ({livre_plus_cher['prix']}€)")
    print(f"📉 Livre le moins cher    : {livre_moins_cher['titre']} ({livre_moins_cher['prix']}€)")
    print(f"🏆 Genre le plus fréquent : {genre_top}")
    print("=============================")
