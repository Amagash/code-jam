file = open("B-large-practice.bin", 'r')
out = open("output-large", 'w')

number_test_case = int(file.readline())

def highest_proba(element):
    element.sort()
    proba = float(1)
    for i in range(len(element)/2):
        proba = proba * float(1 - element[i] * element[-1-i])
    return proba

liste = []
for line in file:
    liste.append(map(float, line.split()))

proba = 0
case = 0
for element in liste:
    if len(element) > 1:
        proba = highest_proba(element)
        case += 1
    else:
        continue
    out.write("Case #{}: {}\n".format(case, proba))

file.close()
out.close()