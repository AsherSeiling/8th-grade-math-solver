pi = 3.1415
import math
import time
# This will help navigate back to start
def ynrspble():
    print("Would you like to go back to start? Y/N")
    yorn = input("")
    if yorn.lower() == "y":
        problemlist()
    else:
        if yorn.lower() == "n":
            print("Thank you for using Seiling math solver v" + varversionofsolver)
        else:
            print("Syntax error please try again")
            ynrspble()

# what this can calculate
def problemlist():
    print("[1] Programing credits")
    print("[2] Y = MX + B")
    print("[3] Slope")
    print("[4] y intercept from table")
    print("[5] x intercept from table")
    print("[6] Two step equations")
    print("[7] Slope To standard form")
    print("[8] Transformations")
    print('[9] Fraction to decimal')
    print('[10] Roots')
    print('[11] Area and Volume')
    print('[12] Pythagorean Theorem')
    print('Select what you would like to use')
    cmd = input()
    if cmd == '1':
        procred()
    elif cmd == '2':
        yemxpb()
    elif cmd == '3':
        slope()
    elif cmd == '4':
        Ytab()
    elif cmd == '5':
        Xtab()
    elif cmd == '6':
        PreAl()
    elif cmd == '7':
        SS()
    elif cmd == '8':
        transformations()
    elif cmd == '9':
        fraction_to_decimal()
    elif cmd == '10':
        nav_for_roots()
    elif cmd == '11':
        area_and_volume_nav()
    elif cmd == '12':
        pythagorean_theorem()

# Programing credits
def procred():
    print("Programmers")
    print(" ")
    print("_____________________________________")
    print("|Math functions | Systems interface |")
    print("|---------------|-------------------|")
    print("| Asher Seiling | Ian Kelley        |")
    print("|_______________|___________________|")
    ynrspble()

#Y=mx+B
def yemxpb():
    ymxb = float(input("Input B "))
    ymxm = float(input("Input M/slope decimal please "))
    ymxx = float(input("Input X "))
    ymxbc = (ymxm * ymxx) + ymxb
    ymxbs = str(ymxbc)
    print("The answer is " + ymxbs)
    ynrspble()

# slope
def slope():
    y1 = float(input("what is your y1? "))
    y2 = float(input("what is your y2? "))
    x1 = float(input("what is your x1? "))
    x2 = float(input("what is your x2? "))
    s1 = y2 - y1
    s2 = x2 - x1
    s3 = s1 / s2
    print(s3)
    ynrspble()

# y from a table - doesn't work
def Ytab():
    tbx = float(input("Input X "))
    tbs = float(input("Input slope (Decimal please) "))
    yft1 = tbx * tbs
    yft2 = tbx - yft1
    yft2s = str(yft2)
    print("y-int= " + yft2s)
    ynrspble()
#x from a table - doesn't work

def Xtab():
    tby = float(input("Input y "))
    tbs = float(input("Input slope "))
    xft1 = tby * tbs
    xft2 = xft1 - tby
    xft2s = str(xft2)
    print("x-int= " + xft2s)
    ynrspble()
# this helps decide what pre al function to use
def PreAl():
    print("[1] Addition")
    print("[2] Subtraction")
    cmd = input()
    if cmd == '1':
        Add()
    elif cmd == '2':
        Sub()

# two step equations
def Add():
    preax = float(input("Input Coefficient (No fractions only decimal) "))
    nmtet = float(input("Input number that equation is equal to" ))
    ipctvar = float(input("Input Constant" ))
    prealcal1 = nmtet - ipctvar
    prealcal2 = prealcal1 / preax
    print("Your answer is: " + str(prealcal2))
    ynrspble()

def Sub():
    print("Input Coefficient (No fractions only decimal)")
    preax = float(input())
    print("Input number that equation is equal to")
    nmtet = float(input())
    print("Input Constant")
    ipctvar = float(input())
    prealcal1 = nmtet + ipctvar
    prealcal2 = prealcal1 / preax
    print("Your awnser is: " + str(prealcal2))
    ynrspble()

