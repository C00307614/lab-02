with open("sample.txt", "r") as src:
        with open("copy.txt", "w") as dst:
            dst.write(src.read())