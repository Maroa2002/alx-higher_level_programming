-- lists the number of records with the same score
-- The result should display:
-- 1.the score
-- 2.the number of records for this score with the label number
-- The list should be sorted by the number of records (descending)

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;