#slope to standard form
def SS():
    print("Y = A/Bx + b --> Ax + By = C")
    time.sleep(1)
    y = float(input("enter y value "))
    A = float(input("enter M as fraction A/B - A "))
    B = float(input("enter M as fraction A/B - B "))
    b = float(input("enter b "))
    ys = str(y)
    As = str(A)
    Bs = str(B)
    bs = str(b)
    print("equation: "+ys+"y = " + As + "/" + Bs + "x + " + bs)
    time.sleep(1)
    print("\n-----------------\n")
    time.sleep(1)
    print("equation: -"+As+"/"+Bs+"x + "+ys+"y = "+bs)
    time.sleep(1)
    print("\n-----------------\n")
    time.sleep(1)
    ys1 = str(y*B)
    bs1 = str(b*B)
    print("final equation: -"+As+"x + "+ys1+"y = "+bs1)
    time.sleep(2)
    print("\n-----------------\n")
    time.sleep(2)
    ynrspble()
# Trasformations

def transformations():
    print("What transformation would you like to preform")
    print("[1] Reflections")
    print("[2] Translations")
    print("[3] Dilations")
    print("[4] Rotations")
    rtdr = input()
    if rtdr == "1":
        refleactions()
    elif rtdr == "2":
        translations()
    elif rtdr == "3":
        dialations()
    elif rtdr == "4":
        rotaions()

def translations():
    print("Translations")
    print("Input X cordnate")
    xcor = float(input())
    print("Input Y cordnate")
    ycor = float(input())
    print("Input Horizontal shift")
    hshift = float(input())
    print("Input Vertical shift")
    vshift = float(input())
    yshiftcal = ycor + vshift
    xshiftcal = xcor + hshift
    xstrcon = str(xshiftcal)
    ystrcon = str(yshiftcal)
    print("Your cordnets are: ( " + xstrcon + ", " + ystrcon + " )")
    ynrspble()

def dialations():
    print("Dilations")
    print("Input X cordnet")
    xcor = float(input())
    print("Input Y cordnet")
    ycor = float(input())
    print("Input Dilation factor in decimal")
    dxyfactor = float(input())
    calx1 = xcor * dxyfactor
    caly2 = ycor * dxyfactor
    calxstrcon = str(calx1)
    calystrcon = str(caly2)
    print("Your awnswer is: (" + calxstrcon + ", " + calystrcon + ")")
    ynrspble()

def rotaions():
    print("Rotations")
    print("Input X cordnate")
    xcor = float(input())
    print("Input Y cordnate")
    ycor = float(input())
    print("Input CLOCKWISE rotation (90, 180, 270)")
    rot = input()
    if rot == "90":
        cal1 = xcor * -1
        calstrx = str(cal1)
        calstry = str(ycor)
        print("The answer is: (" + calstry + ", " + calstrx + ")")
        ynrspble()
    elif rot == "180":
        cal1 = xcor * -1
        cal2 = ycor * -1
        calstrx = str(cal1)
        calstry = str(cal2)
        print("The answer is: (" + calstrx + ", " + calstry + ")")
        ynrspble()
    elif rot == "270":
        cal2 = ycor * -1
        calstrx = str(xcor)
        calstry = str(cal2)
        print("The answer is: (" + calstry + ", " + calstrx + ")")
        ynrspble()

