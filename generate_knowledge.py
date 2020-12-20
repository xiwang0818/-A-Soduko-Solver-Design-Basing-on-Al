import numpy as np
from field_var import field_var

###################################
###### Your Code


def generate_knowledge(sudoku):
    # TODO generate the Knowledge Base
    # you can assume the sudoku is always a 4x4 array. 
    # Feel free to add helper functions in this file if you need them
    # Do not change any other notebooks or files only this file will be evaluated in the end.
    # It is also the only file you need to submit
    # Do not import any additional module or packages
    kb = []
    # TODO fill kb with propositions
    
    for i in range(4):
        for j in range(4):
            if sudoku[i][j] != 0:
                v = int(sudoku[i][j])
                new_proposition = field_var(v, i, j)
                kb.append(new_proposition)



    v = [1,2,3,4]

    for x in range(4):
        for y in range(4):
            new_proposition = field_var(1,x,y) + " | " + field_var(2,x,y) + " | " + field_var(3,x,y)+ " | " + field_var(4,x,y)
            kb.append(new_proposition)

    y = 0
    x = 0

    
    # #counter = 0
    for i in range (4):

            
        for n in v:
            new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x, y+1)
            #print(new_proposition)
            kb.append(new_proposition)
            new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x, y+2)
            #print(new_proposition)
            kb.append(new_proposition)
            new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x, y+3)
            #print(new_proposition)
            kb.append(new_proposition)
                
            new_proposition = field_var(n, x, y+1) + " ==> ~" + field_var(n, x, y)
            #print(new_proposition)
            kb.append(new_proposition)
            new_proposition = field_var(n, x, y+2) + " ==> ~" + field_var(n, x, y)
            #print(new_proposition)
            kb.append(new_proposition)
            new_proposition = field_var(n, x, y+3) + " ==> ~" + field_var(n, x, y)
            #print(new_proposition)
            kb.append(new_proposition)
            ##counter += 6
        x += 1



    x = 0
    y = 1

    for i in range (4):

        for n in v:
            '''if sudoku[x][y] == n:
                new_proposition = field_var(n,x, y) 
                kb.append(new_proposition)'''

            new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x, y+1)
            kb.append(new_proposition)            
            ##print(new_proposition)
            new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x, y+2)
            kb.append(new_proposition)
            ##print(new_proposition)
            new_proposition = field_var(n, x, y+1) + " ==> ~" + field_var(n, x, y)
            kb.append(new_proposition)
            ##print(new_proposition)
            new_proposition = field_var(n, x, y+2) + " ==> ~" + field_var(n, x, y)
            kb.append(new_proposition)
            ##print(new_proposition)
            ##counter += 4

        x += 1


    x = 0
    y = 2

    for i in range (4):
        for n in v:

            new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x, y+1)
            kb.append(new_proposition)
            ##print(new_proposition)
            new_proposition = field_var(n, x, y+1) + " ==> ~" + field_var(n, x, y)
            kb.append(new_proposition)
            ##print(new_proposition)
            #counter += 2
        x += 1

