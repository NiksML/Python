-- Find Flight Arrival Location (New York City)
SELECT city 
    FROM airports
    JOIN flights ON airports.id = flights.destination_airport_id
    WHERE flights.origin_airport_id = 8
    AND flights.year = 2023 
    AND flights.month = 7 
    AND flights.day = 29 
    AND flights.hour = 8 
    AND flights.minute = 20;