CREATE DATABASE OYO;
USE OYO;

CREATE TABLE Hotels (
    hotel_id INT PRIMARY KEY,
    city VARCHAR(50)
);

CREATE TABLE BookingDetails (
    booking_id INT PRIMARY KEY,
    customer_id INT,
    status VARCHAR(20),
    check_in DATE,
    check_out DATE,
    no_of_rooms INT,
    hotel_id INT,
    amount DECIMAL(10, 2),
    discount DECIMAL(10, 2),
    date_of_booking DATE
);
select * from BookingDetails ; 

select * from Hotels ; 

-- 1.Find the - average room rates of different cities
SELECT h.city, 
       ROUND(AVG(b.amount), 2) AS avg_room_rate
FROM BookingDetails b
JOIN hotels h ON b.hotel_id = h.hotel_id
WHERE b.status = 'stayed'
GROUP BY h.city
ORDER BY avg_room_rate DESC;

-- 2.Find the - No of bookings of different cities in Jan Feb Mar Months.
SELECT 
    h.city,
    MONTH(b.check_in) AS month,
    COUNT(*) AS booking_count
FROM BookingDetails b
JOIN hotels h ON b.hotel_id = h.hotel_id
WHERE MONTH(b.check_in) IN (1, 2, 3)
  AND b.status = 'Stayed'
GROUP BY h.city, MONTH(b.check_in)
ORDER BY h.city, month;

-- 4.write the  sql query  Frequency of bookings of no of rooms in Hotel
SELECT no_of_rooms, COUNT(*) AS frequency
FROM BookingDetails
WHERE status = 'stayed'
GROUP BY no_of_rooms
ORDER BY no_of_rooms;

-- 6.Write a sql query Net revenue to company (due to some bookings cancelled)
SELECT SUM(amount) AS net_revenue
FROM bookingDetails
WHERE status = 'stayed';

-- 7.Write a sql query  for  Gross revenue to company
SELECT SUM(amount) AS gross_revenue
FROM bookingDetails;
