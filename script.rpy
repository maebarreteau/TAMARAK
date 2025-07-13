# images 
image salle_dongeon = im.Scale("images/salle_dongeon.png", 1920, 1080)
image homme_cailloux = im.Scale("images/cailloux.png", 600, 800)
image livre_sort1 = im.Scale("images/item_5.png", 160, 160)
image bottes = im.Scale("images/item_13.png", 160, 160)
image castle = im.Scale("images/castle.png", 1920, 1080)
image dragon = im.Scale("images/dragon.png", 600, 800)
image game_over = im.Scale("images/Game_over1.png", 1920, 1080)


# characters 
define u = Character("Une voix rocailleuse")
define c = Character("Homme cailloux")
define d = Character("Dragon")

# Définition des positions personnalisées
transform midleft:
    xpos 0.3  # 0.0 = complètement à gauche, 0.5 = centre
    ypos 0.5
    xanchor 0.5
    yanchor 1.0

transform midright:
    xpos 0.7  # 1.0 = complètement à droite
    ypos 0.5
    xanchor 0.5
    yanchor 1.0

# objets 
default objet_choisi = None

# game over 
label game_over:
    scene black
    "Game Over"
    return



# Le jeu commence ici
label start:

    scene salle_dongeon

    u "Bienvenue à Tamarak, camarade"

    show homme_cailloux at center
    c "Oui, oui c'est à toi que je parle"
    c "Prêt pour la grande aventure ?"

    menu:
        "La grande quoi-":
            c "La grande aventure"
            c "Celle d'une vie"
            c "L'aventure quoi !"
            
    menu:
        "Dis moi en plus":
            c "Tu es à Tamarak, un royaume déchu, jadis glorieux il n'est plus, tu dois lui redonner sa renommé d'antan"
        "Non désolée, ça ne m'intéresse pas, je ne sais même pas ce que je fais là":
            c "Ce n'était pas une question, camarade"

    $ player_name = renpy.input("Comment t'appelles-tu d'ailleurs camarde ?")

    c "Attends [player_name], je dois aller chercher un truc attends moi"
    hide homme_cailloux
    "[player_name]" "..."

    show homme_cailloux at center 
    show livre_sort1 at midright
    show bottes at midleft

    c "Choisis-en un"
    
    menu:
        "Les bottes":
            $ objet_choisi = "bottes"
            hide livre_sort1
            c "Je mets ça dans ton inventaire"
            show bottes at top
        "Le livre de sort I":
            $ objet_choisi = "livre_sort1"
            hide bottes
            c "Je mets ça dans ton inventaire"
            show livre_sort1 at top

    c "Et voilà tu es fin prêt"
    c "Maintenant suis-moi"
    
    scene castle
    show homme_cailloux at center 

    if objet_choisi == "bottes":
        show bottes at top
    elif objet_choisi == "livre_sort1":
        show livre_sort1 at top

c "Ton voyage commence ici"
c "Suis le chemin vers le château et tu trouveras ta voie"
hide homme_cailloux


"Tu avances de quelques pas..."
d "Où penses-tu aller comme ça??"
show dragon at center 
d "Tu n'iras nulle part"

if objet_choisi == "bottes":
    "Tu essayes de t'enfuir en courant mais tes pieds s'embourbent dans le sol"
    jump game_over
    
elif objet_choisi == "livre_sort1":
    "Que vas-tu faire avec un livre ?"
    jump game_over

return

