# Rush-Me-Daddy
Algoritmen en Heuristieken groepje met Daan, Hugo &amp; Sarah  

## Rush Hour Case
Rush Hour is een ogenschijnlijk eenvoudig puzzeltje met een verrassend uitdagend karakter. In een veld van 6 hoog en 6 breed staat een rode auto, de jouwe, en die moet naar de uitgang die recht voor je ligt. Maar andere voertuigen versperren de weg; auto’s van twee eenheden lang en trucks van drie eenheden lang, die alleen in hun rijrichting bewogen mogen worden. Ze mogen niet draaien. De opdracht is: beweeg je auto naar buiten en schrijf een computerprogramma om dat voor je te doen.

Bron: [Rush Hour](https://ah.proglab.nl/cases/rush-hour)

## Input
*Let op! Voor Mac gebruikers geldt bij alle command line argumenten dat python3 gebruikt moet worden in plaats van python.*

Standaard input:  
```
python main.py [gameboardfile] [algorithm]
```

Voor alle gameboard bestanden kan je navigeren naar de data folder. Er is keuze uit 6x6, 9x9, en 12x12 grids. Ook zijn ze gesorteerd op moeilijkheidsgraad waarbij de makkelijkste de eerste in de lijst zijn.   

Om het spel zelf te spelen kan je het algoritme weglaten. Vervolgens kan je een auto bewegen door de letter gevolgd door de richting te typen. Bijvoorbeeld: `[A -1]` kiest auto A en beweegt deze 1 stap naar links. En `[B -1]` kiest auto B en beweegt deze 1 stap omhoog.

Voor elk algoritme geldt dat er standaard een output CSV bestand wordt gegenereerd. Er kan ook een experiment CSV bestand worden gegenereerd wat per algoritme extra data biedt. Hieronder zijn alle command line argumenten uitgelegd per algoritme en ook hoe je de resultaten kan reproduceren.
<br></br>
## Random
De benodigde input om de volgende resultaten te krijgen is: 
```
python main.py Rushhour6x6_1.csv random_exp
```
![6x6_1_exp_graph.png](https://github.com/hugovansteenis/Rush-Me-Daddy/blob/main/results/random/6x6_1_exp_graph.png)
<br></br>
## Greedy
![6x6_2_exp_graph.png](https://github.com/hugovansteenis/Rush-Me-Daddy/blob/main/results/greedy/6x6_2_exp_graph.png)
<br></br>
## Breadth First

<br></br>
## Depth First

<br></br>
## Beam Search


