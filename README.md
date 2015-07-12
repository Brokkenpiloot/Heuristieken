# Heuristieken
Case: RushHour

game.py bevat de implementatie van het spel Rush Hour en de implementatie van het algoritme die dit spel op kan lossen.

Het spel is geimplementeerd aan de hand van twee classes: Board en Car. 
Om het algoritme te kunnen runnen moet een Board, een bord, met afmetingen en win coordinaten geleverd worden.
Vervolgens moet dit bord met auto's gevuld worden met lengte, orientatie en begincoordinaten.
Onderaan de file zijn 7 preset borden meegeleverd.
Unieke borden kunnen handmatig ingevoerd worden maar is door de complexiteit van de code een heus karwei. Aangeraden wordt derhalve om de preset borden te hanteren.

Om dit programma te kunnen runnen dient eerst matplotlib geinstaleerd te worden via matplotlib.org. Hier vind men ook uitgebreide documentatie en guides.

Het algoritme wordt op de volgende manier gerund: timer(game, aantal loops, maximale diepte oplossing). Bij het runnen wordt de gebruiker gevraagd om het aantal oplossingen dat het algoritme dient te vinden in te voeren. 
Aan de hand hiervan wordt gedefinieerd of het Random algoritme wordt gebruikt (bij 1 oplossing), dan wel het Self-improving algoritme (bij meer dan 1 oplossing).



