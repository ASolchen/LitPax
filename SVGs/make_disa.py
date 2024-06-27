
GRAY_30 = "#b3b3b3"
GRAY_50 = "#808080"
f_name = "BLAH"
while (len(f_name)):
    f_name = input("Enter file name:")
    try:
        with open(f"{f_name}.svg", "r") as fp:
            text = fp.read()
        with open(f"{f_name}_Disa.svg", "w") as fp:
            fp.write(text.replace(GRAY_50, GRAY_30))
        print(f"{f_name}_Disa.svg created")
    except Exception as e:
        print(f"{e}")
        print(f"Try again :(")