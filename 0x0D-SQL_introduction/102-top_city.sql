-- displays top 3 city temperatures
SELECT `city`, MAX(`value`) AS `top_temp`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `top_temp` DESC
LIMIT 3;
