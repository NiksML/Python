-- Find Earliest Flight That Day (8: 20)
SELECT *    
    FROM flights
    WHERE origin_airport_id = 8 
    AND flights.year = 2023 
    AND flights.month = 7 
    AND flights.day = 29
    ORDER BY hour,minute ASC LIMIT 1;