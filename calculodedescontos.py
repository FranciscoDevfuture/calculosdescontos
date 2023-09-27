print("*"*5 + " Bem Vindos à loja de Francisco " + "*"*5)

valor_produto = float(input('Entre com o valor desejado:'))
qtd_produto= int(input('Entre com a quantidade desejada:'))
desconto_produto = 0
if qtd_produto <= 4:
  desconto_produto = 0.00
elif 5 <= qtd_produto < 20:
  desconto_produto = 0.03
elif 20 <= qtd_produto < 100:
  desconto_produto=0.6
else:
  desconto_produto=0.10
total_sem_desconto = valor_produto*qtd_produto
print('O valor SEM desconto é de : R$ {:.2f}'.format(total_sem_desconto))
total_com_desconto = valor_produto*qtd_produto
print('O valor COM desconto é de : R$ {:.2f}'.format(total_com_desconto))


