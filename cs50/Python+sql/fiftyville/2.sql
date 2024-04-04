-- Checking Their Interview Transcripts at the Time and Mentions Bakery
SELECT transcript
    FROM interviews
    WHERE day = 28 
    AND month = 7 
    AND transcript LIKE '%bakery%';