class livre :
    titre = "psychologie of money"
    auteur = "moss randall"
    annee_publication =  2017

class bibliotheque :
    liste_books = ["Ego is the Enemy","48 laws of Power","Art of war","la nuit sacree","Rich and Poor DAD"]
    def ajouter_livre(livre):
        bibliotheque.liste_books.append(livre.titre)

    def afficher_livres():
        for i in bibliotheque.liste_books :
            print(i)

L0 = livre()
bibliotheque.ajouter_livre(L0)
bibliotheque.afficher_livres()
