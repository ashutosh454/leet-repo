WITH RankedPrices AS (
    -- Step 1: Find the latest price change on or before 2019-08-16 per product
    SELECT 
        product_id,
        new_price AS price,
        ROW_NUMBER() OVER (
            PARTITION BY product_id 
            ORDER BY change_date DESC
        ) AS rnk
    FROM Products
    WHERE change_date <= '2019-08-16'
)
-- Step 2: Combine products with price changes and products that keep default price 10
SELECT 
    p.product_id,
    COALESCE(r.price, 10) AS price
FROM (SELECT DISTINCT product_id FROM Products) p
LEFT JOIN RankedPrices r
       ON p.product_id = r.product_id 
      AND r.rnk = 1;