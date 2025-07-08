#Uma loja online deseja aplicar descontos em seus produtos com base em cupons de desconto digitados pelos clientes
#como entrada recebe Preço do produto e código do Cupom
#preço final após aplicar o desconto. Com duas casas decimais

# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# TODO: Aplique o desconto se o cupom for válido:
if cupom in descontos:
    desconto_aplicado = descontos[cupom]
    valor_final = preco-(preco*descontos[cupom])
    print(f"{valor_final:.2f}")
    
else:
  print("Cupom inválido! \nTente novamente")