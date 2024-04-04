-- Looking for a crime scene report that matches the date and the location of the crime
SELECT description
    FROM crime_scene_reports
    WHERE day = 28 
    AND month = 7 
    AND street = 'Humphrey Street';