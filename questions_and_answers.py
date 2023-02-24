# Questions and Answers system

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print()
    qtt_options = len(pergunta['Opções'])
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i})', opcao)
        print()
    
    while True:
        user_answer = input('Which is the correct answer? ')
        user_answer = int(user_answer)
        if  user_answer>=0 and user_answer<qtt_options:
            if pergunta['Resposta'] == pergunta['Opções'][user_answer]:
                print('Your answer is correct.')
                break
            else:
                print('Your answer is not correct.')
                break

        print('Type a valid option.')
        continue

