###TD 3

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ortools.sat.python import cp_model


###Sudoku_initialisation manuelle

def Sudoku():

    # Create the model.
    model = cp_model.CpModel()

    taille_case = 3
    taille_ligne = taille_case*3

    ligne = list(range(0, taille_ligne))
    case = list(range(0, taille_case))

    # print(ligne)
    # print(len(ligne))

    #Initialisation de la grille
    grille_init = [[0, 6, 0, 0, 5, 0, 0, 2, 0], [0, 0, 0, 3, 0, 0, 0, 9, 0],[7, 0, 0, 6, 0, 0, 0, 1, 0], [0, 0, 6, 0, 3, 0, 4, 0, 0], [0, 0, 4, 0, 7, 0, 1, 0, 0], [0, 0, 5, 0, 9, 0, 8, 0, 0], [0, 4, 0, 0, 0, 1, 0, 0, 6],[0, 3, 0, 0, 0, 8, 0, 0, 0], [0, 2, 0, 0, 4, 0, 0, 5, 0]]
    print('Grille initiale :\n')



    init = ''
    for i in range (len(grille_init)) :
        for j in range (len(grille_init)) :
            # print(i,j)
            if j%3==2 : init += str(grille_init[int(i)][int(j)])+' |'
            else : init += str(grille_init[int(i)][int(j)])+' '

        if i%3==2 : init += '\n'+'_ _ _  _ _ _  _ _ _ '+'\n\n'
        else : init += '\n'
    print(init)

    grille = {}

    for i in ligne:
        for j in ligne:
            grille[(i, j)] = model.NewIntVar(1, taille_ligne, 'grid %i %i' % (i, j))


    #Lignes - contraintes
    for i in ligne:
        model.AddAllDifferent([grille[(i, j)] for j in ligne])

    #Colonnes - contraintes
    for j in ligne:
        model.AddAllDifferent([grille[(i, j)] for i in ligne])


    #Cases - contraintes
    for i in case:

        for j in case:
            case_1 = []

            for di in case:

                for dj in case:
                    case_1.append(grille[(i * taille_case + di,
                                          j * taille_case + dj)])
            model.AddAllDifferent(case_1)



    # On initialise les valeurs
    for i in ligne:
        for j in ligne:
            if grille_init[i][j]:
                model.Add(grille[(i, j)] == grille_init[i][j])



    # Solve
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE:
        # for i in ligne:
        #     print([int(solver.Value(grille[(i, j)])) for j in ligne])
        print('La grille résolue : \n')
        solution = ''
        for i in ligne :
            for j in ligne :
                if j%3==2 : solution += str(int(solver.Value(grille[(i, j)])))+' |'
                else : solution += str(int(solver.Value(grille[(i, j)])))+' '

            if i%3==2 : solution += '\n'+'_ _ _  _ _ _  _ _ _ '+'\n\n'
            else : solution += '\n'
        print(solution)







###Sudoku avec grille aléatoire à remplir en fonction de la difficulté
import random


