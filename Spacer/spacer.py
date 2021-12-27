import os

def job():
    def saver():
        with open("./spacer.txt", "r") as f:
            lines = f.readlines()

        with open("./backup.txt", "w") as f2:
            f2.writelines(lines)

    i = input("Choose a valid option\nOriginal(o) or Save(s) or New(n) or Quit(q): ").lower()

    if i.startswith("o"):
        if os.path.exists("./backup.txt"):
            with open("./backup.txt", "r") as f:
                lines = f.readlines()

            with open("./spacer.txt", "w") as f2:
                f2.writelines(lines)
        else:
            print("No backup file found")

    elif i.startswith("s"): saver()

    elif i.startswith("n"):
        if not os.path.exists("./spacer.txt"): saver()

        ment = input("Enter the symbol you want to replace: ")
        print("ment", ment)
        repment = input("Enter the symbol you want to replace it with: ")
        print("repment", repment)

        donzo = []

        with open("./spacer.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                rep = line.replace(F"{ment}", F"{repment}")
                print("rep", rep)
                donzo.append(rep)

        with open("./backup.txt", "w") as f2:
            f2.writelines(lines)

        with open("./spacer.txt", "w") as f3:
            f3.write("".join(donzo))

    elif i.startswith("q"): quit()

    else: print("Invalid option")

    print("\nDone\n")

    job()
job()