-- Finds the Name of the people associated with the ATM account Number
SELECT name 
    FROM people
    JOIN bank_accounts ON people.id = bank_accounts.person_id
    JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
    WHERE year = 2023
    AND month = 7
    AND day = 28 
    AND atm_location = 'Leggett Street';