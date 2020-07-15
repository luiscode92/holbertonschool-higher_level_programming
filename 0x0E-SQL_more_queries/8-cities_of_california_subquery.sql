-- list the cities in california that can be found in the database
SELECT id, name FROM cities WHERE state_id =
	(SELECT id FROM STATE WHERE name = 'California');
