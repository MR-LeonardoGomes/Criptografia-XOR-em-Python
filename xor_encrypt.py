import argparse
import os

def xor_encrypt_decrypt(data: bytes, key: bytes) -> bytes:
    """
    BY:Mr-LeonardoGomes 🚀 
    Aplica a operação XOR nos dados usando a chave fornecida.
    Como XOR é reversível, a mesma função serve para criptografar e descriptografar.
    """
    # Repete a chave para que ela tenha o mesmo tamanho dos dados
    # Explicação: Se a chave for menor, ela é repetida ciclicamente [citatcao:1]
    key_repeated = key * (len(data) // len(key)) + key[:len(data) % len(key)]
    
    # Aplica XOR em cada byte
    # Usamos zip para iterar sobre os bytes dos dados e da chave simultaneamente
    encrypted_bytes = bytes([b ^ k for b, k in zip(data, key_repeated)])
    return encrypted_bytes

def main():
    parser = argparse.ArgumentParser(description='Criptografa/Descriptografa um payload com XOR.')
    parser.add_argument('-f', '--file', required=True, help='Arquivo com o payload bruto (ex: payload.bin)')
    parser.add_argument('-o', '--output', required=True, help='Arquivo de saída para o payload criptografado')
    parser.add_argument('-k', '--key', help='Chave XOR (em formato string). Se não for fornecida, uma aleatória será gerada.')
    parser.add_argument('--key-output', help='Arquivo para salvar a chave (útil se ela for gerada).')
    
    args = parser.parse_args()
    
    # 1. Ler o payload bruto do arquivo
    with open(args.file, 'rb') as f:
        payload = f.read()
    print(f"[*] Payload lido: {len(payload)} bytes")
    
    # 2. Definir ou gerar a chave
    if args.key:
        key = args.key.encode()  # Converte string para bytes
        print(f"[*] Usando chave fornecida: {args.key}")
    else:
        # Gera uma chave aleatória de 16 bytes (128 bits) [citation:2][citation:9]
        key = os.urandom(16)
        print(f"[*] Chave aleatória gerada (salve-a!): {key.hex()}")
        if args.key_output:
            with open(args.key_output, 'w') as kf:
                kf.write(key.hex())
            print(f"[*] Chave salva em: {args.key_output}")
    
    # 3. Criptografar o payload
    encrypted_payload = xor_encrypt_decrypt(payload, key)
    
    # 4. Salvar o payload criptografado
    with open(args.output, 'wb') as f:
        f.write(encrypted_payload)
    print(f"[*] Payload criptografado salvo em: {args.output} ({len(encrypted_payload)} bytes)")
    print(f"[*] Lembre-se: para descriptografar, use a mesma chave!")

if __name__ == "__main__":
    main()
