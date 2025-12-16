import bibliotheque as lib

def menu():
    # Chargement des données au démarrage
    ma_bibliotheque = lib.charger_bibliotheque()

    while True:
        print("\n" + "="*40)
        print(" 🏛️  GESTION DE BIBLIOTHÈQUE NUMÉRIQUE ")
        print("="*40)
        print("1. Ajouter un livre")
        print("2. Afficher tous les livres")
        print("3. Rechercher un livre")
        print("4. Emprunter un livre")
        print("5. Retourner un livre")
        print("6. Filtrer par genre")
        print("7. Afficher les statistiques")
        print("8. Supprimer un livre")
        print("9. Quitter")
        
        choix = input("\n👉 Votre choix : ")

        if choix == '1':
            print("\n--- Ajout d'un nouveau livre ---")
            titre = input("Titre : ")
            auteur = input("Auteur : ")
            genre = input("Genre : ")
            annee = input("Année de publication : ")
            prix = input("Prix : ")
            lib.ajouter_livre(ma_bibliotheque, titre, auteur, genre, annee, prix)
            lib.sauvegarder_bibliotheque(ma_bibliotheque)

        elif choix == '2':
            print("\n--- Catalogue complet ---")
            lib.afficher_tous_les_livres(ma_bibliotheque)

        elif choix == '3':
            print("\n--- Recherche ---")
            critere = input("Rechercher par (titre/auteur/genre) ? : ").lower()
            if critere in ['titre', 'auteur', 'genre']:
                valeur = input(f"Entrez le {critere} : ")
                lib.rechercher_livre(ma_bibliotheque, critere, valeur)
            else:
                print("❌ Critère invalide.")

        elif choix == '4':
            print("\n--- Emprunt ---")
            try:
                id_livre = int(input("ID du livre à emprunter : "))
                lib.emprunter_livre(ma_bibliotheque, id_livre)
                lib.sauvegarder_bibliotheque(ma_bibliotheque)
            except ValueError:
                print("❌ L'ID doit être un nombre entier.")

        elif choix == '5':
            print("\n--- Retour ---")
            try:
                id_livre = int(input("ID du livre à retourner : "))
                lib.retourner_livre(ma_bibliotheque, id_livre)
                lib.sauvegarder_bibliotheque(ma_bibliotheque)
            except ValueError:
                print("❌ L'ID doit être un nombre entier.")

        elif choix == '6':
            print("\n--- Filtrer par genre ---")
            genre = input("Quel genre souhaitez-vous afficher ? : ")
            lib.filtrer_par_genre(ma_bibliotheque, genre)

        elif choix == '7':
            lib.generer_rapport(ma_bibliotheque)

        elif choix == '8':
            print("\n--- Suppression ---")
            try:
                id_livre = int(input("ID du livre à supprimer : "))
                lib.supprimer_livre(ma_bibliotheque, id_livre)
                lib.sauvegarder_bibliotheque(ma_bibliotheque)
            except ValueError:
                print("❌ L'ID doit être un nombre entier.")

        elif choix == '9':
            print("\n💾 Sauvegarde finale...")
            lib.sauvegarder_bibliotheque(ma_bibliotheque)
            print("👋 Au revoir !")
            break
        
        else:
            print("❌ Option invalide, veuillez choisir entre 1 et 9.")

if __name__ == "__main__":
    menu()
