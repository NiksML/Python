-- Find All withdraws from the specific ATM referenced in 2nd Witness Transcript
SELECT * 
    FROM atm_transactions
    WHERE year = 2023
    AND month = 7
    AND day = 28
    AND atm_location = 'Leggett Street';