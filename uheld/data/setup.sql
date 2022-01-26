/*
   Opret tilfældige punkter på vejnettet til uheldsdata

   Kode til at skabe falske punter på vejnettet til uheldsdata

*/


-- tilføj primary key og geometry kollone

ALTER table uheldsdata_import2
ADD COLUMN geom geometry(Point,25832),
ADD COLUMN id serial;
ADD PRIMARY KEY(id);



--CREATE TABLE RANDOM_POINTS AS
DROP  table random_points;
create table random_points as	
SELECT
	highway,
	osm_id,
	cycleway,
	surface,
	length,
	st_transform(geom, 25832) as geom
FROM
	(
		SELECT
			highway,
		cycleway,
		    osm_id,
			surface,
			ST_length(WAY) AS length,
		    (ST_dump(ST_generatepoints(ST_buffer(way,	3), 5))).geom AS geom
		FROM public.planet_osm_line
		WHERE ST_LENGTH(WAY) > 200
			AND ((( highway = 'secondary' or highway = 'tertiary') and cycleway is not null) or highway = 'residential')
	) as foo order by random() limit 100000 -- just a higher number than uheldsdata_import rows

-- add id to random_points
ALTER table random_points
ADD COLUMN id serial;

-- Update by joining tables
UPDATE uheldsdata_import2 SET geom = r.geom,
x = replace(round(st_x(r.geom)::numeric,2)::text, '.', ','),
y = replace(round(st_y(r.geom)::numeric,2)::text, '.', ',')
FROM random_points r where uheldsdata_import2.id = r.id


UPDATE uheldsdata_import2 SET
x = replace(round(st_x(geom)::numeric,2)::text, '.', ','),
y = replace(round(st_y(geom)::numeric,2)::text, '.', ',')


select egenpart, dato, alder::varchar, x, y  from uheldsdata_import2 order by id

ALTER TABLE uheldsdata_import
RENAME TO uheldsdata_import2

	