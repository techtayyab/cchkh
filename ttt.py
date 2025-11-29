import sys

if len(sys.argv) == 5:
    course_name=sys.argv[1]
    instructor_name=sys.argv[2]
    duration=int(sys.argv[3])
    fees=int(sys.argv[4])
    print("Course details")
    print("Course Name:", course_name)
    print("Instructor Name:", instructor_name)
    print("Duration (in hours):", duration)
    print("Fees:", fees)


else:
    course_name="xyz"
    instructor_name="eyz"
    duration=0
    fees=0
    print("Course details")
    print("Course Name:", course_name)
    print("Instructor Name:", instructor_name)
    print("Duration (in hours):", duration)
    print("Fees:", fees)
    print("This is default values")
