# Sample Complex SQL Questions and Queries

## 1. Find customers who have spent more than the average customer spending
**Question:** Which customers have spent more than the average total spending across all customers?

```sql
SELECT c.CustomerId, c.FirstName, c.LastName, SUM(i.Total) as TotalSpent
FROM Customer c
JOIN Invoice i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId, c.FirstName, c.LastName
HAVING SUM(i.Total) > (
    SELECT AVG(customer_total) 
    FROM (
        SELECT SUM(Total) as customer_total 
        FROM Invoice 
        GROUP BY CustomerId
    )
)
ORDER BY TotalSpent DESC;
```

## 2. Find artists with albums in multiple genres
**Question:** Which artists have released albums that span across 3 or more different genres?

```sql
SELECT ar.Name as ArtistName, COUNT(DISTINCT g.GenreId) as GenreCount
FROM Artist ar
JOIN Album al ON ar.ArtistId = al.ArtistId
JOIN Track t ON al.AlbumId = t.AlbumId
JOIN Genre g ON t.GenreId = g.GenreId
GROUP BY ar.ArtistId, ar.Name
HAVING COUNT(DISTINCT g.GenreId) >= 3
ORDER BY GenreCount DESC;
```

## 3. Monthly revenue trend with year-over-year comparison
**Question:** Show monthly revenue for each year with percentage change from the previous year?

```sql
WITH MonthlyRevenue AS (
    SELECT 
        strftime('%Y', InvoiceDate) as Year,
        strftime('%m', InvoiceDate) as Month,
        SUM(Total) as Revenue
    FROM Invoice
    GROUP BY strftime('%Y', InvoiceDate), strftime('%m', InvoiceDate)
)
SELECT 
    Year,
    Month,
    Revenue,
    LAG(Revenue) OVER (PARTITION BY Month ORDER BY Year) as PrevYearRevenue,
    ROUND(
        ((Revenue - LAG(Revenue) OVER (PARTITION BY Month ORDER BY Year)) / 
         LAG(Revenue) OVER (PARTITION BY Month ORDER BY Year)) * 100, 2
    ) as YoYGrowthPercent
FROM MonthlyRevenue
ORDER BY Year, Month;
```

## 4. Find the longest album by total duration
**Question:** Which album has the longest total playing time and what is its duration in hours and minutes?

```sql
SELECT 
    al.Title as AlbumTitle,
    ar.Name as ArtistName,
    COUNT(t.TrackId) as TrackCount,
    SUM(t.Milliseconds) as TotalMilliseconds,
    ROUND(SUM(t.Milliseconds) / 1000.0 / 60.0, 2) as TotalMinutes,
    ROUND(SUM(t.Milliseconds) / 1000.0 / 3600.0, 2) as TotalHours
FROM Album al
JOIN Artist ar ON al.ArtistId = ar.ArtistId
JOIN Track t ON al.AlbumId = t.AlbumId
GROUP BY al.AlbumId, al.Title, ar.Name
ORDER BY TotalMilliseconds DESC
LIMIT 1;
```

## 5. Customer purchase patterns by day of week
**Question:** What are the purchasing patterns of customers by day of the week, showing average order value and frequency?

```sql
SELECT 
    CASE strftime('%w', InvoiceDate)
        WHEN '0' THEN 'Sunday'
        WHEN '1' THEN 'Monday'
        WHEN '2' THEN 'Tuesday'
        WHEN '3' THEN 'Wednesday'
        WHEN '4' THEN 'Thursday'
        WHEN '5' THEN 'Friday'
        WHEN '6' THEN 'Saturday'
    END as DayOfWeek,
    COUNT(*) as OrderCount,
    ROUND(AVG(Total), 2) as AvgOrderValue,
    ROUND(SUM(Total), 2) as TotalRevenue,
    COUNT(DISTINCT CustomerId) as UniqueCustomers
FROM Invoice
GROUP BY strftime('%w', InvoiceDate)
ORDER BY strftime('%w', InvoiceDate);
```

## 6. Employees with highest sales performance
**Question:** Rank employees by their sales performance including total sales, number of customers served, and average deal size?

```sql
SELECT 
    e.FirstName || ' ' || e.LastName as EmployeeName,
    e.Title,
    COUNT(DISTINCT i.CustomerId) as CustomersServed,
    COUNT(i.InvoiceId) as TotalOrders,
    ROUND(SUM(i.Total), 2) as TotalSales,
    ROUND(AVG(i.Total), 2) as AvgOrderValue,
    RANK() OVER (ORDER BY SUM(i.Total) DESC) as SalesRank
FROM Employee e
JOIN Customer c ON e.EmployeeId = c.SupportRepId
JOIN Invoice i ON c.CustomerId = i.CustomerId
GROUP BY e.EmployeeId, e.FirstName, e.LastName, e.Title
ORDER BY TotalSales DESC;
```

