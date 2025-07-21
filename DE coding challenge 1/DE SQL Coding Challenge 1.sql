

create database TicketBookingSystem ;
use TicketBookingSystem ;
-- drop database TicketBookingSystem ;
-- Create Venue table
CREATE TABLE Venue (
    venue_id INT PRIMARY KEY IDENTITY(1,1),
    venue_name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL
);

-- Create Event table
CREATE TABLE Event (
    event_id INT PRIMARY KEY IDENTITY(1,1),
    event_name VARCHAR(200) NOT NULL,
    event_date DATE NOT NULL,
    event_time TIME NOT NULL,
    total_seats INT NOT NULL,
    available_seats INT NOT NULL,
    venue_id INT NOT NULL,
    ticket_price DECIMAL(10,2) NOT NULL,
    event_type VARCHAR(50) NOT NULL,
    CONSTRAINT chk_event_type CHECK (event_type IN ('Movie', 'Sports', 'Concert')),
    FOREIGN KEY (venue_id) REFERENCES Venue(venue_id)
);

-- Create Customer table
CREATE TABLE Customer (
    customer_id INT PRIMARY KEY IDENTITY(1,1),
    customer_name VARCHAR(200) NOT NULL,
    email VARCHAR(200) UNIQUE NOT NULL,
    phone_number VARCHAR(20) NOT NULL
);

-- Create Booking table
CREATE TABLE Booking (
    booking_id INT PRIMARY KEY IDENTITY(1,1),
    customer_id INT NOT NULL,
    event_id INT NOT NULL,
    num_tickets INT NOT NULL,
    total_cost DECIMAL(10,2) NOT NULL,
    booking_date DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (event_id) REFERENCES Event(event_id)
);

-- Insert records into Venue
INSERT INTO Venue (venue_name, address) VALUES
('Grand Cinema', '123 Movie St, CityA'),
('City Stadium', '456 Sports Rd, CityB'),
('Concert Hall', '789 Music Ave, CityC'),
('Exhibition Center', '101 Expo Blvd, CityD'),
('Community Theater', '202 Play Ln, CityE'),
('Museum of Art', '303 Gallery Pkwy, CityF'),
('Science Center', '404 Discovery Dr, CityG'),
('Botanical Gardens', '505 Green St, CityH'),
('Waterfront Park', '606 Oceanfront Rd, CityI'),
('The Jazz Club', '888 Melody Lane, CityK'),
('Children''s Museum Auditorium', '999 Imagination Blvd, CityL'),
('Innovation Hub', '707 Tech Ave, CityJ');

-- Insert records into Event
INSERT INTO Event (event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type) VALUES
('The Dark Knight Rises', '2025-07-15', '19:00:00', 1, 300, 250, 200.00, 'Movie'),
('Unbooked Test Movie', '2025-07-30', '17:00:00', 1, 100, 100, 250.00, 'Movie'),
('Cricket World Cup Final', '2025-08-20', '14:30:00', 2, 50000, 48000, 1500.00, 'Sports'),
('Rock Legends Concert', '2025-09-10', '20:00:00', 3, 5000, 4500, 2500.00, 'Concert'),
('Comedy Night Live', '2025-07-25', '21:00:00', 4, 150, 100, 150.00, 'Movie'),
('Annual Sports Meet', '2025-08-01', '09:00:00', 5, 10000, 9000, 500.00, 'Sports'),
('Classical Music Gala', '2025-09-22', '18:00:00', 3, 800, 750, 1800.00, 'Concert'),
('Summer Movie Marathon', '2025-07-20', '10:00:00', 1, 400, 350, 100.00, 'Movie'),
('Football Championship', '2025-10-05', '16:00:00', 2, 30000, 28000, 1200.00, 'Sports'),
('Jazz Fusion Night', '2025-10-15', '20:30:00', 6, 600, 550, 2000.00, 'Concert'),
('AI fusion', '2025-06-20', '10:00:00', 1, 100, 40, 500.00, 'Concert'),
('Kids Movie Festival', '2025-07-18', '11:00:00', 7, 200, 180, 80.00, 'Movie');

-- Insert records into Customer
INSERT INTO Customer (customer_name, email, phone_number) VALUES
('Alice Smith', 'alice.s@example.com', '9876543210'),
('John NoBook', 'john.nobook@example.com', '9999988888'),
('Bob Johnson', 'bob.j@example.com', '9988776655'),
('Charlie Brown', 'charlie.b@example.com', '9000000000'),
('Diana Prince', 'diana.p@example.com', '9111111111'),
('Eve Adams', 'eve.a@example.com', '9222222222'),
('Frank Green', 'frank.g@example.com', '9333333333'),
('Grace Hopper', 'grace.h@example.com', '9444444444'),
('Harry Potter', 'harry.p@example.com', '9555555555'),
('Ivy Rose', 'ivy.r@example.com', '9666666666'),
('Jack Sparrow', 'jack.s@example.com', '9777777777');

-- Insert records into Booking
INSERT INTO Booking (customer_id, event_id, num_tickets, total_cost) VALUES
(1, 1, 2, 400.00),
(2, 2, 5, 7500.00),
(3, 3, 1, 2500.00),
(4, 1, 3, 600.00),
(5, 4, 1, 150.00),
(6, 5, 6, 3000.00),
(7, 6, 2, 3600.00),
(8, 7, 4, 400.00),
(9, 8, 5, 6000.00),
(10, 9, 3, 6000.00),
(1, 10, 2, 160.00),
(2, 1, 1, 200.00);

select * from Venue;
select * from Event;
select * from Customer;
select * from Booking;

-- 1. Find the total number of tickets booked and total revenue generated for each event

select E.event_name,sum(B.num_tickets) as total_tickets,sum(B.total_cost) as total_revenue
from Event E
join Booking B on E.event_id = B.event_id
group by E.event_name
order by total_revenue desc;

-- 2. List the maximum tickets booked for each event.

select E.event_name,max(B.num_tickets) as max_ticket_booked
from Event E
join Booking B on E.event_id = B.event_id
group by E.event_name
order by max_ticket_booked desc;

-- 3. Display total tickets sold and revenue grouped by event type.

select event_type,sum(num_tickets) as total_tickets_sold,sum(total_cost) as total_revenue
from Event E
join Booking B on E.event_id = B.event_id
group by rollup(event_type);

-- 4. For each event type, get the average ticket price and total number of events conducted.

select event_type,count(*) as no_of_events,avg(ticket_price) as avg_price
from Event 
group by (event_type)
order by avg_price desc;

-- 5. List venues and the number of distinct events hosted at each venue.

select V.venue_name,count(distinct E.event_id) as event_count 
from Venue V
join Event E on V.venue_id = E.venue_id
group by V.venue_name
order by event_count desc;