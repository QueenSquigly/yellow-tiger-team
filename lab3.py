


food = 'pasta'
print(food[0:3])
print(food[-3: ])
first_last = food[0] + food[-1]
print(first_last)
food_list = food.split()
print(food_list)
joined_food = ''.join(food_list)
print(joined_food)

# task 2
#number_list = [1,2,3,4,5]
#number_list.append(6)
#print(number_list)
#number_list.insert(3, 7)
#print(number_list)
#number_list.pop(4)
#print(number_list)
#number_list.remove(1)
#print(number_list)
#print(number_list[0:3])
#print(number_list[-3: ])


#? task 3
books = {"GraveWeaver" : "im the grim reaper", 
"rorita" : "watermelon",
"android_k05" : "soulwinder",
"Komatsuki" : "monochrome"}
x = books.keys()
y = books.values()
q = books.get("GraveWeaver")
books.pop("android_k05")
del {"komatsuki"}
print(x)
print(y)
print(q)