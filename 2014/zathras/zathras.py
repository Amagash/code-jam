# file = open("input", "r")
# file = open("A-small-practice-zathras.bin", "r")
file = open("B-large-practice-zathras.bin", "r")

file.readline()
# output = open("out-test.txt", "w")
# output = open("out-small-zathras.txt", "w")
output = open("out-large-zathras.txt", "w")

i = 1
for line in file:
    list = map(int, line.split())
    A = list[0]
    B = list[1]
    alpha = list[2]
    beta = list[3]
    Y = list[4]
    while Y != 0:
        decom_a = int(A*0.01)
        decom_b = int(B*0.01)
        couple_num = min(A, B)
        offspring = int(couple_num * 0.02)
        acrobots = int(offspring * alpha * 0.01)
        bouncoids = int(offspring * beta * 0.01)
        remaining = offspring - (acrobots + bouncoids)
        new_acro = int(remaining / 2) + acrobots
        new_boun = int(remaining / 2) + bouncoids
        if remaining % 2 != 0:
            new_boun += 1
        A = new_acro + A - decom_a
        B = new_boun + B - decom_b
        Y -= 1
    print "Case #{}: {} {}\n".format(i, A, B)
    output.write("Case #{}: {} {}\n".format(i, A, B))
    i += 1
file.close()
output.close()


