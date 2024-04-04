-- Find the Names of the people associated with the Same License Plate
SELECT name 
    FROM people as p
    JOIN bakery_security_logs ON p.license_plate = bakery_security_logs.license_plate
    WHERE bakery_security_logs.day = 28 
    AND bakery_security_logs.month = 7
    AND bakery_security_logs.year = 2023 
    AND bakery_security_logs.hour = 10
    AND bakery_security_logs.minute BETWEEN 15 AND 25;