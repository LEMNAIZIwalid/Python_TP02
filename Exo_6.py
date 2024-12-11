class Rectangle :
    largeur = 5
    hauteur = 3
    def calculer_surface():
        return "La surface de rectangle est : "+str(Rectangle.largeur * Rectangle.hauteur )
    def calculer_perimetre():
        return "Le perimetre de rectangle est : "+str(( Rectangle.largeur*2 )+( Rectangle.hauteur*2 ))

Rectangle_surface = Rectangle.calculer_surface()
print(Rectangle_surface)

Rectangle_perimetre = Rectangle.calculer_perimetre()
print(Rectangle_perimetre )