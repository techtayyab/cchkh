import sys

if len(sys.argv) == 5:
    name=sys.argv[1]
    marks1=int(sys.argv[2])
    marks2=int(sys.argv[3])
    marks3=int(sys.argv[4])
    ascore=(marks1 + marks2 + marks3) / 3

    print("Student details")
    print("Name:", name)
    print("Average marks:", ascore)
else:
    name="xyz"
    marks1=0
    marks2=0
    marks3=0
    ascore=(marks1 + marks2 + marks3) / 3

    print("Student details")
    print("Name:", name)
    print("Average marks:", ascore)
    print("This is default values")
