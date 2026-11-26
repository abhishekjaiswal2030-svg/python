for i in range(0,2):
 name = input("User Name: ")
 age = int(input("User Age: "))
 country = input("User Country: ").strip().title()

 if country == "United Kingdom":
    print("Name:",name)
    print('Country:',country)
    print("You are UK citizen")
    if age >= 18:
        print('Age:',age)
        print("You are eligible for vote")
    else:
        print('Age:',age)
        print("You are not eligible for vote")
 else:
    print("You are not from United Kingdom")

 print("Thank you for applying for the voter list.")
 