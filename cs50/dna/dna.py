import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Wrong usage, try this: dna.py databases/small.csv sequences/1.txt")
        return

    # TODO: Read database file into a variable
    rows = []
    with open(sys.argv[1]) as file:
        db_of_people = csv.DictReader(file)
        #print(db_of_people.fieldnames)
        for row in db_of_people:
            rows.append(row)
            #print(row)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as file:
        dna = file.readline()
        #print(dna.fieldnames)


    # TODO: Find longest match of each STR in DNA sequence
    longest_matches_of_each_STR = [0]
    for i in range(1,len(db_of_people.fieldnames)):
        #print(list(db_of_people.fieldnames)[i])   
        #print(f"i is {i}")
        #print(f"rows len is {len(rows)}")
        subseq = list(db_of_people.fieldnames)[i]
        longest_matches_of_each_STR.append(longest_match(dna,subseq))
    #print(longest_matches_of_each_STR)
        

    # TODO: Check database for matching profiles
    #print(rows[2][db_of_people.fieldnames[2]])
    check_count = 0
    for k in range (0,len(rows)):
        for i in range(1,len(db_of_people.fieldnames)):
            if str(longest_matches_of_each_STR[i]) == rows[k][db_of_people.fieldnames[i]]:
                #print(str(longest_matches_of_each_STR[i]) , rows[k][db_of_people.fieldnames[i]])
                check_count += 1
            else: 
                check_count = 0
        #print(f"k is {k}")
        if check_count == len(db_of_people.fieldnames) - 1:
            print(rows[k][db_of_people.fieldnames[0]])
            break
        elif k == len(rows) - 1:
            print("No match")
        
    #print(f"checkcount is {check_count}")
    #for i in range(1,len(db_of_people.fieldnames)):
        #print(longest_matches_of_each_STR[i], rows[10][db_of_people.fieldnames[i]])
        #print(str(longest_matches_of_each_STR[i]) == rows[2][db_of_people.fieldnames[i]]) 

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run

if __name__ == "__main__":
    main()
