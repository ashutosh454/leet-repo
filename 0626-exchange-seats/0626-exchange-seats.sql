SELECT 
    id,
    CASE 
        -- For odd IDs, get the next student (if last row, fallback to current student)
        WHEN id % 2 = 1 THEN COALESCE(LEAD(student) OVER (ORDER BY id), student)
        -- For even IDs, get the previous student
        ELSE LAG(student) OVER (ORDER BY id)
    END AS student
FROM Seat;