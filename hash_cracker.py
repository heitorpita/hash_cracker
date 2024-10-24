import hashlib

def criar_md5(senha):
    return hashlib.md5(senha.encode()).hexdigest()

def criar_sha1(senha):
    return hashlib.sha1(senha.encode()).hexdigest()

def criar_sha256(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def main():
    tipo_hash = input("Digite o tipo de hash (md5, sha1, sha256): ").strip().lower()
    hash_alvo = input("Digite o hash alvo: ").strip()
    
    arquivo_rockyou = r"C:\Users\heito\OneDrive\Documentos\GitHub\hash-cracker\senhas.txt" 

    try:
        with open(arquivo_rockyou, 'r', encoding="latin-1") as arquivo:
            for senha in arquivo:
                senha = senha.strip()
                hash_criado = None

                if tipo_hash == "md5":
                    hash_criado = criar_md5(senha)
                elif tipo_hash == "sha1":
                    hash_criado = criar_sha1(senha)
                elif tipo_hash == "sha256":
                    hash_criado = criar_sha256(senha)

                if hash_criado == hash_alvo:
                    print(f"Hash encontrado! A Palavra é: {senha}")
                    return

            print("Nada encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
