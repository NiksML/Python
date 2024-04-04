-- Check Phone Calls During the Time Frame and Tap Into Call
SELECT caller 
    FROM phone_calls
    WHERE year = 2023 
    AND month = 7 
    AND day = 28
    AND duration <= 60;
