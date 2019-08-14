""" Day 26: Nested Logic
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def fines(due_date, return_date):
    """ Returns interger due date in "Hackos"
    Date format: [D,M,Y]
    """
    if return_date[2] > due_date[2]:
        # Year(s) late
        return 10000
    elif return_date[2] == due_date[2]:
        # same year
        if return_date[1] > due_date[1]:
            # month(s) late
            return 500 * (return_date[1] - due_date[1])

        elif return_date[1] == due_date[1] and return_date[0] > due_date[0]:
            # same month, but days late
            return 15 * (return_date[0] - due_date[0])

    return 0 # early / on time


def main():
    date_returned = list(map(int, input().split()))
    date_expected = list(map(int, input().split()))

    sys.stdout.write( str(fines(date_expected, date_returned) ))


if __name__ == "__main__":
    main()
