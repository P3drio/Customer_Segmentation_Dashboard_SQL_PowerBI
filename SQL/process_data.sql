-- Clean raw data

DROP TABLE IF EXISTS online_retail_cleaned;

CREATE TABLE online_retail_cleaned AS
SELECT *
FROM online_retail_raw
WHERE Invoice NOT LIKE 'C%';

-- Customer summary aggregation

DROP TABLE IF EXISTS customer_summary;

CREATE TABLE customer_summary AS
SELECT CustomerID,
       COUNT(DISTINCT Invoice) AS total_orders,
       SUM(Quantity) AS total_quantity,
       SUM(Quantity * UnitPrice) AS total_spent
FROM online_retail_cleaned
GROUP BY CustomerID;


-- Add segmentation

ALTER TABLE customer_summary
ADD COLUMN segment TEXT;

UPDATE customer_summary
SET segment = CASE
    WHEN total_spent >= 1000 THEN 'High Value'
    WHEN total_spent >= 500 THEN 'Medium Value'
    ELSE 'Low Value'
END;