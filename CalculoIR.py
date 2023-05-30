#Calculadora de Imposto(Valores Ficticios)

#Declarando variavel que lê valor do imposto do user

income = float(input("Enter the annual income: "))

#Codição de valores do imposto

if income <= 85528:
  tax = (income * 0.18) - 556.02 


elif income > 85528:
  tax = (income - 85528) * 0.32 + 14839.02

#Arrendondando Valor do Imposto

tax = round(tax, 0)

#Mostrando na Tela resolução
print("The tax is:", tax, "thalers")
