-- Find the Names of the Callers
SELECT name 
    FROM people
    JOIN phone_calls ON people.phone_number = phone_calls.caller
    WHERE phone_calls.year = 2023
    AND phone_calls.month = 7 
    AND phone_calls.day = 28
    AND phone_calls.duration <= 60;