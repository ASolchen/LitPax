
GRAY_30 = "#b3b3b3"
GRAY_50 = "#808080"

f_name = input("Enter file name:")

with open(f"{f_name}.svg", "r") as fp:
    text = fp.read()

with open(f"{f_name}_Disa.svg", "w") as fp:
    fp.write(text.replace(GRAY_50, GRAY_30))