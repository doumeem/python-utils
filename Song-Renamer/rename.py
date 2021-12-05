import os

def saver():
    with open("backup.txt", "w") as f:
        f.writelines("\n".join(os.listdir("./Rename")))
    print("Saved the original names.")

i = input("Original or Save or New: ").lower()
if i.startswith("o"):
    try:
        with open("backup.txt", "r") as f:
            lines = f.readlines()
        already_renamed = []
        for line in lines:
            line = line.replace('\n', '')
            for file in sorted(os.listdir("./Rename")):
                if not file in already_renamed:
                    try:
                        os.rename(F"./Rename/{file}", F"./Rename/{line}")
                        already_renamed.append(file)
                    except FileExistsError:
                        pass
        print("Changed the names to the original names.")
    except FileNotFoundError:
        print("You didn't save the original names.")

elif i.startswith("s"):
    saver()

elif i.startswith("n"):
    if not os.path.exists("./backup.txt"): saver()
    original_artist = input("Insert the name for the original artist: ")
    input_artists = input("Insert the names for the feat artists (seperate by ', '): ")
    list_artists = input_artists.split(", ")
    already_renamed = []
    if original_artist or input_artists:
        for file in sorted(os.listdir("./Rename")):
            if not file in already_renamed:
                f = file.replace("-", " ")
                f = f.replace("_", " ")
                if not f.startswith(F"{original_artist} -"): f = f.replace(str(original_artist), f'{original_artist} -')
                if len(list_artists) > 1:
                    for artist in list_artists:
                        f = f.replace(f"{artist} ", f"{artist} & ")
                if not 'Ft.' in f: f = f.replace("Ft", "Ft.")
                os.rename(F"./Rename/{file}", F"./Rename/{f}")
            print(F"Renamed {f}")
            already_renamed.append(file)
    else:
        print("You need to atleast enter something for either the original artist or the feat artists.")

elif i.startswith("t"):
    for file in sorted(os.listdir("./Rename")):
        f = file.replace(" ", "-")
        f = f.replace("--", "-")
        f = f.replace("&", "")
        f = f.replace("Ft.", "Ft")
        os.rename(F"./Rename/{file}", F"./Rename/{f}")

else: print("You need to choose a available option")

input("\nClick any button to exit.")
