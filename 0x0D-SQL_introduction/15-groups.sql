-- lists number of records with same score in table `second_table`
-- orderd by number desc
SELECT `score`, COUNT(*) AS `number` FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC
