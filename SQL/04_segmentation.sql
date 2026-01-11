DROP VIEW IF EXISTS customer_segments;

CREATE VIEW customer_segments AS
SELECT 
    CustomerID,
    Frequency,
    Monetary,
    LastPurchaseDate,
    CASE
        WHEN Monetary >= 1000 AND Frequency >= 10 THEN 'High Value'
        WHEN Monetary >= 150 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS Segment
FROM customer_metrics;

DROP TABLE IF EXISTS customer_summary;

CREATE TABLE customer_summary AS
SELECT *
FROM customer_segments;