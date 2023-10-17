array = [
        ["|        MCU        |        MCU        |        MCU        |        MCU        |        MCU        |"],
        ["| :---------------: | :---------------: | :---------------: | :---------------: | :---------------: |"],
        ]

# ouverture du fichier kinetis.txt pour écrire avec la syntaxe et un retour à la ligne tous les 5 itérations
with open("STM.txt", "r") as f:
    for i, line in enumerate(f):
        if i % 5 == 0:
            array.append(["| " + line.strip() + " | "])
        else:
            array[-1].append(" " + line.strip() + " | ")

        
        
# écriture de array dans un fichier kinetisFinal.txt
with open("STMFinal.txt", "w") as f:
    for line in array:
        f.write("".join(line) + "\n")