def cifra_file(f1, f2):
    with open(f1, "r") as reader:
        lines = reader.readlines()
    with open(f2, "w") as reader2:
        for line in lines:
            newLine = ""
            for c in line:
                if c.isalpha():
                    c = chr((ord(c)+13) % 26)
                newLine += c
            reader2.write(newLine)
    print("Listo!")


cifra_file("TextoEjemplo.txt", "NewCypheredFile.txt")
