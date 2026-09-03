# Ant Colony Optimization - Path Selection

R1 = int(input("Enter R1: "))
R2 = int(input("Enter R2: "))

P1 = R1 / (R1 + R2)
P2 = R2 / (R1 + R2)

print("Path 1 Probability:", P1 * 100, "%")
print("Path 2 Probability:", P2 * 100, "%")

if P1 > P2:
    print("Most ants will follow Path 1.")
elif P2 > P1:
    print("Most ants will follow Path 2.")
else:
    print("Both paths have equal probability.")
