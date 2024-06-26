potential_condition = ["sunny" , "rainy" , "cold"]
current_condition = str(input("What’s the weather like today? (sunny/rainy/cold): "))


if current_condition == potential_condition[0]:
    print("Wear a t-shirt and sunglasses.")

elif current_condition == potential_condition[1]:
    print("Don’t forget your umbrella and a raincoat.")

elif current_condition == potential_condition[2]:
    print("Make sure to wear a warm coat and a scarf.")

else:
    print("Sorry, I don’t have recommendations for this weather.")