"""
Opgave: Mapmatching af uheld vha. af Dansk Adresse Registers RESTful service.

1. Skriv en funktion, der henter data ud i en dictionary: {'id': int, 'x': float, 'y': float }
2. Skriv en funktion der henter datasæt fra DAWA på baggrund af dette koordinat.
3. Udvælg hvilke data vi vil gemme til videre brug.

Uheldsdata tabellen skal opdateres med to tre nye felter:

ALTER table uheldsdata
add column vej_geom geometry(Point, 25832),
add column komkode varchar,
add column vejkode varchar

"""


def main():
    pass

if __name__ == "__main__":
    main()
