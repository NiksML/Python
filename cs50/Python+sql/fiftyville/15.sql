-- Who is a killer--
SELECT name 
    FROM people
    JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
    WHERE bakery_security_logs.day = 28 
    AND bakery_security_logs.month = 7
    AND bakery_security_logs.year = 2023 
    AND bakery_security_logs.hour = 10
    AND bakery_security_logs.minute BETWEEN 15 AND 25

INTERSECT 

SELECT name 
    FROM people
    JOIN phone_calls ON people.phone_number = phone_calls.caller
    WHERE phone_calls.year = 2023
    AND phone_calls.month = 7 
    AND phone_calls.day = 28
    AND phone_calls.duration <= 60;

INTERSECT

SELECT name 
    FROM people
    JOIN bank_accounts ON people.id = bank_accounts.person_id
    JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
    WHERE year = 2023
    AND month = 7
    AND day = 28 
    AND atm_location = 'Leggett Street'

INTERSECT

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