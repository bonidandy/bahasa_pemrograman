#Bonifasius Dandy Krisnanda
#20210801002
#Teknik informatika

import numpy as np
a= np.array (([5, 3],
             [3, 4]))
b= np.array (([6, 3],
             [7, 3]))
c= np.array (([5,4],
             [12, 10],
             [9, 17]))
print ("A"),
print (a)

print ("B"),
print(b)

print ("C")
print (c)


#Perkalian
print ("a.) A*B")
e = np.dot(a, b)
print (e)

#Pengurangan
print ("b.) A-B")
e = (a-b)
print (e)

#perkalian
print ("c.) A*C")
e = np.dot(a, c.T)
print (e)

#perkalian
print ("d.) B*C")
e = np.dot (b, c.T)
print (e)

#pembagian
print ("d.) B/A")
print ("invers a")
e = np.linalg.inv(a)
print (e)
print ("    ")
print ("Hasil B/A")
d= np.dot(b, e)
print (d)
