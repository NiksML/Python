-- Find Passenger Names for the flight (Killer is Bruce)
SELECT name 
    FROM people
    JOIN passengers ON people.passport_number = passengers.passport_number
    JOIN flights ON passengers.flight_id = flights.id
    JOIN airports ON flights.origin_airport_id = airports.id
    WHERE airports.city = 'Fiftyville'
    AND flights.year = 2023 
    AND flights.month = 7 
    AND flights.day = 29 
    AND flights.hour = 8 
    AND flights.minute = 20;