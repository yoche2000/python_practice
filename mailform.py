# Email format filter, a function to check the format validity of an email address
# by Bbangddok's Kimbab
def mailform(addr):
    atcounter = 0
    spacecounter = 0
    dotafterat = 0
    for x in addr:
        if atcounter != 0:
            if x == '.':
                dotafterat = 1
        if x == '@':
            atcounter += 1
        if x == ' ':
            spacecounter += 1

    if (atcounter == 1 and spacecounter == 0 and dotafterat == 1):
        print("Valid email format.")
        return addr
    else:
        print("Invalid email format.")
        if (atcounter != 1):
            print("A valid email address requires one \"@\".")
        else:
            if (dotafterat != 1):
                print("A valid email address should include a \".\" after \"@\".")
        if spacecounter != 0:
            print("A valid email address should include no space.")
        addr = input("Please input the mail address that your willing to check: \n")
        ans = mailform(addr)
        return ans

addr = input("Please input the mail address that your willing to check: \n")    #Generate the first input
v_addr=mailform(addr)   #Running the function
print(v_addr)           #Printing the valid mail address
