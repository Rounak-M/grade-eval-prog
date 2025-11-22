import sys

try:
    if len(sys.argv) != 5:
        print("Usage: python marks.py <a> <b> <c> <d> <e>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    d = int(sys.argv[4])
    e = int(sys.argv[5])

    avg = (a + b + c + d + e) / 5

    print("Average of 5 subjects:", avg)

    if avg > 80:
        print("Grade: A")
    elif 60 < avg <= 80:
        print("Grade: B")
    elif 40 < avg <= 60:
        print("Grade: C")
    else:
        print("You Failed.")

except ValueError:
    print("Invalid input. All values must be numbers.")
