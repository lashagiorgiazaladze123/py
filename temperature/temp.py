temp = (input("enter temperatur:"))
is_sunny = (input("True if it is sunny outside if not its sunny outside False:"))


if temp >= "28" and is_sunny == "True":
    print("It is Hot outside🥵")
    print("It is SUNNY☀️")

elif temp >= "28" and is_sunny == "False":
    print("its warm outside ")
    print("its cloudy☁️")

elif temp >= "25" and is_sunny == "True":
    print("its warm outside ")
    print("its sunny☀️")

elif temp >= "25" and is_sunny == "False":
    print("its warm outside 🌤️")
    print("its cloudy☁️")


elif temp <= "20" and is_sunny == "False":
    print("its cold outside🥶")
    print("its cloudy☁️")

elif temp <= "20" and is_sunny == "True":
    print("its cold outside🥶")
    print("its sunny☀️")

else:
    print("Wrong Input")