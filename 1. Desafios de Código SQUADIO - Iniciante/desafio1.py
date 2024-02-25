# Desafio: A Aventura do Explorador

'''
exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Se o input for:	
2

O output deve ser:
Explorador: 1 passo
Explorador: 2 passos

Se o input for:
3

O output deve ser:
Explorador: 1 passo
Explorador: 2 passos
Explorador: 3 passos
'''

# TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.
# Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
# Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.

# SOLUÇÃO e EXPLICAÇÃO:
quantidade_passos = int(input()) # quantidade de passos que o explorador deu na floresta 

if quantidade_passos <= 0: # Verifica se a quantidade de passos é positiva
    print("Nenhum passo dado na floresta.") # Imprime a mensagem caso a quantidade de passos seja zero
else:
    # Loop for para imprimir a mensagem do explorador
    for passo in range(1, quantidade_passos + 1): # Loop for para imprimir a mensagem do explorador indicando o número do passo
      if passo == 1: # Verifica se o número do passo é igual a 1
        print(f"Explorador: {passo} passo") # Imprime a mensagem do explorador indicando o número do passo
      else: # Caso contrário
        print(f"Explorador: {passo} passos") # Imprime a mensagem do explorador indicando os número dos passos (no plural)

