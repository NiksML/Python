-- Look through security footage to look for cars that left parking lot in time frame (10:15 - 10:25)
SELECT *
    FROM bakery_security_logs
    WHERE day = 28 
    AND month = 7 
    AND year = 2023
    AND hour = 10 
    AND minute BETWEEN 15 AND 25;