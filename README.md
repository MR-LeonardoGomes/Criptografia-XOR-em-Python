#  BY:Mr-LeonardoGomes 🚀 
#  Script de Criptografia XOR em Python 🐍


Este será seu "criador de payloads". Ele pega um payload bruto (gerado por ferramentas como o msfvenom) e o embaralha usando uma chave XOR.

Conceitos-chave:

Operador : Em Python, o operador ^ realiza a operação XOR bit a bit .

Funcionamento: Iteramos byte a byte do payload e aplicamos a operação XOR com um byte da nossa chave. Se a chave for mais curta que o payload, podemos repeti-la (criando uma chave de ciclo) .

Exemplo de Script (xor_encrypt.py):
