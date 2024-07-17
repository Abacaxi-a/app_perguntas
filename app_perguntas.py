perguntas = [
    {
        'pergunta':'quanto é 2+2:',
        'resposta':'4',
        'alternativas':['4','3','2','1']
    },
    {
        'pergunta':'quantas letras tem o alfabeto:',
        'resposta':'26',
        'alternativas':['32','26','27','5']
    },
]

resultado = 0
for pergunta in perguntas:
    print(pergunta['pergunta'])
    
    opcoes = range(1,5)
    dic = {}
    for opcao,alternativa in zip(opcoes,pergunta['alternativas']) :
        dic[opcao] = alternativa
        print(f'{opcao}) resposta: {alternativa}')
    resposta = int(input('escolha uma das alternativas: '))

    if str(resposta) in str(dic):
        res = dic[resposta]
        if res == pergunta['resposta']:
            print('NICE')
            resultado += 1
            print()
        else:
            print('erro, próxima')
            print()
    else:
        print('alternativa não existe')
print(f'Você acertou : {resultado}')