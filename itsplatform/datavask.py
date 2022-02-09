'''Vi skal nu prøve at lave datavask af en datasæt ved hjælp af Pandas i python.

Vi skal importere filen bil_import_2022.csv til en pandas dataframe.

Der skal dannes et overblik over dataene identificier problemer med fdaa
    Få et overblik over dine data, lav forskellige SELECT forespørgsler (queries)
        Bør datatyperne være anderledes end varchar?
        Hvordan er felterne/kollonernes indhold?
    Lav en ny tabel, bil, på baggrund af public.bil_import men hvor datatyperne er sat korrekt.
        Der mangler en bil, indsæt denne i public.bil:

        Id: 1923, Manufactor: Kia, Model: Yaris, Drivmiddel: El, KmPrAar: 7500, Årgang: 2016

        Hvor mange forskellige bilmærker har vi før og efter vask?
    Hvilke biler har kørt mindst 20.000 km i kører på benzin (type=2)?
        Hvor mange biler er det?
        Hvor langt har de kørt ialt?
    Hvad er 10, 25 og 75 % fraktilen for kørte km.
        Hvordan ser det ud indenfor de enkelte bilmærker
'''