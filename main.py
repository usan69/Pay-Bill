import random



names_str=input("Give me everybody's names, separated by a comma. ")
names=names_str.split(",")

#num_names=len(names)
#random_choice = random.randint( 0 , num_names - 1)
#person_who_will_pay=names[random_choice]      *another-wayy

person_who_will_pay=random.choice(names)


print(person_who_will_pay +" is going to buy the meal today!")


print("sorry, " + person_who_will_pay + " today maybe your bad day")
