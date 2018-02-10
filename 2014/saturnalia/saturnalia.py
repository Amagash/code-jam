file = open("A-small-practice-saturnalia.bin", "r")

file.readline()

out = open("output-small-saturnalia.txt", "w")
i = 1
for line in file:
    out.write("Case #{}:".format(i) + "\n")
    i += 1
    dash = "+{}+\n".format((len(line) + 1) * "-")
    out.write(dash)
    out.write("| {} |\n".format(line[:-1]))
    out.write(dash)

out.close()
