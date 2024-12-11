class Voiture :
    marque = "BMW"
    modele = "M4 compition"
    Annee = 2022
    def afficher_info():
        print(f"Marque : {Voiture.marque}")
        print(f"Modele : {Voiture.modele}")
        print(f"Annee : {Voiture.Annee}")
V1 = Voiture.afficher_info()