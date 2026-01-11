-- 02_cleaning.sql
-- Clean data for analysis

-- Remove canceled invoices
DELETE FROM online_retail_clean
WHERE Invoice LIKE 'C%';

-- Remove invalid records
DELETE FROM online_retail_clean
WHERE CustomerID IS NULL
   OR Quantity <= 0
   OR UnitPrice <= 0;

-- Add total transaction value
ALTER TABLE online_retail_clean
ADD COLUMN TotalPrice REAL;

UPDATE online_retail_clean
SET TotalPrice = Quantity * UnitPrice;

-- Remove duplicates
DELETE FROM online_retail_clean
WHERE rowid NOT IN (
    SELECT MIN(rowid)
    FROM online_retail_clean
    GROUP BY
        Invoice,
        StockCode,
        Quantity,
        InvoiceDate,
        UnitPrice,
        CustomerID
);