def refleactions():
    print("What would you like to reflect across")
    print("[1] X axis")
    print("[2] Y axis")
    print("[3] Y = X")
    print("[4] Y = -X")
    xory = input()
    if xory == "1":
        print("Input X cordnet")
        xcor = float(input())
        print("Input Y cordnet")
        ycor = float(input())
        varcal2 = ycor * -1
        finalcal1 = str(xcor)
        finalcal2 = str(varcal2)
        print("The awnser is: ( " + finalcal1 + ", " + finalcal2 + ")")
        ynrspble()
    elif xory == "2":
        print("Input X cordnet")
        xcor = float(input())
        print("Input Y cordnet")
        ycor = float(input())
        varcal2 = xcor * -1
        finalcal1 = str(ycor)
        finalcal2 = str(varcal2)
        print("The awnser is: ( " + finalcal2 + ", " + finalcal1 + ")")
        ynrspble()
    elif xory == "3":
        print("Input X cordnet")
        xcor = float(input())
        print("Input Y cordnet")
        ycor = float(input())
        finalcal1 = str(ycor)
        finalcal2 = str(xcor)
        print("The awnser is: ( " + finalcal1 + ", " + finalcal2 + ")")
        ynrspble()
    elif xcor == "4":
        print("Rotations")
        print("Input X cordnate")
        xcor = float(input())
        print("Input Y cordnate")
        ycor = float(input())
        print("Input CLOCKWISE rotation (90, 180, 270)")
        rot = input()
        if rot == "90":
            cal1 = xcor * -1
            calstrx = str(cal1)
            calstry = str(ycor)
            print("The answer is: (" + calstry + ", " + calstrx + ")")
            ynrspble()
        elif rot == "180":
            cal1 = xcor * -1
            cal2 = ycor * -1
            calstrx = str(cal1)
            calstry = str(cal2)
            print("The answer is: (" + calstrx + ", " + calstry + ")")
            ynrspble()
        elif rot == "270":
            cal2 = ycor * -1
            calstrx = str(xcor)
            calstry = str(cal2)
            print("The answer is: (" + calstry + ", " + calstrx + ")")
            ynrspble()

#Converts Fractions to decimal
def fraction_to_decimal():
    print('Fracton to decimal converter')
    print('Input the numerator in interger form (Top part of the fraction)')
    varnumfractodec = int(input())
    print('input demonimator in Intager form (Bottom of the fraction)')
    vardemfractonecdem = int(input())
    varcal1 = varnumfractodec / vardemfractonecdem
    varprint = str(varcal1)
    if varcal1 < 1:
        varprint = str(varcal1) + '0'
    print('Your awnswer is ' + varprint)
    ynrspble()

#Square roots
def square_roots():
    print('Input number you want to square')
    varnumtosquare = float(input())
    varsquarerootcal1 = varnumtosquare ** 2
    print('your awnswer is ' + str(varsquarerootcal1))
    ynrspble()

#cube roots
def cube_roots():
    print('Input number you want to cube')
    varnumtocube = float(input())
    varcuberootcal1 = varnumtocube ** 3
    print('your awnswer is ' + str(varcuberootcal1))
    ynrspble()

#Anything else to power
def to_the_power():
    print('Input base number')
    varbasenumber = float(input())
    print('Input what woy would like to multiply it by a power to')
    vartoapower = float(input())
    varcaltoapower1 = varbasenumber ** vartoapower
    print('your awnswer is ' + str(varcaltoapower1))

 #navigaton for roots
def nav_for_roots():
    print('[1] Square roots')
    print('[2] Cube roots')
    print('[3] Other')
    print('[4] Back to start')
    varselectrootnav = input()
    if varselectrootnav == '1':
        square_roots()
    elif varselectrootnav == '2':
        cube_roots()
    elif varselectrootnav == '3':
        to_the_power()
    elif varselectrootnav == '4':
        ynrspble()

# Navigaton volume and area
def area_and_volume_nav():
    print('[1] Area')
    print('[2] Volume')
    print('[3] Exit')
    var_aavn = input()
    if var_aavn == '1':
        nav_area()
    elif var_aavn == '2':
        nav_volume()
    elif var_aavn == '3':
        ynrspble()

# Navigaton Volume
def nav_volume():
    print('[1] Cones')
    print('[2] Cubes')
    print('[3] Spheres')
    print('[4] Cylinder')
    print('[5] Triangular prism')
    var_navv = input()
    if var_navv == '1':
        volume_of_cones()
    elif var_navv == '2':
        volume_of_cubes()
    elif var_navv == '3':
        volume_of_spheres
    elif var_navv == '4':
        volume_of_cylienders()
    elif var_navv == '5':
        volume_of_tri_prism()


# Navigaton Area
def nav_area():
    print('[1] Area of a circle')
    print('[2] Area of a rectangle(or cube)')
    print('[3] Area of a triangle')
    areainputnav = input()
    if areainputnav == '1':
        area_of_a_circle()
    elif areainputnav == '2':
        area_of_square()
    elif areainputnav == '3':
        area_of_triangle()

