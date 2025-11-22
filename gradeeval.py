import sys

if len(sys.argv) != 6:
    print("Usage: python3 gradeeval.py <s1> <s2> <s3> <s4> <s5>")
    sys.exit(1)

s1 = int(sys.argv[1])
s2 = int(sys.argv[2])
s3 = int(sys.argv[3])
s4 = int(sys.argv[4])
s5 = int(sys.argv[5])

avg = (s1 + s2 + s3 + s4 + s5) / 5
print("Average =", avg)

if avg >= 80:
    print("A grade")
elif avg >= 60:
    print("B grade")
elif avg >= 40:
    print("C grade")
elif avg >= 30:
    print("D grade")
else:
    print("Fail")
