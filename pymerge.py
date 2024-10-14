import os

inp = input("Input directory to be compiled:\n")
fav = input("Enter the filename to be saved as:")
ls = os.listdir(inp)
co = 1
for x in ls:
    with open(f"{inp}/{x}", "r") as d:
        c = f"\n#Q{co} ################## \n\n" + d.read()
        with open (f"{fav}.py", "a") as i:
            i.write(f"{c}\n")
    co += 1
print(f"Operation done, file saved in {fav}.py")