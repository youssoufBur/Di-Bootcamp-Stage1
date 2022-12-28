da = input("Entrer votre date de naissance (jj/mm/aaaa):")
esp ="       "
chaine = esp+"|:B:i:r:t:h:d:a:y:|"
happy = esp+" __|"+" "*11+"|__"
a= (len(chaine)-5)/2
b="_"*3
A = "i"*5
A = esp+"    "+b+A+b
B =esp+"|"+" "*17+"|"
c = esp+"   |:H:a:p:p:y:|"
C = esp+"~"*19

top = esp+"|"+"^"*17+"|"
print(f"{A}\n{c}\n{happy}\n{top}\n{chaine}\n{B}\n{C}\n{esp}    {da}")
