n = int(input("Enter number of elements :"))

# list with some default words for the game to be played asap.
a = ['Gas','Food','Gym','Health']

# Below line read inputs from user using map()
# which consists of list converter function with map() helped to place all user given words inside the xlsx file.
b = list(map(str,input("\nEnter the words in a single go: ").strip().split()))[:n]

print("\n List is -", a)

a = a + b

print(a)
