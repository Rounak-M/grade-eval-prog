import sys

print("DEBUG argv:", sys.argv) 

try:
    if len(sys.argv) != 6:
        print("Usage: python marks.py <m1> <m2> <m3> <m4> <m5>")
        sys.exit(1)

    marks = [arg.strip().replace('"', '').replace("'", "") for arg in sys.argv[1:]]

   
    marks = [int(m) for m in marks]

    avg = sum(marks) / 5
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
