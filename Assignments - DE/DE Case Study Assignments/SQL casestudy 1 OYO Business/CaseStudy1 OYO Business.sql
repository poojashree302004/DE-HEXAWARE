CREATE DATABASE CaseStudy1;
USE CaseStudy1;

CREATE TABLE Oyo_City( Hotel_ID INT, City VARCHAR(20));
BULK INSERT Oyo_City
FROM 'D:\Victus Laptop\Downloads\Oyo_City.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',
    TABLOCK
);

SELECT * FROM Oyo_City;

CREATE TABLE Oyo_Sales( booking_id INT, customer_id INT, status VARCHAR(20), check_in DATE, check_out DATE, no_of_rooms INT, hotel_id INT, amount INT, discount INT, date_of_booking DATE);
BULK INSERT Oyo_Sales
FROM 'D:\Victus Laptop\Downloads\Oyo_Sales.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',
    TABLOCK
);
SELECT * FROM Oyo_Sales;

-- Average Room Rate of different Cities
SELECT oc.city, AVG(os.amount) AS "Average Room Rate" 
FROM Oyo_City oc
LEFT JOIN Oyo_Sales os
ON oc.Hotel_ID = os.hotel_id
GROUP BY oc.City
ORDER BY AVG(os.amount) DESC;

-- No of bookings of different cities in Jan Feb Mar Months
SELECT oc.city, COUNT(os.booking_id) AS "Number Of Bookings"
FROM Oyo_City oc
LEFT JOIN Oyo_Sales os
ON oc.Hotel_ID = os.hotel_id
WHERE MONTH(os.date_of_booking) IN (1,2,3) AND os.status != 'Cancelled'
GROUP BY oc.City
ORDER BY COUNT(os.booking_id) DESC;

-- Frequency of early bookings prior to check-in the hotel
SELECT COUNT(*) AS "Frequency of Early Bookings" FROM Oyo_Sales WHERE date_of_booking < check_in;
SELECT datediff(day, date_of_booking, check_in) AS "Number Of days in advance" , COUNT(*) AS "Frequency of Early Bookings" 
FROM Oyo_Sales 
WHERE date_of_booking < check_in AND status != 'Cancelled' 
GROUP BY datediff(day, date_of_booking, check_in);

-- Frequency of bookings of no of rooms in Hotel
SELECT hotel_id, COUNT(no_of_rooms) AS "No of Rooms" FROM Oyo_Sales WHERE status != 'Cancelled' GROUP BY hotel_id;

-- New customers in Feb month
SELECT COUNT(customer_id) AS "New customers in Feb Month" 
FROM Oyo_Sales 
WHERE MONTH(date_of_booking) = 2 AND status != 'Cancelled' AND customer_id NOT IN 
(SELECT customer_id 
FROM Oyo_Sales 
WHERE date_of_booking < '2022-02-01');

-- Net revenue to company (due to some bookings cancelled)  
SELECT CASE WHEN GROUPING(hotel_id) = 1 THEN 'Net Revenue' 
ELSE CAST(hotel_id AS VARCHAR(10)) 
END AS hotel_id, 
SUM(amount) AS "Revenue" 
FROM Oyo_Sales 
WHERE status != 'Cancelled' 
GROUP BY ROLLUP(hotel_id);

-- Gross revenue to company
SELECT CASE WHEN GROUPING(hotel_id) = 1 THEN 'Gross Revenue' 
ELSE CAST(hotel_id AS VARCHAR(10)) 
END AS hotel_id, 
SUM(amount) AS "Revenue" 
FROM Oyo_Sales 
GROUP BY ROLLUP(hotel_id);
