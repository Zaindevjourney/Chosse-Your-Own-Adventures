                          #CHOOSE YOUR OWN ADVENTURE#
name = input("Type your name: ")
print("Welcome" ,name, "to this adventure! ")
answer = input("You are on a dirt road, it has come to an end and you can go left or right.Which way would you like to go? ").lower()

if answer == "left":
    answer = input("you come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross (swim/walk)? ")

    if answer == "swim":
        print("You swam accross and were eaten by an alligator. ")

    elif answer == "walk":
        print("You walked for many miles, run out of water and you lost the game. ")

    else:
        print("Not a valid option. you lose.")


elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back and lose. ")

    elif answer == "cross":
        answer = input("You cross the bridage and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You talk to the stanger and they give you gold. YOU WIN!")

        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")

        else:
            print("Not a valid option. you lose. ")    

    else:
            print("Not a valid option. you lose. ")    


else:
    print('Not a valid option. you  lose. ')

print("THANK YOU FOR TRYING" ,name)