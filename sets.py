tablicaa = ['Anna', 'Monika', 'Joanna', 'Ewa', 'Karolina', 'Kacper',
             'Dawid', 'Mateusz', 'Ewa', 'Bartosz']
tablicab = ['Kuba', 'Paulina', 'Marzena', 'Zuza', 'Tomek', 'Ewa', 
             'Bartek', 'Olek', 'Jacek', 'Magda', 'Paulina']
tablicac = ['Anastazja', 'Ewa', 'Monika', 'Anna', 'Karolina', 
             'Ola', 'Ula', 'Maciek', 'Paulina']
A = set (tablicaa)
B = set (tablicab)
C = set (tablicac)

print (A.union(B,C))
print (A.intersection(B,C))
print (A.symmetric_difference(B.union(C)))