## 7. Genre popularity by country
**Question:** What are the top 3 most popular genres in each country based on total sales?

```sql
WITH GenreCountrySales AS (
    SELECT 
        c.Country,
        g.Name as GenreName,
        SUM(il.UnitPrice * il.Quantity) as TotalSales,
        ROW_NUMBER() OVER (PARTITION BY c.Country ORDER BY SUM(il.UnitPrice * il.Quantity) DESC) as Rank
    FROM Customer c
    JOIN Invoice i ON c.CustomerId = i.CustomerId
    JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId
    JOIN Track t ON il.TrackId = t.TrackId
    JOIN Genre g ON t.GenreId = g.GenreId
    GROUP BY c.Country, g.GenreId, g.Name
)
SELECT Country, GenreName, ROUND(TotalSales, 2) as TotalSales, Rank
FROM GenreCountrySales
WHERE Rank <= 3
ORDER BY Country, Rank;
```

## 8. Tracks that appear on multiple albums
**Question:** Find tracks that have the same name but appear on different albums (potential duplicates or covers)?

```sql
SELECT 
    t1.Name as TrackName,
    COUNT(DISTINCT t1.AlbumId) as AlbumCount,
    GROUP_CONCAT(DISTINCT al.Title || ' by ' || ar.Name, '; ') as Albums
FROM Track t1
JOIN Album al ON t1.AlbumId = al.AlbumId
JOIN Artist ar ON al.ArtistId = ar.ArtistId
WHERE t1.Name IN (
    SELECT Name 
    FROM Track 
    GROUP BY Name 
    HAVING COUNT(DISTINCT AlbumId) > 1
)
GROUP BY t1.Name
HAVING COUNT(DISTINCT t1.AlbumId) > 1
ORDER BY AlbumCount DESC, t1.Name;
```

## 9. Customer lifetime value analysis
**Question:** Calculate customer lifetime value, purchase frequency, and identify high-value customers?

```sql
WITH CustomerMetrics AS (
    SELECT 
        c.CustomerId,
        c.FirstName || ' ' || c.LastName as CustomerName,
        c.Country,
        COUNT(i.InvoiceId) as TotalOrders,
        SUM(i.Total) as TotalSpent,
        AVG(i.Total) as AvgOrderValue,
        MIN(i.InvoiceDate) as FirstPurchase,
        MAX(i.InvoiceDate) as LastPurchase,
        ROUND(JULIANDAY(MAX(i.InvoiceDate)) - JULIANDAY(MIN(i.InvoiceDate)), 0) as CustomerLifespanDays
    FROM Customer c
    JOIN Invoice i ON c.CustomerId = i.CustomerId
    GROUP BY c.CustomerId, c.FirstName, c.LastName, c.Country
)
SELECT 
    CustomerName,
    Country,
    TotalOrders,
    ROUND(TotalSpent, 2) as TotalSpent,
    ROUND(AvgOrderValue, 2) as AvgOrderValue,
    CustomerLifespanDays,
    CASE 
        WHEN CustomerLifespanDays > 0 THEN ROUND(TotalOrders * 1.0 / (CustomerLifespanDays / 365.0), 2)
        ELSE TotalOrders
    END as OrdersPerYear,
    CASE 
        WHEN TotalSpent >= 45 THEN 'High Value'
        WHEN TotalSpent >= 25 THEN 'Medium Value'
        ELSE 'Low Value'
    END as CustomerSegment
FROM CustomerMetrics
ORDER BY TotalSpent DESC;
```

## 10. Album completion rate by customers
**Question:** What percentage of each album has been purchased by customers (track completion rate)?

```sql
WITH AlbumTrackCounts AS (
    SELECT AlbumId, COUNT(*) as TotalTracks
    FROM Track
    GROUP BY AlbumId
),
CustomerAlbumPurchases AS (
    SELECT 
        i.CustomerId,
        t.AlbumId,
        COUNT(DISTINCT t.TrackId) as PurchasedTracks
    FROM Invoice i
    JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId
    JOIN Track t ON il.TrackId = t.TrackId
    GROUP BY i.CustomerId, t.AlbumId
)
SELECT 
    c.FirstName || ' ' || c.LastName as CustomerName,
    al.Title as AlbumTitle,
    ar.Name as ArtistName,
    cap.PurchasedTracks,
    atc.TotalTracks,
    ROUND((cap.PurchasedTracks * 100.0 / atc.TotalTracks), 2) as CompletionPercentage
FROM CustomerAlbumPurchases cap
JOIN Customer c ON cap.CustomerId = c.CustomerId
JOIN Album al ON cap.AlbumId = al.AlbumId
JOIN Artist ar ON al.ArtistId = ar.ArtistId
JOIN AlbumTrackCounts atc ON cap.AlbumId = atc.AlbumId
WHERE cap.PurchasedTracks >= atc.TotalTracks * 0.5  -- At least 50% completion
ORDER BY CompletionPercentage DESC, CustomerName;
```