def Sudoku_bis():

    print('Si le programme ne génère pas directement une grille, veuillez interrompre le processus et relancer le programme.\nMerci.\n\n')

    # Create the model.
    model = cp_model.CpModel()

    taille_case = 3
    taille_ligne = taille_case*3

    ligne = list(range(0, taille_ligne))
    case = list(range(0, taille_case))

    # print(ligne)
    # print(len(ligne))



    #Initialisation de la grille
    grille_init = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 6, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    grille_trouvee=False

    #on cherche une grille aléatoire résolvable
    while not grille_trouvee:

        liste=[1,2,3,4,5,6,7,8,9]
        k=0
        while liste!=[]:
            grille_init[0][k]=random.choice(liste)
            #print(liste)
            liste.remove(grille_init[0][k])
            k+=1

        #print('Grille initiale :\n')



        # init = ''
        # for i in range (len(grille_init)) :
        #     for j in range (len(grille_init)) :
        #         # print(i,j)
        #         if j%3==2 : init += str(grille_init[int(i)][int(j)])+' |'
        #         else : init += str(grille_init[int(i)][int(j)])+' '
        #
        #     if i%3==2 : init += '\n'+'_ _ _  _ _ _  _ _ _ '+'\n\n'
        #     else : init += '\n'
        # print(init)

        grille = {}

        for i in ligne:
            for j in ligne:
                grille[(i, j)] = model.NewIntVar(1, taille_ligne, 'grid %i %i' % (i, j))


        #Lignes - contraintes
        for i in ligne:
            model.AddAllDifferent([grille[(i, j)] for j in ligne])

        #Colonnes - contraintes
        for j in ligne:
            model.AddAllDifferent([grille[(i, j)] for i in ligne])


        #Cases - contraintes
        for i in case:

            for j in case:
                case_1 = []

                for di in case:

                    for dj in case:
                        case_1.append(grille[(i * taille_case + di,
                                            j * taille_case + dj)])
                model.AddAllDifferent(case_1)



        # On initialise les valeurs
        for i in ligne:
            for j in ligne:
                if grille_init[i][j]:
                    model.Add(grille[(i, j)] == grille_init[i][j])



        # Solve
        solver = cp_model.CpSolver()
        status = solver.Solve(model)

        if status == cp_model.FEASIBLE:
            # for i in ligne:
            #     print([int(solver.Value(grille[(i, j)])) for j in ligne])
            # print('La grille résolue : \n')
            # solution = ''
            # for i in ligne :
            #     for j in ligne :
            #         if j%3==2 : solution += str(int(solver.Value(grille[(i, j)])))+' |'
            #         else : solution += str(int(solver.Value(grille[(i, j)])))+' '
            #
            #     if i%3==2 : solution += '\n'+'_ _ _  _ _ _  _ _ _ '+'\n\n'
            #     else : solution += '\n'
            # print(solution)

            grille_trouvee=True
            #print(status)



    print('Une grille a été générée\n')

    #On a la grille aléatoirement remplie
    #On cache mnt un certain nombre de case
    niveau=0
    while niveau not in [1,2,3,4,5]:
        print('A quel niveau de jeu voulez-vous jouer :\n1-débutant\n2-facile\n3-moyen\n4-difficile\n5-très difficile')
        niveau=eval(input('Niveau choisi : '))

    print('Vous avez choisi le niveau ',niveau)

    #print(grille[0,0])

    nb_cases = 0
    if niveau==1: nb_cases=50
    elif niveau==2: nb_cases=40
    elif niveau==3: nb_cases=33
    elif niveau==4: nb_cases=26
    else : nb_cases=17

    ratio = nb_cases/(9**2)

    print('\n\nLa grille à résoudre est la suivante, à vous de jouer : \n')
    solution = ''
    for i in ligne :
        for j in ligne :
            rd=random.uniform(0,1)
            if j%3==2 and rd<=ratio : solution += str(int(solver.Value(grille[(i, j)])))+' |'
            elif j%3==2 and rd>ratio : solution += '  |'
            elif j%3!=2 and rd<=ratio : solution += str(int(solver.Value(grille[(i, j)])))+' '
            else : solution += '  '

        if i%3==2 : solution += '\n'+'_ _ _  _ _ _  _ _ _ '+'\n\n'
        else : solution += '\n'
    print(solution)
    print('\nVoulez-vous afficher la solution ?')

    reponse = eval(input('0-Non\n1-Oui\nVotre réponse :'))

    if reponse :
            print('\nVoici la grille résolue : \n')
            solution = ''
            for i in ligne :
                for j in ligne :
                    if j%3==2 : solution += str(int(solver.Value(grille[(i, j)])))+' |'
                    else : solution += str(int(solver.Value(grille[(i, j)])))+' '

                if i%3==2 : solution += '\n'+'_ _ _  _ _ _  _ _ _ '+'\n\n'
                else : solution += '\n'
            print(solution)
    else: print('Vous avez choisi de ne pas voir la solution.\nBon courage pour votre résolution.')






