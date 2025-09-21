import random 

def definidor_de_barris():
    barris = int(input("Quantos barris serão?"))
    return barris_envenenados(barris)

def barris_envenenados(num_barris):
    barril_envenenado = random.randint(1, num_barris)

    num_prisioneiros = (num_barris - 1).bit_length()
    prisioneiros_mortos = []

    for i in range(num_prisioneiros):
        if(barril_envenenado >> i) & 1:
            prisioneiros_mortos.append(i + 1)
    
    print("Prisioneiros mortos:")
    if prisioneiros_mortos:
        print(f"{prisioneiros_mortos}")
    else: 
        print("Nenhum prisioneiro foi morto")
    
    barril_encontrado_binario = ['0'] * num_prisioneiros

    for prisioneiro in prisioneiros_mortos:
        barril_encontrado_binario[prisioneiro - 1] = '1'

    barril_encontrado_binario.reverse()
    barril_encontrado = int("".join(barril_encontrado_binario), 2)

    print(f"O barril envenenado foi o: {barril_encontrado}")

    return barril_envenenado, barril_encontrado