######################################行遍历
        
        
        
    x = 0
    y = 0

    for i in range (4):

        #for j in range (3):
        for n in v:

            new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x+1, y)
            kb.append(new_proposition)
            new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x+2, y)
            kb.append(new_proposition)
            new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x+3, y)
            kb.append(new_proposition)

            new_proposition = field_var(n, x+1, y) + " ==> ~" + field_var(n, x, y)
            kb.append(new_proposition)
            new_proposition = field_var(n, x+2, y) + " ==> ~" + field_var(n, x, y)
            kb.append(new_proposition)
            new_proposition = field_var(n, x+3, y) + " ==> ~" + field_var(n, x, y)
            kb.append(new_proposition)
            ##counter += 6
        y += 1


    y = 0
    x = 1

    for i in range (4):
        for n in v:

            new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x+1, y)
            kb.append(new_proposition)
            new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x+2, y)
            kb.append(new_proposition)

            new_proposition = field_var(n, x+1, y) + " ==> ~" + field_var(n, x, y)
            kb.append(new_proposition)
            new_proposition = field_var(n, x+2, y) + " ==> ~" + field_var(n, x, y)
            kb.append(new_proposition)
            #counter += 4
        y += 1


    y = 0
    x = 2

    for i in range (4):
        for n in v:


            new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x+1, y)
            kb.append(new_proposition)

            new_proposition = field_var(n, x+1, y) + " ==> ~" + field_var(n, x, y)
            kb.append(new_proposition)
            #counter += 2
        y += 1
    #########################################列遍历
        
        
        
    x = 0
    y = 0
    for n in v:


        new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x, y+1)
        kb.append(new_proposition)
        new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x+1, y+1)
        kb.append(new_proposition)
        new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x+1, y)
        kb.append(new_proposition)

        new_proposition = field_var(n, x, y+1) + " ==> ~" + field_var(n, x, y)
        kb.append(new_proposition)
        new_proposition = field_var(n, x+1, y+1) + " ==> ~" + field_var(n, x, y)
        kb.append(new_proposition)
        new_proposition = field_var(n, x+1, y) + " ==> ~" + field_var(n, x, y)
        kb.append(new_proposition)



        new_proposition = field_var(n, x, y+1) + " ==> ~" + field_var(n, x+1, y+1)
        kb.append(new_proposition)
        new_proposition = field_var(n, x, y+1) + " ==> ~" + field_var(n, x+1, y)
        kb.append(new_proposition)

        new_proposition = field_var(n, x+1, y+1) + " ==> ~" + field_var(n, x, y+1)
        kb.append(new_proposition)
        new_proposition = field_var(n, x+1, y) + " ==> ~" + field_var(n, x, y+1)
        kb.append(new_proposition)



        new_proposition = field_var(n, x+1, y+1) + " ==> ~" + field_var(n, x+1, y)
        kb.append(new_proposition)
        new_proposition = field_var(n, x+1, y) + " ==> ~" + field_var(n, x+1, y+1)
        kb.append(new_proposition)
        #counter += 12

    x = 0
    y = 2
    for n in v:

        new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x, y+1)
        kb.append(new_proposition)
        new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x+1, y+1)
        kb.append(new_proposition)
        new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x+1, y)
        kb.append(new_proposition)

        new_proposition = field_var(n, x, y+1) + " ==> ~" + field_var(n, x, y)
        kb.append(new_proposition)
        new_proposition = field_var(n, x+1, y+1) + " ==> ~" + field_var(n, x, y)
        kb.append(new_proposition)
        new_proposition = field_var(n, x+1, y) + " ==> ~" + field_var(n, x, y)
        kb.append(new_proposition)


        new_proposition = field_var(n, x, y+1) + " ==> ~" + field_var(n, x+1, y+1)
        kb.append(new_proposition)
        new_proposition = field_var(n, x, y+1) + " ==> ~" + field_var(n, x+1, y)
        kb.append(new_proposition)

        new_proposition = field_var(n, x+1, y+1) + " ==> ~" + field_var(n, x, y+1)
        kb.append(new_proposition)
        new_proposition = field_var(n, x+1, y) + " ==> ~" + field_var(n, x, y+1)
        kb.append(new_proposition)



        new_proposition = field_var(n, x+1, y+1) + " ==> ~" + field_var(n, x+1, y)
        kb.append(new_proposition)
        new_proposition = field_var(n, x+1, y) + " ==> ~" + field_var(n, x+1, y+1)
        kb.append(new_proposition)
        #counter += 12


    x = 2
    y = 0
    for n in v:

        new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x, y+1)
        kb.append(new_proposition)
        new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x+1, y+1)
        kb.append(new_proposition)
        new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x+1, y)
        kb.append(new_proposition)

        new_proposition = field_var(n, x, y+1) + " ==> ~" + field_var(n, x, y)
        kb.append(new_proposition)
        new_proposition = field_var(n, x+1, y+1) + " ==> ~" + field_var(n, x, y)
        kb.append(new_proposition)
        new_proposition = field_var(n, x+1, y) + " ==> ~" + field_var(n, x, y)
        kb.append(new_proposition)



        new_proposition = field_var(n, x, y+1) + " ==> ~" + field_var(n, x+1, y+1)
        kb.append(new_proposition)
        new_proposition = field_var(n, x, y+1) + " ==> ~" + field_var(n, x+1, y)
        kb.append(new_proposition)

        new_proposition = field_var(n, x+1, y+1) + " ==> ~" + field_var(n, x, y+1)
        kb.append(new_proposition)
        new_proposition = field_var(n, x+1, y) + " ==> ~" + field_var(n, x, y+1)
        kb.append(new_proposition)



        new_proposition = field_var(n, x+1, y+1) + " ==> ~" + field_var(n, x+1, y)
        kb.append(new_proposition)
        new_proposition = field_var(n, x+1, y) + " ==> ~" + field_var(n, x+1, y+1)
        kb.append(new_proposition)
        #counter += 12

    x = 2
    y = 2
    for n in v:

        new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x, y+1)
        kb.append(new_proposition)
        new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x+1, y+1)
        kb.append(new_proposition)
        new_proposition = field_var(n, x, y) + " ==> ~" + field_var(n, x+1, y)
        kb.append(new_proposition)

        new_proposition = field_var(n, x, y+1) + " ==> ~" + field_var(n, x, y)
        kb.append(new_proposition)
        new_proposition = field_var(n, x+1, y+1) + " ==> ~" + field_var(n, x, y)
        kb.append(new_proposition)
        new_proposition = field_var(n, x+1, y) + " ==> ~" + field_var(n, x, y)
        kb.append(new_proposition)



        new_proposition = field_var(n, x, y+1) + " ==> ~" + field_var(n, x+1, y+1)
        kb.append(new_proposition)
        new_proposition = field_var(n, x, y+1) + " ==> ~" + field_var(n, x+1, y)
        kb.append(new_proposition)

        new_proposition = field_var(n, x+1, y+1) + " ==> ~" + field_var(n, x, y+1)
        kb.append(new_proposition)
        new_proposition = field_var(n, x+1, y) + " ==> ~" + field_var(n, x, y+1)
        kb.append(new_proposition)



        new_proposition = field_var(n, x+1, y+1) + " ==> ~" + field_var(n, x+1, y)
        kb.append(new_proposition)
        new_proposition = field_var(n, x+1, y) + " ==> ~" + field_var(n, x+1, y+1)
        kb.append(new_proposition)

    return kb

