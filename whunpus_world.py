import numpy as np

while True:
    probability= float(input("Insert probability -> ")) #probability of being a well
    print("\n")

    c00= 0
    c11= 0
    c22= 0
    valid= 0.0
    total= 0

    if probability == 0:
        print("exit()")
        break

    while valid < 10000:
        total= total + 1
        a= np.array([[0,0,0],
                    [0,0,0],
                    [0,0,0]])

        if np.random.random() <= probability:
            a[0][0]= 1

        if np.random.random() <= probability:
            a[1][1]= 1

        if np.random.random() <= probability:
            a[2][2]= 1

        #nao é necessario as 3 linhas seguintes pq ja sabemos que nao podem sao poços
        #logo vao ser descartados e na contam como valdos, logo é um desperdicio
        #de tempo e resursos da maquina

        #if np.random.random() <= probability:
        #    a[1][0]= 1

        #if np.random.random() <= probability:
        #    a[2][1]= 1

        #if np.random.random() <= probability:
        #    a[2][0]= 1

        #if a[2][0] == 0: #start position isnt a well
        #    if a[1][0] == 0 and a[2][1] == 0: #first move isnt a well

        if a[1][1] == 1 or (a[0][0] == 1 and a[2][2] == 1) or (a[0][0] == 1 and a[1][1] == 1 and a[2][2] == 1): #check diagonal to find is first move is a brise
            valid= valid + 1.0
            #print(a)

            if a[0][0] == 1:
                c00= c00 + 1

            if a[1][1] == 1:
                c11= c11 + 1

            if a[2][2] == 1:
                c22= c22 +1

    print("P(c00)= %f  P(c11)= %f  P(c22)= %f" %(c00/valid, c11/valid, c22/ valid))
    print("well prob.= %.5f, total calculated= %d, valid= %d, invalid= %d\n" %(probability, total, valid, total - valid))
