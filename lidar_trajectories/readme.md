# Lidar data

LiDAR – Light Detection and Ranging

Trafikforskningsgruppen råder over en LiDAR til opsætning for at registrere trafik. For at behandle lidar data, har gruppen fået skrevet et [program](https://github.com/mihsamusev/pylidartracker) til behandling af disse.

I denne opgave har I fået et output fra pylidartracker, der har behandlet lidar data I krydset ved Create [Rendburgsgade/Nyhavnsgade](https://www.openstreetmap.org/#map=19/57.04797/9.92835)


---

1. Indlæs config.json, lav variabler som du skal bruge senere
2. Indlæs ortofoto og plot det på en måde hvor x og y er I UTM koordinatsystem
3. Plot detektions region:
* a. plot det_region I separate akser
* b. Udfyld det_region_to_utm i helpers.py for at transformere regionen til koordinatsystemet euref89-utm32
4. Plot den transformerede region oven på ortophoto
5. Plot tracks:
* a. Udfyld data_to_tracks i helpers.py, hvordan kan du teste at det virker rigtig?
* b. Plot alle tracks i nye akser, ser det ok ud?
* c. Udfyld track_to_utm at konvertere en track til rigtig koordinatsystem, test med en plot
* d. Plot transformerede tracks oven på ortophoto 
