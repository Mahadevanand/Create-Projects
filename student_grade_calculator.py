def total_marks(m1, m2, m3, m4, m5):
    return m1+m2+m3+m4+m5

def average_marks(total):
    return total/5

def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "Fail"


while True:
    name = input("Enter Student Name: ")
    m1 = int(input("English: "))
    m2 = int(input("Maths: "))
    m3 = int(input("Science: "))
    m4 = int(input("Social: "))
    m5 = int(input("Computer: "))

    total = total_marks(m1, m2, m3, m4, m5)
    avg = average_marks(total)

    result = grade(avg)

    print("\n______ RESULTS _______")
    print("Student Name : ", name)
    print("Total marks : ", total)
    print("Average marks : ", avg)
    print("Grade : ", result)

    choice = input("\nCalculator another student? (yes/no): ")

    if choice.lower() != "yes":
        break
