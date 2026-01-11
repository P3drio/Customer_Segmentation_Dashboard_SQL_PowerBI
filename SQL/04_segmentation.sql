DROP VIEW IF EXISTS customer_segments;

CREATE VIEW customer_segments AS
SELECT 
    CustomerID,
    Frequency,
    Monetary,
    LastPurchaseDate,
    CASE
        WHEN Monetary >= 10000 AND Frequency >= 50 THEN 'High Value'
        WHEN Monetary >= 5000 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS Segment
FROM customer_metrics;
