SELECT * FROM pinball_data;

ALTER TABLE pinball_data
ADD COLUMN first_five TEXT
AFTER opdb_id_;

ALTER TABLE pinball_data
ADD COLUMN year_ TEXT
AFTER manufacture_date;

UPDATE pinball_data
SET first_five = SUBSTRING(opdb_id_,1,5);

UPDATE pinball_data
SET year_ = SUBSTRING(manufacture_date,1,4);

-- see which manufacturers dominated the market 
SELECT manufacturer_name, COUNT(manufacturer_name) as count
FROM pinball_data
GROUP BY manufacturer_name
HAVING count >= 100
ORDER BY count DESC;

-- 'Gottlieb',
-- 'Williams',
-- 'Bally',
-- 'Stern'


SELECT manufacturer_name, year_, COUNT(manufacturer_name) as count
FROM pinball_data
WHERE manufacturer_name IN ('Gottlieb', 'Williams', 'Bally', 'Stern')
GROUP BY manufacturer_name, year_
ORDER BY year_;

CREATE VIEW top_four AS 
(SELECT *
FROM pinball_data
WHERE manufacturer_name IN ('Gottlieb', 'Williams', 'Bally', 'Stern'));

SELECT COUNT(*)
FROM top_four;

SELECT manufacturer_name, COUNT(manufacturer_name) as count
FROM top_four
GROUP BY manufacturer_name;



-- using binary to do case sensitive string matching
CREATE VIEW jd AS 
(SELECT *
FROM top_four AS tf
LEFT JOIN group_data  AS gd
ON CAST(tf.first_five AS BINARY) = CAST(gd.opdb_id AS BINARY));

SELECT count(*)
FROM jd;

SELECT manufacturer_name, COUNT(manufacturer_name) as count
FROM jd
GROUP BY manufacturer_name;

SELECT group_name, COUNT(group_name) as count
FROM jd
GROUP BY group_name
ORDER BY count DESC;

SELECT *
FROM jd
WHERE group_name LIKE 'Harley%';