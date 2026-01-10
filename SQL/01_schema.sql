-- 01_schema.sql
-- Working table from raw retail data

DROP TABLE IF EXISTS online_retail_clean;

CREATE TABLE online_retail_clean AS
SELECT
    Invoice,
    StockCode,
    Description,
    Quantity,
    InvoiceDate,
    Price,
    "Customer ID" AS CustomerID,
    Country
FROM online_retail_raw;