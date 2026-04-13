# Programa de Pesquisa de Opinião - TudoWeb

qtd_excelente = 0
qtd_ruim = 0

# Loop para 50 entrevistados
for i in range(1, 51):
    print(f"\nEntrevistado {i}")

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opção: "))

    # Estrutura de decisão
    if opiniao == 1:
        qtd_excelente += 1
    elif opiniao == 3:
        qtd_ruim += 1
    elif opiniao == 2:
        pass  # não precisa contar o "BOM"
    else:
        print("Opção inválida!")

# Resultado final
print("\n===== RESULTADO DA PESQUISA =====")
print(f"Quantidade de respostas EXCELENTE: {qtd_excelente}")
print(f"Quantidade de respostas RUIM: {qtd_ruim}")