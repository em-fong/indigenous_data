/*Emily Fong, Assignment 4

Data source:
http://www.census.gov/geo/maps-data/data/gazetteer2010.html
"American Indian/Alaska Native/Native Hawaiian Areas"
 */

DROP TABLE IF EXISTS native;

CREATE TABLE native (
  geoID integer,
  ansiCode integer,
  name text PRIMARY KEY,
  pop2010 integer,
  housingCount2010 integer,
  land_meters integer,
  water_meters integer,
  land_sqmi integer,
  water_sqmi integer,
  latitude real,
  longitude real
);
