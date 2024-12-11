class CompteBancaire :
    titulaire = "xxx"
    solde  = 100

    def deposer(montant):
        CompteBancaire.solde = CompteBancaire.solde + montant
        print(f" Votre nouveau solde est {CompteBancaire.solde}")
        return CompteBancaire.solde
    
    def retirer(montant):
        if montant <= CompteBancaire.solde:
            CompteBancaire.solde = CompteBancaire.solde - montant
            print(f"Votre solde devient : {CompteBancaire.solde}")
        else:
            print("Erreur !!!!! ")

    def afficher_solde():
        print(f"Votre solde Bancaire est : {CompteBancaire.solde}")

CB =  CompteBancaire.deposer(0)
CB = CompteBancaire.retirer(1)
CB = CompteBancaire.afficher_solde()
