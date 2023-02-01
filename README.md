# Rush-Me-Daddy
Algoritmen en Heuristieken groepje met Daan, Hugo &amp; Sarah  

## Rush Hour Case
Rush Hour is een ogenschijnlijk eenvoudig puzzeltje met een verrassend uitdagend karakter. In een veld van 6 hoog en 6 breed staat een rode auto, de jouwe, en die moet naar de uitgang die recht voor je ligt. Maar andere voertuigen versperren de weg; auto’s van twee eenheden lang en trucks van drie eenheden lang, die alleen in hun rijrichting bewogen mogen worden. Ze mogen niet draaien. De opdracht is: beweeg je auto naar buiten en schrijf een computerprogramma om dat voor je te doen.  

![Rushhour Logo](https://github.com/hugovansteenis/Rush-Me-Daddy/blob/main/rushhour_logo.jpeg)

Bron: [Rush Hour](https://ah.proglab.nl/cases/rush-hour)

## Input en Usage
*<b style="color:red">Let op! Voor Mac gebruikers geldt bij alle command line argumenten dat python3 gebruikt moet worden in plaats van python.</b>*

Standaard input:  
```
python main.py [gameboardfile] [algorithm]
```

Voor alle gameboard bestanden kan je navigeren naar de data folder. Er is keuze uit 6x6, 9x9, en 12x12 grids. Ook zijn ze gesorteerd op moeilijkheidsgraad waarbij de makkelijkste de eerste in de lijst zijn.   

Om het spel zelf te spelen kan je het algoritme weglaten. Vervolgens kan je een auto bewegen door de letter gevolgd door de richting te typen. Bijvoorbeeld: `[A -1]` kiest auto A en beweegt deze 1 stap naar links. En `[B -1]` kiest auto B en beweegt deze 1 stap omhoog.

Voor elk algoritme geldt dat er standaard een output CSV bestand wordt gegenereerd. Er kan ook een experiment CSV bestand worden gegenereerd wat per algoritme extra data biedt. Hieronder zijn alle command line argumenten uitgelegd per algoritme en ook hoe je de resultaten kan reproduceren.  

## Repository Overview
Alle code staat in de `code` folder. Deze is onderverdeeld in algorithms, classes, en visualisation. Er bestaan drie classes.

De `car` class die informatie over de auto objecten heeft, de `game` class die zorgt dat het spel gespeeld kan worden, auto's kunnen bewegen en checkt of het spel al gewonnen is en de `grid` class die het board maakt.

In `algorithms` staan alle 5 algoritmes die je kan gebruiken om de game op te lossen.

In de `data` folder staan de gebruikte game boards. In de `experiments` folder staan alle experimenten per algoritme. In de `results` folder staan de resultaten voor elk algoritme zoals visualisaties, een output CSV bestand met alle gemaakt moves voor de game en animaties van de moves en een experiment CSV bestand aangeduid met 'exp'. In de main folder staan de README en benodigde libraries. Verder worden vanuit `main.py` alle algoritmes aangeroepen en kan je de game starten.
<br></br>
## Random
De benodigde input om de volgende resultaten te krijgen is: 
```
python main.py Rushhour6x6_1.csv random_exp
```
Random houdt in dat er willekeurige moves worden gezet tot een oplossing bereikt is.

![6x6_1_exp_graph.png](https://github.com/hugovansteenis/Rush-Me-Daddy/blob/main/results/random/6x6_1_exp_graph.png)
<br></br>
## Greedy
Input:
```
python main.py Rushhour6x6_2.csv greedy_exp
```
Greedy houdt in dat er twee heuristieken worden toegepast. Als eerste wordt er gekeken of de rode auto 1 zet naar rechts kan, als dat niet kan wordt er gekeken of er een blokkade voor de rode auto is die 1 zet omlaag kan, als dat niet kan wordt er een willekeurige zet uitgevoerd.
![6x6_2_exp_graph.png](https://github.com/hugovansteenis/Rush-Me-Daddy/blob/main/results/greedy/6x6_2_exp_graph.png)
<br></br>
## Breadth First
Input:
```
python main.py Rushhour6x6_1.csv breadth_exp
```
Breadth First en Depth First in vergelijking tot random waarbij de eerste en de beste oplossing wordt aangenomen, zijn breadth first en depth first exhaustive. Dit betekent dat alle mogelijke states worden afgegaan wat dus de beste oplossing biedt. 
![6x6_1_exp_graph.png](https://github.com/hugovansteenis/Rush-Me-Daddy/blob/main/results/breadth/graph_breadth_1.png)
<br></br>
## Depth First
Input:
```
python main.py Rushhour6x6_1.csv depth_exp
```

![6x6_1_exp_graph.png](https://github.com/hugovansteenis/Rush-Me-Daddy/blob/main/results/depth/graph_depth_1.png)
<br></br>
## Beam Search
Input:
```
python main.py Rushhour6x6_2.csv beam_exp
```
Beam Search is een compromis en kiest steeds de top [`w`] aantal states uit waarbij `w` gekozen kan worden. Dit geeft niet altijd de beste oplossing maar kost wel minder geheugen dan breadth first search.
![6x6_1_exp_graph.png](https://github.com/hugovansteenis/Rush-Me-Daddy/blob/main/results/beam/graph_beam_1.png)
