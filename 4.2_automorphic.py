num = int(input("Enter a number: "))

if 0 <= num <= 9:
    if str(num * num).endswith(str(num)):
        print(f"{num} is an Automorphic num.")
    else:
        print(f"{num} is not an Automorphic num.")
else:
    print("Invalid input")
