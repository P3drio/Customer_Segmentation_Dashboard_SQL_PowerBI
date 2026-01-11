DROP VIEW IF EXISTS customer_metrics;

CREATE VIEW customer_metrics AS
SELECT
    CustomerID,
    COUNT(DISTINCT Invoice) AS Frequency,
    SUM(TotalPrice) AS Monetary,
    MAX(InvoiceDate) AS LastPurchaseDate
FROM online_retail_clean
GROUP BY CustomerID