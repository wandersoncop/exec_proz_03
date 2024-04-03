print ("Digite seu nome completo:")
nome = input()
print("ola ",nome," como vai?")


executar = True

while(executar == True):
    print ("digite seu ano de nascimento")
    try:
        ano = int(input())
        if(ano < 1922) or (ano>2021):
            print("o ano precisa ser entre 1922 e 2021")
        else:
            idade = 2022 - ano
            print ("Oi ", nome, "você completou ou completará", idade, "anos de idade em 2022")
            executar = False
    except:
        print("os anos precisan ser escritos apenas com  numeros")