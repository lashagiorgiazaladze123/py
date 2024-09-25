unit = input("enter your unit of weight(K-kilogram)(Lbs-pounds):")
weight = float(input("enter your weight:"))
if unit == "K"or unit == "k":
    result = weight * 2.2
    print(result)
elif unit == "Lbs"or unit == "lbs":
    result = weight / 2.2
    print(result)
else:
    print("wrong unit")