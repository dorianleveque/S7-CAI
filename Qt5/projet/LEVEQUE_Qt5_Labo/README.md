# Installation
Pour profiter de cette application, il suffit de dézipper l'archive du projet et de lancer le mainwindow py avec python dans sa version 3.
<b> 
> /!\ Le projet utilise des modules qui doivent être installés au préalable.
</b>

    > Liste des modules utilisés dans le projet:
    - py Qt5
    - re (pour les expressions régulières) (normalement déjà installé avec python)


# Utilisation du logiciel
## Qu'est ce que c'est ? 
Ce logiciel est un éditeur graphique d'image SVG. Avec ce logiciel, vous êtes capable dessiner des lignes, des rectangles, des cercles, des ellipses, des polygones, d'insérer des textes et de pouvoir sauvegarder votre dessin dans le format SVG.

## Quels sont les types de sauvegarde ?
Vous pouvez sauvegarder vos dessins en sauvegardant dans deux différents formats ! Le JSON et le SVG.
/!\ Le SVG ne conserve malheureusement pas toutes les propriétés des figures du dessin, des propriétés propres à Qt ne sont pas exportées.

    Pourquoi le SVG ?
    > Le SVG est un format de fichier qui permet de conserver une image de manière vectorielle. Il me semblait judicieux d'utiliser ce format pour sauvegarder les dessins. 
    (Mais également pour expérimenté, puisque j'ai découvert que Qt le supportait et que je l'avais jamais utilisé)

    Malheureusement, je me suis rendu compte trop tard dans le développement que certaine propriété de Qt n'était pas exportée.J'ai donc laissé le support du SVG en avertissant l'utilisateur et mis en place une sauvegarde de fichier en JSON.

# Comment tracé ?
- Pour les tracés de trait, de rectangle et d'ellipse, maintenir le clic gauche tout en traçant la figure désirée.
- Pour les tracés du polygone, cliquer pour placer un point et fermer la figure pour qu'elle apparaisse.
- Pour le placement de texte, cliquer dans la zone de dessin pour placer votre futur texte. Une boîte de dialogue apparaît pour saisir votre texte.


## Raccourcis clavier
L'ensemble des raccourcis claviers sont listés dans les menus du logiciel.

D'autres raccourcis existent. 

- Pour dessiner un carré: sélectionner l'outil de dessin rectangle. Commencé à tracer (maintenir le clic gauche) tout en maintenant la touche SHIFT.

- Pour dessiner un cercle: sélectionner l'outil de dessin ellipse. Commencé à tracer (maintenir le clic gauche) tout en maintenant la touche SHIFT.


# Problèmes rencontrés
Lors du développement, j'ai rencontré de nombreux problèmes. Certains ont été résolus, d'autres sont encore présents dans cette version du logiciel.
>Le problème le plus visible vient de la traduction. Ayant un peu d'expérience avec Qt, je ne métais jamais penché sur la traduction dans un logiciel et je souhaitais utiliser ce projet pour me perfectionner. J'utilise le logiciel QtLinguist pour les traductions qui me génère un fichier .Qm. Je charge bien le fichier, certains menus sont traduits mais d'autres restes en anglais pour des raisons que j'ignore.

> Un autre souci est pour la sauvegarde de fichier. En effect j'ai d'abord souhaité supporter le SVG pensant que je pourrais tout restituer. Malheureusement, ce n'est que vers la fin que je me suis rendu compte que seules les formes et les couleurs l'étaient mais pas lorsque l'on rajoute des remplissages spéciaux.Ainsi j'ai également fait la sauvegarde "classique" vue en cours mais je n'ai pas au le temps de la finir. De plus je ne voyais pas comment récupérer les points d'un polygone déjà tracé.