## 11. Revenue contribution by media type
**Question:** What is the revenue contribution and growth trend of each media type over time?

```sql
WITH MediaTypeRevenue AS (
    SELECT 
        mt.Name as MediaType,
        strftime('%Y', i.InvoiceDate) as Year,
        SUM(il.UnitPrice * il.Quantity) as Revenue
    FROM MediaType mt
    JOIN Track t ON mt.MediaTypeId = t.MediaTypeId
    JOIN InvoiceLine il ON t.TrackId = il.TrackId
    JOIN Invoice i ON il.InvoiceId = i.InvoiceId
    GROUP BY mt.MediaTypeId, mt.Name, strftime('%Y', i.InvoiceDate)
)
SELECT 
    MediaType,
    Year,
    ROUND(Revenue, 2) as Revenue,
    ROUND(Revenue * 100.0 / SUM(Revenue) OVER (PARTITION BY Year), 2) as MarketSharePercent,
    ROUND(
        ((Revenue - LAG(Revenue) OVER (PARTITION BY MediaType ORDER BY Year)) / 
         LAG(Revenue) OVER (PARTITION BY MediaType ORDER BY Year)) * 100, 2
    ) as YoYGrowthPercent
FROM MediaTypeRevenue
ORDER BY Year, Revenue DESC;
```

## 12. Cross-selling opportunities
**Question:** Which genres are frequently bought together by the same customers?

```sql
WITH CustomerGenres AS (
    SELECT DISTINCT
        i.CustomerId,
        g.GenreId,
        g.Name as GenreName
    FROM Invoice i
    JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId
    JOIN Track t ON il.TrackId = t.TrackId
    JOIN Genre g ON t.GenreId = g.GenreId
)
SELECT 
    g1.GenreName as Genre1,
    g2.GenreName as Genre2,
    COUNT(*) as CoOccurrences,
    ROUND(COUNT(*) * 100.0 / (
        SELECT COUNT(DISTINCT CustomerId) FROM CustomerGenres WHERE GenreId = g1.GenreId
    ), 2) as CrossSellRate
FROM CustomerGenres g1
JOIN CustomerGenres g2 ON g1.CustomerId = g2.CustomerId AND g1.GenreId < g2.GenreId
GROUP BY g1.GenreId, g1.GenreName, g2.GenreId, g2.GenreName
HAVING COUNT(*) >= 5
ORDER BY CoOccurrences DESC
LIMIT 20;
```

## 13. Seasonal sales patterns
**Question:** Analyze seasonal sales patterns and identify peak selling periods?

```sql
SELECT 
    CASE 
        WHEN CAST(strftime('%m', InvoiceDate) AS INTEGER) IN (12, 1, 2) THEN 'Winter'
        WHEN CAST(strftime('%m', InvoiceDate) AS INTEGER) IN (3, 4, 5) THEN 'Spring'
        WHEN CAST(strftime('%m', InvoiceDate) AS INTEGER) IN (6, 7, 8) THEN 'Summer'
        ELSE 'Fall'
    END as Season,
    strftime('%Y', InvoiceDate) as Year,
    COUNT(*) as OrderCount,
    ROUND(SUM(Total), 2) as TotalRevenue,
    ROUND(AVG(Total), 2) as AvgOrderValue,
    COUNT(DISTINCT CustomerId) as UniqueCustomers
FROM Invoice
GROUP BY 
    CASE 
        WHEN CAST(strftime('%m', InvoiceDate) AS INTEGER) IN (12, 1, 2) THEN 'Winter'
        WHEN CAST(strftime('%m', InvoiceDate) AS INTEGER) IN (3, 4, 5) THEN 'Spring'
        WHEN CAST(strftime('%m', InvoiceDate) AS INTEGER) IN (6, 7, 8) THEN 'Summer'
        ELSE 'Fall'
    END,
    strftime('%Y', InvoiceDate)
ORDER BY Year, 
    CASE Season
        WHEN 'Spring' THEN 1
        WHEN 'Summer' THEN 2
        WHEN 'Fall' THEN 3
        WHEN 'Winter' THEN 4
    END;
```

