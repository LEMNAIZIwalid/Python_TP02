class Personne :
    nom = "Lemnaizi"
    prenom = "Walid"
    age = 21
    liste_amis = []

    def sepresenter():
        print(f"Bonjour a tous je m'appelle {Personne.nom} {Personne.prenom} et j'ai {Personne.age}")
    
    def ajouter_ami(ami):
        Personne.liste_amis.append(ami)
    
    def afficher_ami():
        for i in Personne.liste_amis :
            print(i)

class Etudiant(Personne):
    matricule = "A1330....."
    def etudier():
        print(f"L'étudiant {Personne.prenom} {Personne.nom} (matricule: {Etudiant.matricule}) est en train d'étudier.")

P1 = Personne.sepresenter()
P2 = Etudiant.etudier()

P3 = Personne.ajouter_ami("Amine")
P3 = Personne.ajouter_ami("Aya")
P3 = Personne.ajouter_ami("Issam")
P3 = Personne.ajouter_ami("Laila")

P3 = Personne.afficher_ami()