# Volume of cones
def volume_of_cones():
    print('Input unit')
    varconevoluni = input()
    print('Input radius')
    varinradcone = float(input())
    print('Input hight')
    varnhighcon = float(input())
    varcal1 = (((varinradcone ** 2) * pi) * varnhighcon) * 1/3
    print('Your awnswer is ' + str(varcal1) + ' Cubic ' + varconevoluni)
    ynrspble()

# Volume of Cyinders
def volume_of_cylienders():
    print('Input unit')
    var_ciluninit = input()
    print('Input radius')
    var_radcil = float(input())
    print('Input hight')
    var_highcil = float(input())
    varcalcil1 = ((((var_radcil ** 2) * pi)) * var_highcil)
    print('Your awnswer is ' + str(varcalcil1) + ' Cubic ' + str(var_ciluninit))
    ynrspble()

# Volume of cubes
def volume_of_cubes():
    print('Input unit')
    varcubeunit = input()
    print('Input legth of side 1')
    varcubeside1leg = float(input())
    print('Input legth of side 2')
    varcubeside2leg = float(input())
    print('Input hight')
    varcubehight = float(input())
    varcalcubevol1 = (varcubeside1leg* varcubeside2leg) * varcubehight
    print('Your awnswer is ' + str(varcalcubevol1) + ' Cubic ' + str(varcubeunit))
    ynrspble()
# Volume of spheres
def volume_of_spheres():
    print('Input unit')
    var_sphereunitinput = input()
    print('Input radius')
    var_radsphereinput = float(input())
    var_spherecal1 = (((var_radsphereinput ** 3) * pi) * 4/3)
    print('Your Answer is ' + str(var_spherecal1) + ' Cubic ' + var_sphereunitinput)
    ynrspble()

#Volume of a triangular prism
def volume_of_tri_prism():
    print('Input unit')
    var_unitri = input()
    print('Input legth')
    var_trilegth = float(input())
    print('Input hight of triangle')
    var_tritrihigh = float(input())
    print('Input Triangle base')
    var_tritribase = float(input())
    var_caltrivol1 = ((var_tritrihigh * var_tritribase) * var_trilegth) * 1/2
    print('Your answer is ' + str(var_caltrivol1) + ' cubic ' + var_unitri)
    ynrspble()

# Area of a square
def area_of_square():
    print('Input unit')
    var_areasquareuni = input()
    print('Input Hight of square')
    var_highsquarearea = float(input())
    print('Input Width of square')
    var_squarewidth = float(input())
    var_squareareacal1 = var_highsquarearea * var_squarewidth
    print('Your awnswer is ' + str(var_squareareacal1) + ' ' + var_areasquareuni + ' Squared')
    ynrspble()

# Area of a triangle calculator
def area_of_triangle():
    print('Input unit')
    var_unitareatri = input()
    print('Input triangle hight')
    var_triareahigh = float(input())
    print('Input triangle base')
    var_tribasearea = float(input())
    var_caltriarea1 = (var_triareahigh * var_tribasearea) * 1/2
    print('Your answer is ' + str(var_caltriarea1) +  ' ' + var_unitareatri + ' squared')
    ynrspble()

# area of a circle
def area_of_a_circle():
    print('Input unit')
    var_unicirin = input()
    print('Input Radius')
    var_radcirin = float(input())
    var_calcirc1 = (var_radcirin ** 2) * pi
    print('The answer is ' + str(var_calcirc1) + ' ' + var_unicirin + ' squared')
    ynrspble()

# Calculates Pythagorean Theorem
def pythagorean_theorem():
    print('Input A')
    var_apainput = float(input())
    print('Input B')
    var_bpainput = float(input())
    var_calpa1 = (var_apainput ** 2) + (var_bpainput ** 2)
    var_rootpa = math.sqrt(var_calpa1)
    print('Your awnswer is ' + str(var_rootpa))
    ynrspble()

if __name__ == "__main__":
    varversionofsolver = "1.0 Beta"
    print("Seiling 8th grade math solver v " + varversionofsolver)
    problemlist()