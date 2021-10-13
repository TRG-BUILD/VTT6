"""
En stor del af trafiksikkerhedsarbejdet er arbejdet med uheldsdata. Uheldsdata fra Politiets registreringer kan findes i vejman.dk.

Med udgangspunkt i uheld fra 2008-2014, er der genereret et datasæt, hvor alder og dato er randomiseret, således de ikke er personhenførbare. Datasættet findes i uheld_fake.xlsx.

I filen uheld_fake.xls er færdselsuheld opgjort på egenpart, dato og alder.

    Indlæs datasættet i en pandas dataframe

        Dan jer et overblik over datasættet. Brug f.eks. funktionerne describe og dtypes.

    Find det totale antal uheld

        Hvor mange uheld var der i 2009?

        Hvordan var de fordelt på egenpart i 2009?

    Lav et diagram der viser udviklingen over det totale antal uheld over tid.

    Grupper uheldene i aldersintervallerne: 0-15, 16-17, 18-24, 25-34, 35-44, 45-54, 55-64, 65-74, 75-84 og 85+

        Hvor mange uheld er der i hvert interval?

        Ekstraopgave: Lav grupperingen ved hjælp af en liste med intervallerne og en for-løkke, der løber gennem listen.

    Lav en ny dataframe som indeholder alle uheld hvor egenpart er “Bike”.

        Gentag spørgsmål 3 for den nye dataframe.

    Hvad er 10 % og 90 % fraktilen for alderen i “Bike”

    Lav et histogram for hvert år i dataframen for “Bike”.

        Ekstraopgave: Lav en for-løkke der laver og gemmer histogrammerne for hvert år.
"""