def area_rect(a,b):
    return a*b

def pri_rect(x,y):
    return (x+x+y+y)

def area_sq(o):
    return o*o

if __name__ == "__main__":
    print("1.Area rect")
    print("2.Peri rect")
    print("3.Area sq")
    selection = int(input("Enter"))

    while selection < 4:

        if (selection == 1):
            length = int(input("Enter length of rect"))
            breadth = int(input("Enter Breadth"))
            Area_rectangle = area_rect(length, breadth)
            print(Area_rectangle)
            break;

        elif (selection == 2):
            length = int(input("Enter length of rect"))
            breadth = int(input("Enter Breadth"))
            Peri_rect = pri_rect(length, breadth)
            break;

        elif (selection == 3):
            side = int(input("Enter the side"))
            Area_sq = area_sq(side)
            break;

        else:
            print("Wrong")