"""

Include in a program a method for
read the size of an array to integers from the keyboard,
as well as all of its elements, ensuring it only has positive and even values.
Check that the size (or dimension) is not null or negative.
To test, read different amounts of data.

"""

def read_array():
    while True:
        #ler
        array = []
        length = input('Insira o tamanho: ')
        length = int(length)
        for i in range(0, length):
            j = input(f'Insira um valor no índice {i}: ')
            while ((int(j)%2)!=0 or int(j)<=0):
                print('Insira somente valores positivos e pares.')
                j = input(f'Insira um valor no índice {i}: ')

            array.append(int(j))

        #verifica
        if(len(array)<=0):
            print('Este arranjo tem valor inválido.')
            continue
            
        #printa
        print(array)
        break

read_array()
