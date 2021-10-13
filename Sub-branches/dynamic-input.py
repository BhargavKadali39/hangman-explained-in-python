n = int(input("Enter number of elements :"))

a = ['Gas','Food','Gym','Health']

# Below line read inputs from user using map()

b = list(map(str,input("\nEnter the words in a single go: ").strip().split()))[:n]

print("\n List is -", a)

a = a + b

print(a)
