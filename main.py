import random
from random import randint
from initial_population import InitialPopulation
import pandas as pd


#sanitize data Functions
extract_dataframe = lambda file: pd.DataFrame(pd.read_csv(file)) #convert CSV file to pandas dataframe



if __name__ == '__main__':
    first_pop = InitialPopulation()
    first_pop.create_population()
    first_pop.print_population()


  





    '''    
    
    
    letras = "!,.:;?áÁãÃâÂõÕôÔóÓéêÉÊíQWERTYUIOPASDFGHJKLÇZXCVBNMqwertyuiopasdfghjklçzxcvbnm1234567890 "
    lista_letras = list(letras)
    populacao1 = []



    for pop in range(400):
        individuo=""
        for contador in range(9):
            if(contador==0):
                gene="O"
            else:
                indice=(randint(0,87))
                gene = lista_letras[indice]
            individuo=individuo+gene
        populacao1.append(individuo)

    #for individuo in populacao:
    #    print(individuo)

    populacao2=[]
    populacao2.append(populacao1[0])


    pais = random.sample(populacao,2)
    pai1= pais[0]
    pai2 = pais[1]

    print("PAIS")
    print(pai1)
    print(pai2)
    print("\n")


    pai1_1=pai1[:5]
    pai1_2=pai1[5:]

    pai2_1=pai2[:5]
    pai2_2=pai2[5:]

    filho1=pai1_1+pai2_2
    filho2=pai2_1+pai1_2

    print("FILHOS")
    print(filho1)
    print(filho2)

    '''