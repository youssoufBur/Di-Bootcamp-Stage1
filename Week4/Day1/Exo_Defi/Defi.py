import random as R
mot = input("Entrer un mot:")
try:
    if len(mot) == 10:
        for i in mot:
            print(i)
        mt = list(mot)
        R.shuffle(mt)
        #mt="mt"
        for i in mt:
            try:
                mo=mo+i
            except:
                mo=i
        print(mo)
except:
    if len(mot) < 10:
        print("La taille  de votre chaîne de caractère ne vaut pas 10.")
    else:
        print("La taille  de votre chaîne de caractère depasse 10.")
