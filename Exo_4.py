class Personne :
    nom = "Lemnaizi"
    prenom = "Walid"
    age = 21
    def sepresenter():
        print(f"Bonjour a tous je m'appelle {Personne.nom} {Personne.prenom} et j'ai {Personne.age}")


class Etudiant(Personne):
    matricule = "A1330....."
    def etudier():
        print(f"L'étudiant {Personne.prenom} {Personne.nom} (matricule: {Etudiant.matricule}) est en train d'étudier.")

P1 = Personne.sepresenter()
P2 = Etudiant.etudier()