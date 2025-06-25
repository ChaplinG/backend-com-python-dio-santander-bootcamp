#Uma empresa quer validar se os e-mails cadastrados pelos usuários estão no formato correto
# Regras para um e-mail válido:
# - Deve conter o caractere "@" e um domínio, como gmail.com ou outlook.com.
# - Não pode começar ou terminar com "@".
# - Não pode conter espaços.
#Sáidas apenas como "E-mail válido" ou "E-mail inválido"

# Entrada do usuário
email = input().strip()

# TODO: Verifique as regras do e-mail:
dominios_email = {"gmail.com", "hotmail.com", "outlook.com"}

if email.count("@") == 1 and " " not in email:
  nome_usuario, dominio = email.split("@")
  
  if nome_usuario != "" and dominio in dominios_email:
    print("E-mail válido")
    
  else:
    print("E-mail inválido")
    
else:
  print("E-mail inválido")