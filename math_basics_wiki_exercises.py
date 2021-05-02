import math

num_sides = int(input("How many sides is this polygon?\n"))
num_diagonals = ((num_sides*(num_sides-3))/2)
print("A Polygon with "+str(num_sides)+" has "+str(num_diagonals)+" sides.")

a_side_len = int(input("How long is side A: "))
b_side_len = int(input("How long is side B: "))
hypo_len = math.sqrt((a_side_len**2) + (b_side_len**2))
print("A Right Triangle with sides the length of %s, and %s has a hypotenus of length %s"%(a_side_len,b_side_len,hypo_len))