## 14. Employee hierarchy and sales performance
**Question:** Show the employee hierarchy with their direct reports and combined team sales performance?

```sql
WITH RECURSIVE EmployeeHierarchy AS (
    -- Base case: top-level employees (no manager)
    SELECT 
        EmployeeId,
        FirstName || ' ' || LastName as EmployeeName,
        Title,
        ReportsTo,
        0 as Level,
        FirstName || ' ' || LastName as HierarchyPath
    FROM Employee
    WHERE ReportsTo IS NULL
    
    UNION ALL
    
    -- Recursive case: employees with managers
    SELECT 
        e.EmployeeId,
        e.FirstName || ' ' || e.LastName as EmployeeName,
        e.Title,
        e.ReportsTo,
        eh.Level + 1,
        eh.HierarchyPath || ' -> ' || e.FirstName || ' ' || e.LastName
    FROM Employee e
    JOIN EmployeeHierarchy eh ON e.ReportsTo = eh.EmployeeId
),
EmployeeSales AS (
    SELECT 
        e.EmployeeId,
        COALESCE(SUM(i.Total), 0) as DirectSales,
        COUNT(DISTINCT c.CustomerId) as CustomersManaged
    FROM Employee e
    LEFT JOIN Customer c ON e.EmployeeId = c.SupportRepId
    LEFT JOIN Invoice i ON c.CustomerId = i.CustomerId
    GROUP BY e.EmployeeId
)
SELECT 
    eh.Level,
    REPEAT('  ', eh.Level) || eh.EmployeeName as IndentedName,
    eh.Title,
    ROUND(COALESCE(es.DirectSales, 0), 2) as DirectSales,
    es.CustomersManaged,
    eh.HierarchyPath
FROM EmployeeHierarchy eh
LEFT JOIN EmployeeSales es ON eh.EmployeeId = es.EmployeeId
ORDER BY eh.HierarchyPath;
```

## 15. Advanced customer segmentation with RFM analysis
**Question:** Perform RFM (Recency, Frequency, Monetary) analysis to segment customers?

```sql
WITH CustomerRFM AS (
    SELECT 
        c.CustomerId,
        c.FirstName || ' ' || c.LastName as CustomerName,
        c.Country,
        -- Recency: days since last purchase
        JULIANDAY('2013-12-31') - JULIANDAY(MAX(i.InvoiceDate)) as Recency,
        -- Frequency: number of purchases
        COUNT(i.InvoiceId) as Frequency,
        -- Monetary: total amount spent
        SUM(i.Total) as Monetary
    FROM Customer c
    JOIN Invoice i ON c.CustomerId = i.CustomerId
    GROUP BY c.CustomerId, c.FirstName, c.LastName, c.Country
),
RFMScores AS (
    SELECT 
        *,
        -- Score from 1-5 (5 being best)
        CASE 
            WHEN Recency <= 50 THEN 5
            WHEN Recency <= 100 THEN 4
            WHEN Recency <= 200 THEN 3
            WHEN Recency <= 300 THEN 2
            ELSE 1
        END as R_Score,
        CASE 
            WHEN Frequency >= 7 THEN 5
            WHEN Frequency >= 5 THEN 4
            WHEN Frequency >= 3 THEN 3
            WHEN Frequency >= 2 THEN 2
            ELSE 1
        END as F_Score,
        CASE 
            WHEN Monetary >= 45 THEN 5
            WHEN Monetary >= 25 THEN 4
            WHEN Monetary >= 15 THEN 3
            WHEN Monetary >= 5 THEN 2
            ELSE 1
        END as M_Score
    FROM CustomerRFM
)
SELECT 
    CustomerName,
    Country,
    ROUND(Recency, 0) as DaysSinceLastPurchase,
    Frequency as TotalOrders,
    ROUND(Monetary, 2) as TotalSpent,
    R_Score || F_Score || M_Score as RFM_Score,
    CASE 
        WHEN R_Score >= 4 AND F_Score >= 4 AND M_Score >= 4 THEN 'Champions'
        WHEN R_Score >= 3 AND F_Score >= 3 AND M_Score >= 3 THEN 'Loyal Customers'
        WHEN R_Score >= 4 AND F_Score <= 2 THEN 'New Customers'
        WHEN R_Score <= 2 AND F_Score >= 3 AND M_Score >= 3 THEN 'At Risk'
        WHEN R_Score <= 2 AND F_Score <= 2 THEN 'Lost Customers'
        WHEN M_Score >= 4 THEN 'Big Spenders'
        ELSE 'Others'
    END as CustomerSegment
FROM RFMScores
ORDER BY (R_Score + F_Score + M_Score) DESC, CustomerName;
```