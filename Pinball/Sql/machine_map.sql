SELECT count(*)
FROM all_machines;

SELECT count(*)
FROM all_regions;

CREATE VIEW machine_loc AS 
(SELECT *
FROM all_machines AS am
INNER JOIN all_regions AS ar
ON am.location_id = ar.loc_id);

SELECT *
FROM machine_loc;

SELECT country, count(country) AS count
FROM machine_loc
GROUP BY country
ORDER BY count DESC;
-- 'US', USA
-- 'CA', Canada
-- 'AU', Australia
-- 'FI', Finland
-- 'GB', Great Britain
-- 'JP', Japan
-- 'UM', 


SELECT *
FROM machine_loc
WHERE country = 'UM';

UPDATE machine_loc
SET country = 'US'
WHERE country = 'UM';

SELECT zip, count(zip) as count
FROM machine_loc
WHERE country = 'US'
GROUP BY zip
ORDER BY count DESC;

SELECT state, count(state) as count
FROM machine_loc
WHERE country = 'US'
GROUP BY state
ORDER BY count DESC;



